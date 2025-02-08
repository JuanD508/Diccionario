import time
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Una respuesta a una broma",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("Esa palabra no está en el diccionario")
    time.sleep(1)
#Hola
