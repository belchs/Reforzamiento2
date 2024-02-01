
# 1
empleado = {"nombre": "Ana","edad": 30,"salario": 3000}
print("Mi primer diccionario tiene el siguiente contenido:{}".format(empleado))

# 2
lista_empleado = list(empleado)
print("Mi diccionario convertido en lista es :{}".format(lista_empleado))
"""tipo de variable empleado"""
print("El tipo de datos de mis datos convertidos en lista es {}".format(type(empleado)))


# 3
empleado["dni"] = "71415787"
print("Mi diccionario actualizado tiene los siguientes valores después de agregar dni:{}".format(empleado["dni"]))

print("Valor de salario:", empleado["salario"])

# 4
del empleado["edad"]
print("El diccionario actualizado después de eliminar edad es :{}".format(empleado))

# 5 Convertir tu diccionario a una lista
lista_empleado = list(empleado)
print("Mi diccionario convertido en lista es :{}".format(lista_empleado))
"""tipo de datos """
print("El tipo de datos de mis datos convertidos en lista es {}".format(type(empleado)))

# 6

# 7
departamentos = {
    'departamento1': 'Lima',
    'departamento2': 'Arequipa',
    'departamento3': 'Cusco',
    'departamento4': 'Piura',
    'departamento5': 'Junín',
    'departamento6': 'Tacna'
}
print("7. Diccionario de departamentos:", departamentos)

# Borrar cualquier departamento
del departamentos["departamento3"]
print(" El diccionario de departamentos después de borrar el dep3 es :{}".format(departamentos))



# 8
empleado["carrera"]="Ingeniería química"
print("Mi diccionario después de agregar mi carrera es:{}".format(empleado))
