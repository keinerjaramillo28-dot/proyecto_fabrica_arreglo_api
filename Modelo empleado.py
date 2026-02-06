from base_Datos_empleados import base_datos_empleados
from Empleado_modelo import Empleado_modelo


# creo la base de datos de empleados
obj_bd_Empleado_lista = base_datos_empleados()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("carlos", "garcia", "9293884390", "1739294990")
obj_empleado2 = Empleado_modelo("aleja", "sarmiento", "1639274839", "1538299449")
obj_empleado3 = Empleado_modelo("fernando", "martinez", "2649394748", "3274839903")
obj_empleado4 = Empleado_modelo("emmanuel", "Muñoz", "27382948478", "1648294947")
obj_empleado5 = Empleado_modelo("alonso", "jaramillo", "2748294849", "2748393758") 
obj_empleado6 = Empleado_modelo("sofia", "sanchez", "2748394859", "38475738399")


# llamo el metodo de la base de datos que guarda al objeto
#creo una lista para guardar masivamente

lista_nuevos_modelos = [obj_empleado, obj_empleado2, obj_empleado3, obj_empleado4, obj_empleado5, obj_empleado6]

# guardar varios empleados a la vez
obj_bd_Empleado_lista.guardar_varios_empleados(lista_nuevos_modelos) 

# inserta el empleado en la posicion que escojas
obj_bd_Empleado_lista.insertar_empleados(3, obj_empleado)  

# elimina el último empleado de la lista
obj_bd_Empleado_lista.eliminar_ult_lista()  

# elimina el empleado en la posición que indiques 
obj_bd_Empleado_lista.eliminar_empleado_por_posicion(5)  

print("\n--- Lista Despues de las eliminaciones ---")
obj_bd_Empleado_lista.imprimir_info()

# ordena la lista por nombre del empleado alfabéticamente
print("\n--- Lista ordenada por nombre (sort) ---")
obj_bd_Empleado_lista.sort_empleados()  
obj_bd_Empleado_lista.imprimir_info()

# invierte el orden de la lista de empleados
print("\n--- Lista invertida (reverse) ---")
obj_bd_Empleado_lista.reverse_empleados()  
obj_bd_Empleado_lista.imprimir_info()
