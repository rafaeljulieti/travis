'''Conversao de temperatura: Celcius para fahrenheit (Usuario deve digitar "F"),
fahrenheit para Celcius (Usuario deve digitar "C") e a terceira opcao de digitar
valor invalido. Mostrar temperatura convertida ou valor invalido.'''
grau = input("Digite C (Converte de C para F) ou digite F (Converte de F para C):")
temp = float(input("Digite a temperatura:"))

if grau == "C" or grau == "c":
    print ("Sao %.2f"%((temp*1.8)+32), "graus fahrenheit.")
elif grau == "F" or grau == "f":
    print ("Sao %.2f"%((temp - 32)/1.8), "graus Celcius.")
else:
    print ("Opcao invalida")
