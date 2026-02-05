class base_datos_empleados:
    def _init_(self):
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
        

    def guardar_varios_empleados(self, varios_obj):
        # Inserta los objetos uno a uno usando insert.
        # Si no se especifica una posición, se insertan al final preservando el orden.
        index = len(self.db_empleado_lista)
        for obj in varios_obj:
            self.db_empleado_lista.insert(index, obj)
            index += 1

    def extender_empleados(self, varios_obj):
        # Extiende la lista con múltiples objetos usando extend.
        # Es más eficiente que insert cuando no se necesita una posición específica.
        self.db_empleado_lista.extend(varios_obj)
        return True