import random 

palabras = ["rosado", "morado", "azul", "naranja", "verde", "amarillo"]
palabra_escogida = random.choice(palabras) #aqui se selecciona una palabra de forma aleatoria

blanks = "" 
for i in range(len(palabra_escogida)):
    blanks += "_ "

print("Palabra:", blanks) #en esta parte se cambian las letras por _

letra_adivinada = []
numero_de_vidas = 7
game_over = False

while not game_over:
    print("Tienes", numero_de_vidas, "vidas!")
    adivina = input("Adivina una letra: ").lower()

    if adivina not in letra_adivinada:
        letra_adivinada.append(adivina)

    if adivina not in palabra_escogida:
        numero_de_vidas -= 1
        print(f"La letra {adivina} no está en la palabra. Pierdes una vida.")

    tu_palabra = ""
    for letra in palabra_escogida:
        if letra in letra_adivinada:
            tu_palabra += letra
        else:
            tu_palabra += "_ "

    print("Palabra:", tu_palabra)

    if "_ " not in tu_palabra:
        print("GANASTE")
        game_over = True

    if numero_de_vidas == 0:
        print(f"La palabra era {palabra_escogida}. PERDIOOOO")
        game_over = True
        
