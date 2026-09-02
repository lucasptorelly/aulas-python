senha_digitada = int(input("Digite sua senha: "))
senha_cadastrada = 1234
acesso_liberado = senha_cadastrada == senha_digitada

print("Acesso liberado?", acesso_liberado)


#O primeiro erro encontrado é a ordem está incorreta entre senha_cadastrada e senha_digitada e o segundo erro é
# necesário colocar o int antes od input para que ele entenda como um numero a resposta
