turno = input("Digite o turno: ")

match turno:
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa noite!")
    case _:
        print("Bom dia!")
