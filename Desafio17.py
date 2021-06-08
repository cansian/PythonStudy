import math

cateto_o = float(input("Digite o comprimento do cateto oposto: "))
cateto_a = float(input("Digite o comprimento do cateto adjacente: "))
print("O comprimento da hipotenusa é {:.2f}".format(math.sqrt(cateto_o**2 + cateto_a**2)))
