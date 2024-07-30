import pandas as pd
import random

# Define las opciones para cada característica
zodiac_signs = ["Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio"]
energy_levels = ["Alto", "Medio", "Bajo"]
new_experiences = ["Entusiasta", "Abierto", "No me gustan"]
valued_qualities = ["Libertad personal", "Comodidad y seguridad", "Conocimiento y aprendizaje"]
important_in_relationships = ["Lealtad y fidelidad", "Empatía y cariño", "Carisma y creatividad"]
adaptabilities = ["Muy adaptable", "Puedo adaptarme", "No soy muy flexible"]
communications = ["Me gusta hablar", "Prefiero escuchar", "No me siento cómodo"]
curiosities = ["Muy curioso/a", "Algo curioso/a", "No siento una gran curiosidad"]
personal_qualities = ["Empatía y sensibilidad", "Ambición y determinación", "Lealtad y protección"]
preferred_environments = ["Uno lleno de estímulos", "Un ambiente tranquilo", "Un espacio intelectualmente estimulante"]
emotion_managements = ["Las expreso abiertamente", "Las gestiono internamente", "No suelo expresarlas mucho"]
attractive_qualities = ["Su creatividad y originalidad", "Su lealtad y sinceridad", "Su empatía y apoyo emocional"]
leaderships = ["Me siento cómodo/a", "Puedo liderar si es necesario", "No me gusta liderar"]
challenge_approaches = ["Perseverar hasta lograr", "Buscar el camino más placentero", "Evaluar las opciones con calma"]

# Genera datos aleatorios
data = {
    "ZodiacSign": [random.choice(zodiac_signs) for _ in range(1000)],
    "energyLevel": [random.choice(energy_levels) for _ in range(1000)],
    "newExperiences": [random.choice(new_experiences) for _ in range(1000)],
    "valuedQuality": [random.choice(valued_qualities) for _ in range(1000)],
    "importantInRelationships": [random.choice(important_in_relationships) for _ in range(1000)],
    "adaptability": [random.choice(adaptabilities) for _ in range(1000)],
    "communication": [random.choice(communications) for _ in range(1000)],
    "curiosity": [random.choice(curiosities) for _ in range(1000)],
    "personalQuality": [random.choice(personal_qualities) for _ in range(1000)],
    "preferredEnvironment": [random.choice(preferred_environments) for _ in range(1000)],
    "emotionManagement": [random.choice(emotion_managements) for _ in range(1000)],
    "attractiveQuality": [random.choice(attractive_qualities) for _ in range(1000)],
    "leadership": [random.choice(leaderships) for _ in range(1000)],
    "challengeApproach": [random.choice(challenge_approaches) for _ in range(1000)]
}

# Crea un DataFrame y guarda los datos en un archivo CSV
df = pd.DataFrame(data)
df.to_csv('random_user_data.csv', index=False)

print("Datos aleatorios generados y guardados en 'random_user_data.csv'")
