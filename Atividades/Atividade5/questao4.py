mes = int(input("Digito um número correspondente ao mês do ano"))

match mes:
    case 12 | 1 | 2:
        print("Verão")
    case 3 | 4 | 5:
        print("outono")
    case 6 | 7 | 8:
        print("inverno")
    case 9 | 10 | 11:
        print("primavera")
    case _:
        print("erro")
