from Clase import  Numeros

def lista1():
    listA=Numeros()
    k=float(input('ingrese los numeros enteros de la lista 1,finalice con -1 \n'))
    while (k != -1):
        listA.agregar(int(k))
        k=float(input())
    return listA
def lista2():
    listB=Numeros()
    k=float(input('ingrese los numeros enteros de la lista 2,finalice con -1 \n'))
    while (k != -1):
        listB.agregar(int(k))
        k=float(input())
    return listB
if __name__ == '__main__':
    A=lista1()
    B=lista2()
    print('La union de ambas listas es: ')
    print(A+B)
    print ('La resta de la lista 1 con la lista 2 es: ')
    print(A-B)
    if A==B:
        print('los conjuntos son iguales')
    else:
        print('los conjuntos son diferentes')
