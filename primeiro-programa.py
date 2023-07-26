menu = """

[1] Depositário
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques =0
LIMITE_SAQUES = 3


while True:

    opção = input(menu)

    if opção == "1":
        
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n "
        
        else:
            print("Operação Não Realizada! O valor depositado e invalido.")

    elif opção == "2":
        valor = float(input("informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("Operação não realizada! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Não realizada! O valor de saque excede o limite. ")

        elif excedeu_saques:

            print("Operação Não Realizada! Numero maximo de saques excedido.")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n "
            numero_saques += 1

        else:
            print("Operação Não Realizada!o valor informado é invalido.")


    elif opção == "3":
        print("\n========================= EXTRATO =================== ==")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("==================================================== ============")

    elif opção == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
