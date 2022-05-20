#input

a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))

#processing

if a<b:
    a=a+1
    cant_num=0
    while a<b:
        r=a%2
        if r==0:
             cant_num=cant_num + 1
        a=a+1
    print("la cantidad de numeros pares es de =", cant_num)

else:
    print("a debe ser menor que b")