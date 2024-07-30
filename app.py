import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from flask import Flask, render_template, request, send_from_directory, send_file

app = Flask(__name__)

# Directorio para guardar imágenes y archivo CSV
IMAGE_DIR = 'static/images'
CSV_FILE = 'user_data.csv'

# Función para leer datos
def read_data(csv_file):
    df = pd.read_csv(csv_file, encoding='utf-8')
    return df

# Función para codificar datos
def encode_data(df):
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.astype(int)  # Convertir valores booleanos a enteros
    return df_encoded


# Función para estandarizar datos
def standardize_data(df_encoded):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_encoded)
    return scaled_data

# Función para aplicar PCA
def apply_pca(data, n_components=2):
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data)
    df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    return df_pca

# Función para aplicar algoritmos de clustering
def apply_clustering(df_encoded, algorithm='kmeans'):
    if algorithm == 'kmeans':
        model = KMeans(n_clusters=3)
    elif algorithm == 'dbscan':
        model = DBSCAN(eps=0.5, min_samples=5)
    else:
        raise ValueError("Algoritmo no soportado: elige 'kmeans' o 'dbscan'")
    
    clusters = model.fit_predict(df_encoded)
    df_encoded['Cluster'] = clusters
    return df_encoded

# Función para generar la gráfica de clusters
def generate_cluster_plot(df_encoded, algorithm):
    plt.figure(figsize=(10, 6))
    x_col = df_encoded.columns[0]
    y_col = df_encoded.columns[1]

    sns.scatterplot(x=x_col, y=y_col, hue='Cluster', data=df_encoded, palette='viridis', legend='full')
    plt.title(f'Clustering usando {algorithm.upper()}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plot_filename = f'cluster_plot_{algorithm}.png'
    plot_path = os.path.join(IMAGE_DIR, plot_filename)

    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    return plot_filename


# Función para obtener datos codificados como HTML
def get_encoded_data_html(csv_file):
    df = read_data(csv_file)
    df_encoded = encode_data(df)
    return df_encoded.to_html()

# Main function
def main(csv_file, algorithm='kmeans'):
    # Leer datos
    df = read_data(csv_file)
    print(f"Total entries in CSV: {len(df)}")
    
    # Codificar datos
    df_encoded = encode_data(df)
    print(f"Total entries after encoding: {len(df_encoded)}")
    
    # Estandarizar datos
    scaled_data = standardize_data(df_encoded)
    
    # Aplicar PCA
    df_pca = apply_pca(scaled_data)
    
    # Aplicar clustering
    df_clustered = apply_clustering(df_pca, algorithm)
    print(f"Cluster assignment counts:\n{df_clustered['Cluster'].value_counts()}")
    
    # Generar gráfica de clusters
    plot_filename = generate_cluster_plot(df_clustered, algorithm)
    
    return plot_filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    algorithm = request.form['algorithm']
    plot_filename = main(CSV_FILE, algorithm)
    return render_template('result.html', plot_filename=plot_filename, algorithm=algorithm)

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

@app.route('/submit', methods=['POST'])
def submit():
    # Recoger los datos del formulario
    form_data = request.form.to_dict()
    
    # Leer los datos existentes
    df = read_data(CSV_FILE)
    
    # Agregar los nuevos datos al DataFrame
    df = pd.concat([df, pd.DataFrame([form_data])], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(CSV_FILE,encoding='utf-8', index=False)
    
    return render_template('choose_algorithm.html')

@app.route('/download_csv')
def download_csv():
    return send_file(CSV_FILE, as_attachment=True, mimetype='text/csv')

@app.route('/encoded_data')
def encoded_data():
    encoded_data_html = get_encoded_data_html(CSV_FILE)
    return render_template('encoded_data.html', encoded_data_html=encoded_data_html)

if __name__ == '__main__':
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    app.run(debug=True)
