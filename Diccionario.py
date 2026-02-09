class datos_diccionario:
  def _init_(self):
    self.datos_diccionario = {"1090400171": {"nombre": "betulio","apellido":"escobar","maquina":("maquina1",maquina2","maquina3")}}
  def longitud_diccionario(self):
    longitud = len(self.datos_diccionario)
    return longitud
  def limpiar_diccionario(self):
    limpiar = self.datos_diccionario.clear()
    self.datos_diccionario = limpiar
  def copiar_diccionario(self):
    copiar = self.datos_diccionario.copy()
    self.copiar_diccionario = copiar
  def sacar_elemento(self):
    sacar = self.datos_diccionario.valunes()
    return sacar
  def devolver_llaves(self):
    devolver = self.datos_diccionario.keys()
    return devolver 
  def sacar_valores(self):
     dato_valores = self.datos_diccionario.valunes()
     return dato_valores
  def eliminar_info(self):
    eliminar = self. datos_diccionario.pop("1090401071")
     return eliminar
  def eliminar_elemento(self):
     eliminar = self.datos_diccionario.popitem()
     return eliminar
  def actualizar_info(self,nuevo_diccionario):
     actualizar = self.datos_diccionario.update(nuevo_diccionario)
     return actualizar
  def imprimir_info(self):
    for clave in self.datos_diccionario.keys():
    print(f"dato info: {self.dato_diccionario[clave]}")
  

    
    
