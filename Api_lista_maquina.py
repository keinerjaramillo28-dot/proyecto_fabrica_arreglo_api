class api_db_maquinas:
  def _init_(self):
    self.api_maquina = [
      ["codigo","nombre maquina","modelo maquina","estado maquina"],
      ["code 2801","brazo mecanico","x100","apagada"],
      ["code 1124","cinta transportadora","zx300","requiere mantenimiento"],
      ["code 1283","monobrazo","jk100","encendida"],
    ]

def imprimir_info(self):
  for i in range(len(self.api_maquina)):
    print(self.api_maquina[i])

def duscar_info(self):
  return self.api_maquina[0][1]
  
