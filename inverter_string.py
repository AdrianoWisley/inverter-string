import string

def inverter_string(texto):
  
    texto_invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

if __name__ == "__main__":
    while True:
        texto = input("Digite uma palavra para inverter (ou 'sair' para encerrar): ")

        if texto.lower() == "sair":
            break

        if not texto.isalpha():
            print("Por favor, digite apenas letras.")
            continue

        
        if any(char not in string.ascii_letters for char in texto):
            print("A palavra não deve conter caracteres especiais.")
            continue

        if not texto:
            print("Por favor, digite uma palavra válida.")
            continue

        try:
            texto_invertido = inverter_string(texto)
            print(f"A string invertida é: {texto_invertido}")
        except TypeError:
            print("Por favor, digite apenas texto.")