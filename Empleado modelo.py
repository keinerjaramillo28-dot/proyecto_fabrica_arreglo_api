class Empleado_modelo: 
    def __init__(self, nombre, apellido, celular, cedula):
        self.cedula_empleado = cedula
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.celular_empleado = celular
        print("Empleado creado como objeto")

    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_nombre_empleado(self, nuevo_nombre):
        self.nombre_empleado = nuevo_nombre
    
    def ver_info_empleado(self):
        info_empleado = "nombre empleado= " + self.nombre_empleado + ", apellido empleado= " + self.apellido_empleado  + ", cedula empleado= " + self.cedula_empleado + ", celular empleado= " + self.celular_empleado
        return info_empleado
