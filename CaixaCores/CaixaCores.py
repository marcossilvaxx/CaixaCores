cores = {}

def AdicionarCor():
    cor = str(input("Informe uma cor:\n"))
    hexad = str(input("Informe o código hexadecimal correspondente à cor:\n"))
    cores[cor] = hexad
    print("Cor %s adicionada." % cor)

def ListarCores():
    print("A caixa de cores contém atualmente as seguintes cores:\n")
    for i in cores.items():
        print(i)

def ExibirMenu():
    pergunta = str(input("Para adicionar uma cor à caixa de cores, digite 1. Para ver as cores já adicionadas à caixa de cor, digite 2. Para sair, digite 0:\n"))
    if pergunta == "1":
        AdicionarCor()
    elif pergunta == "2":
        ListarCores()
    elif pergunta == "0":
        return "0"

while True:
    ExibirMenu()
    if ExibirMenu() == "0":
        print("Programa encerrado.")
        break