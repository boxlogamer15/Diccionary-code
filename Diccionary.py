meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador o siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

print(" ¡Bienvenido al diccionario moderno!")
print(" Escribe palabras en MAYÚSCULAS para conocer su significado.")
print(" Puedes consultar hasta 5 palabras.\n")

for i in range(5):
    word = input(f"({i+1}/5) Escribe una palabra: ")

    if word in meme_dict:
        print("👉 Significado:", meme_dict[word])
    else:
        print("❌ Lo siento, no conozco esa palabra.")
    
    print()  

print(" Gracias por usar el diccionario. ¡Hasta luego!")