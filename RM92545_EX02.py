numero = int(input("Informe os minutos do horário atual: "))

resultado = 1
count = 1

while count <= numero:
    resultado = resultado * count
    count = count + 1

print(f"A senha para desbloqueio é: LIBERDADE{resultado}")
