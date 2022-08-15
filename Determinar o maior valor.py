print("=================ExercicioDankicode for=======================")
from time import sleep
maior = int(input("Informe um valor : "))
menor = int(input("Informe outro valor : "))
x = 100
while x < 120:
    x = x + 1
    if x > maior :
        print("agora {}, será o maior valor.".format(x))
        sleep(1)
    elif maior > x :
        print("O valor {}, digitado por voce será o maior.".format(maior))
       
while x < 120:
     x = x + 1
if x < menor :
        print("Agora {},será o menor valor.".format(x))

elif menor < x :
        print("O valor {},digitado por voce é o menor.".format(menor))

x1 = int(input("Determine o primeiro valor do intervalo : "))
x2 = int(input("Determine o primeiro valor do intervalo : "))
for x in range(x1,x2):
    if x > maior :
        print("agora {}, será o maior valor.".format(x))
        sleep(1)
    elif maior > x :
        print("O valor {}, digitado por voce será o maior.".format(maior))


        
for x in range(x1,x2):
    if x < menor :
        print("agora {}, será o maior valor.".format(x))
        sleep(1)
    elif menor < x :
        print("O valor {}, digitado por voce será o maior.".format(maior))    

