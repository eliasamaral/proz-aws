def conte_palavra(frase):
    palavras = frase.split()
    print(f"Número de palavras: {len(palavras)}")

def conte_caracter(frase):
    caracteres = len(frase.replace(" ", ""))
    print(f"Número de caracteres: {caracteres}")

while True:
    frase = input("Digite uma frase: ")
    opcao = input("Selecione uma opção: 1 - Contar palavras 2 - Contar caracteres 3 - Sair\n")

    try:
        if opcao == 1:
            conte_palavra(frase)
        elif opcao == 2:
            conte_caracter(frase)
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    except: 
        print("Opção inválida.")