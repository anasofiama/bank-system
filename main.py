menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500.00
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(f"Por favor, selecione uma operação para dar seguimento: {menu}")

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        while valor<=0:
            valor = float(input("Valor inválido!\nVocê deve depositar um valor superior a R$ 0,00.\nDigite novamente o valor do depósito:"))

        extrato.append(f"Depósito: R$ {valor:.2f}")
        saldo += valor


    elif opcao == "s":

        if numero_saques >= LIMITE_SAQUES:
            print(f"Operação falhou! Número máximo de saques diários excedido. Você só pode realizar {LIMITE_SAQUES} saques por dia.")
            continue
        
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite} permitido para sua conta.")


        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar os nossos serviços.\nAté a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
