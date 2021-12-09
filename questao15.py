while True:
    print(
    """
1- adição
2- subtração
3- multiplicação
4- divisão
5- sair"""
    )
    opcao = int(input())

    if opcao ==1:
        for x in range(1,11):
            print(f"tabuada de soma do {x}")
            for y in range(1,11):
                print(f"{x} + {y} = {x+y}")
            print()

    elif opcao ==2:
        for x in range(1,11):
            print(f"tabuada de subtração do {x}")
            for y in range(1,11):
                print(f"{x} - {y} = {y-x}")
            print()

    elif opcao ==3:
        for x in range(1,11):
            print(f"tabuada da multiplicação do {x}")
            for y in range(1,11):
                print(f"{x} * {y} = {x*y}")
            print()

    elif opcao ==4:
        for x in range(1,11):
            print(f"tabuada da divisão do {x}")
            for y in range(1,11):
                print(f"{x} / {y} = {x/y}")
            print()

    elif opcao ==5:
        break