from datos import base_datos_empleados
from modelo import Empleado_modelo


# creo la base de datos de empleados
obj_bd_Empleado_lista = base_datos_empleados()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("keiner", "jaramillo", "1098759434", "98733784521")
obj_empleado2 = Empleado_modelo("alejandra", "sarmiento", "9246843645", "9858965923")


# llamo el metodo de la base de datos que guarda al objeto
#creo una lista para guardar masivamente

lista_nuevos_modelos = [obj_empleado, obj_empleado2]

obj_bd_Empleado_lista.agregar_empleado(obj_empleado) # guardar un obj
obj_bd_Empleado_lista.agregar_empleado(obj_empleado2)



#Imprimo toda la lista de empleados
obj_bd_Empleado_lista.imprimir_info()
