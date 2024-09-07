def add_operacao(extrato, operacao):
     extrato.append(operacao)

def depositar(extrato, saldo=0):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except:
        print("Valor incompatível! Operação encerrada.")
        return saldo
    
    while valor<=0:
        try:
            valor = float(input("Valor inválido!\nVocê deve depositar um valor superior a R$ 0,00.\nDigite novamente o valor do depósito:"))
        except:
            print("Valor incompatível! Operação encerrada.")
            return saldo
    
    add_operacao(extrato, f"Depósito: R$ {valor:.2f}")
    saldo += valor

    return saldo

def sacar(extrato, saldo, numero_saques, LIMITE_SAQUES = 3, limite = 500.00):

    if numero_saques >= LIMITE_SAQUES:
            print(f"Operação falhou! Número máximo de saques diários excedido. Você só pode realizar {LIMITE_SAQUES} saques por dia.")
            return saldo, numero_saques
    
    try:
        valor = float(input("Informe o valor do saque: "))
    except:
         print("Valor incompatível! Operação encerrada.")
         return saldo, numero_saques

    if valor > limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite} permitido para sua conta.")

    elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif valor > 0:
            saldo -= valor
            add_operacao(extrato, f"Saque: R$ {valor:.2f}")
            numero_saques += 1

    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques
    
def gerar_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = []
numero_saques = 0

while True:

    opcao = input(f"Por favor, selecione uma operação para dar seguimento: {menu}")

    if opcao == "d":
        saldo = depositar(extrato, saldo=saldo)

    elif opcao == "s":
        saldo, numero_saques = sacar(extrato, saldo, numero_saques)

    elif opcao == "e":
        gerar_extrato(extrato, saldo)

    elif opcao == "q":
        print("Obrigado por utilizar os nossos serviços.\nAté a próxima!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
