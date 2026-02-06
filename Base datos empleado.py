from base_Datos_empleados import base_datos_empleados
from Empleado_modelo import Empleado_modelo


# creo la base de datos de empleados
obj_bd_Empleado_lista = base_datos_empleados()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("Juan", "Perez", "123456789", "987654321")
obj_empleado2 = Empleado_modelo("Maria", "Gomez", "987654321", "123456789")


# llamo el metodo de la base de datos que guarda al objeto
#creo una lista para guardar masivamente

lista_nuevos_modelos = [obj_empleado, obj_empleado2]

obj_bd_Empleado_lista.agregar_empleado(obj_empleado) # guardar un obj
obj_bd_Empleado_lista.agregar_empleado(obj_empleado2)



#Imprimo toda la lista de empleados
obj_bd_Empleado_lista.imprimir_info()
