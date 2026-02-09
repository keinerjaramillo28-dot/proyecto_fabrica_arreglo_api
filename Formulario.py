import tkinter as ventana
def enviar_info():
  print("datos enviados a la base de datos")
  
formulario = ventana.tk()
formulario.title("registro de maquina")
codigo_maquina = ventana.label(formulario,text="codigo maquina")
codigo_maquina.pack()
texto_codigo = ventana.entry(formulario)
texto_codigo.pack()
nombre_maquina = ventana.label(formulario,text="cual es el nombre de la maquina: ")
nombre_maquina.pack()
texto_nombre = ventana.entry(formulario)
texto_nombre.pack()
modelo_maquina = ventana.label(formulario,text="modelo maquina:")
modelo_maquina.pack()
texto_modelo = ventana.entry(formulario)
texto_modelo.pack()
estado_maquina = ventana.label(formulario,text="estado maquina;")
estado_maquina.pack()
texto_estado = ventana.entry(formulario)
texto_estado.pack()
boton_maquina = ventana.button(formulario,text="guardar maquina",command=enviar_info)
boton_maquina.pack()



formulario.mainloop()




