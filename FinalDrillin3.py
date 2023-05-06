#Funcion que modifica los nombres de los magos
def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = f"El gran {lista[i]}"
    return lista

#Funcion que imprime los elementos de la lista ingresada
def imprimir_nombres(lista):
    for i in lista:
        print(f"{i}")

#Lista original
listaNombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
#Hacemos una copia la cual será modificada
otros = listaNombres[:] #copiar lista con slice

#Creamos las listas magos y cientificos
magos = list()
cientificos = list()

#Llenamos las listas correspondientes a la vez que retiramos el elemento de la lista otros
for i in range(len(listaNombres)):
    if(listaNombres[i] in ["Harry Houdini","David Blaine","Teller"]):
        magos.append(otros.pop(otros.index(listaNombres[i])))
    elif(listaNombres[i] in ["Newton","Hawking","Einstein"]):
        cientificos.append(otros.pop(otros.index(listaNombres[i])))

#Imprimimos lo pedido
print("Todos los nombres:")
imprimir_nombres(listaNombres)
print("***********************")
print("Nombres de Magos:")
imprimir_nombres(magos)
print("***********************")
print("Nombres de Magos modificados:")
magos = hacer_grandioso(magos)
imprimir_nombres(magos)
print("***********************")
print("Nombres de Cientificos:")
imprimir_nombres(cientificos)
print("***********************")
print("Nombres restantes:")
imprimir_nombres(otros)
