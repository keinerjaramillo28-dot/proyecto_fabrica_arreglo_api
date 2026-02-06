class base_datos_empleados:
    def __init__(self):
        # ARRAY
        self.db_empleado_lista = []

    def agregar_empleado(self, obj_empleado):
        self.db_empleado_lista.append(obj_empleado)
        return True
    
    def guardar_varios_empleados(self, varios_obj):
        self.db_empleado_lista.extend(varios_obj)

    def imprimir_info(self):
        for i in range(len(self.db_empleado_lista)):
            print(self.db_empleado_lista[i].ver_info_empleado())

            
    def insertar_empleados (self, posicion, obj_empleado):
        self.db_empleado_lista.insert(posicion, obj_empleado)
        return True
    
    def eliminar_ult_lista(self):
        self.db_empleado_lista.pop()
        return True
    
    def eliminar_empleado_por_posicion(self, posicion):
        self.db_empleado_lista.remove(self.db_empleado_lista[posicion])
        return True
    
    def obtener_nombre(self, empleado):
        return empleado.get_nombre_empleado()
    
    def sort_empleados(self):
        self.db_empleado_lista.sort(key=self.obtener_nombre)
        return True
  
    def reverse_empleados(self):
        self.db_empleado_lista.reverse()
        return True
