import math

angulo = float(input("Digite o angulo que deseja calcular o seno , cosseno e tangente: "))
angulo_r = math.radians(angulo)
seno = math.sin(angulo_r)
cosseno = math.cos(angulo_r)
tangente = math.tan(angulo_r)

print("O seno é {}, cosseno é {} e a tangente é {} ".format(seno, cosseno, tangente))
