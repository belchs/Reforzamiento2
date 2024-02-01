
"""Reforzamiento 2"""
#1
cursos = ["Matemáticas", "Física", "Fisicoquímica", "Biología", "Inglés", "Qorganica"]
print("La lista de mis cursos en la universidad fueron:", cursos)

# 2
cursos.append("Seguridad")
cursos.append("Química")
cursos.append("Agroindustrias")
cursos.append("Estadística")
print("el resultado de mi nueva lista es : {}".format(cursos))

# 3
cursos.remove("Agroindustrias")
cursos.remove("Seguridad")
print("Mi nueva lista después de remover 2 cursos es:{}".format(cursos))

# 4
cursos.reverse()
print("Los datos de mi lista invertida es :{}".format(cursos))

# 5
cantidad_items = len(cursos)
print("La cantidad total de items en mi lista es :{}".format(cantidad_items))

# 6
cursos.insert(1, "Seguridad")
print("El valor de mi lista actualizada al agregar un curso más es :{}".format(cursos))

repeticiones= cursos.count("Seguridad")
print("Cantidad de veces que se repite 'Seguridad':", repeticiones)

# 7.
del cursos[0]
print("Los datos de mi lista actual después de borrar el primer item es :{}".format(cursos))

# 8.
lista_nueva = []
lista_nueva.append(3.1)
lista_nueva.append(3.2)
lista_nueva.append(3.3)
lista_nueva.append(10)
lista_nueva.append(20)
lista_nueva.append(30)
lista_nueva.append("hola")
lista_nueva.append("mundo")
lista_nueva.append("lema")
print("Mi nueva lista contiene lo siguiente :{}".format(lista_nueva))

# 9
suma_listas = cursos + lista_nueva
print("La suma total de mis dos listas cursos y lista_nueva es :{}".format(suma_listas))

# 10
lista_desordenada = [10, 8, 6, 4, 2, 1]
lista_desordenada.sort()
print("Mi lista ordenada es :{}".format(lista_desordenada))

# 11
lista_2 = [3.14, True, 5.67, False, 8.9, True]
print("Penúltimo valor:", lista_2[-2])
print("Último valor:", lista_2[-1])
print("Penúltimo valor:", lista_2[-2],lista_2[-1])


# 12
tipos_elementos = [type(elemento) for elemento in lista_2]
print("Tipos de datos en la lista:", tipos_elementos)


# 13.
lista_2.clear()
print("Mi lista después de eliminar todos los elementos de  lista2:", lista_2)

# 14
lista_desordenada.pop(1)
lista_desordenada.pop(3)
print("Mi lista después de eliminar elementos por índices:", lista_desordenada)

# 15
lista_enteros = list(range(1, 101))
print("Mi ista con los 100 primeros enteros:", lista_enteros)

# 16
datos_entre_10_y_35 = lista_enteros[10:34]
print("Los datos entre la posición 10 y 35:", datos_entre_10_y_35)






