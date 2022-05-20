a=int(input("Dame el valor de a: "))
b=int(input("Dame el valor de b: "))

if a<b:
    a=a+1
    cant_num=1
    while a<b:
        a=a+1
        cant_num=cant_num+1
    print("la cantidad de numeros que hay es de =", cant_num)