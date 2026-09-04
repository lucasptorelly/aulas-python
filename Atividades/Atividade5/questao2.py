vogal = input("Digite uma letra do alfabeto: ")

match vogal:
    case "a" | "e" | "i" | "o" | "u":
        print("Essa letra é uma vogal")
    case _:
        print("Não é uma vogal")