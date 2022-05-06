class Numeros:
    __lista:[]
    def __init__(self):
        self.__lista=[]
    def agregar(self,n):
        if len(self.__lista) == 0:
            self.__lista.append(n)
        else:
            k = len(self.__lista)
            bandera= True
            for i in range(k):
                if self.__lista[i] == n:
                    bandera= False
            if bandera:
                self.__lista.append(n)
    def __str__(self):
        if self.getlen() == 0:
            cadena = "{}"
        else:
            cadena = "{"
            for unElemento in self.__lista:
                cadena += "{0}; ".format(unElemento)
            cadena = cadena[0:-2] + "}"
        return cadena
    def getlen(self):
        return (len(self.__lista))
    def quitar(self,n):
        if n in self.__lista:
            self.__lista.remove(n)
    def __add__(self, other):
        nueva=Numeros()
        for i in range(len(self.__lista)):
            n=self.__lista[i]
            nueva.agregar(n)
        for j in range(len(other.__lista)):
            n=other.__lista[j]
            nueva.agregar(n)
        return (nueva)
    def __sub__(self, other):
        nueva=Numeros()
        for i in range(len(self.__lista)):
                nueva.agregar(self.__lista[i])
        for j in range(len(other.__lista)):
                nueva.quitar(other.__lista[j])
        return nueva
    def __eq__(self, other):
        bandera=True
        if len(self.__lista) == len(other.__lista):
            i=0
            while i < len(self.__lista):
                j=0
                while j < len(other.__lista):
                    if self.__lista[i] != other.__lista[j]:
                       j = j+1
                       bandera=False
                    else:
                        i = i+1
                        bandera=True
                        j = len(other.__lista)
                if not bandera:
                    i= len(self.__lista)
        else:
            bandera=False
        return  bandera
