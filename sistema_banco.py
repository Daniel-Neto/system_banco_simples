menu = """
    [d] -> Depositar
    [s] -> Sacar
    [e] -> Extrato
    [v] -> Sair

"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao=="d":
        valor = float(input("Informe o valor do depósito:"))
        
        if valor > 0:
            saldo += valor
            extrato = f"Depósito realizado no valor R$ {valor:.2f}\n"
        else:
            print("Falha na operação. O valor informado é inválido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado:"))

        if valor > saldo:
            print("Operação falhou! Não há saldo suficiente na conta.")
        elif valor > limite:
            print("Falha na operação. Não é possível sacar mais que 500 reais por dia.")
        elif numero_saques > LIMITE_SAQUES:
            print("Falha na operação. O número de saques excedeu o limite.")
        elif valor > 0:
            saldo -= valor
            numero_saques +=1
            extrato = f"Saque realizado no valor R$ {valor:.2f}\n"
        else:
            print("Falha na operação. O valor informado é inválido.")
    
    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas movimentações")
        else:
            print("=============EXTRATO============")
            print(f"Saldo R$ {saldo:.2f}")
            print("----------------------------------")
    
    elif opcao == "v":
        break

    else:
        print("Operação inválida, tente novamente.")