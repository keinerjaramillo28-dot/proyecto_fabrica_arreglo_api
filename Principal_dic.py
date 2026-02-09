from dicccionario in datos_diccionario
obj_diccionario = datos_diccionario()
info = obj_diccionario.sacar_valores()
print (info)

nuevo_diccionario = {"1090401289":{"nombrr":"roberto","apellido":"sanchez","maquina":("maquina pintura","maquina hidraulica")}}

obj_diccionario.actualizar_info(nuevo_diccionario)
obj_diccionario.imprimir_info()
