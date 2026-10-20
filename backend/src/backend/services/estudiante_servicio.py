from ..schemas.estudiante import Estudiante
class EstudianteServicio:

    def __init__(self):
        self.listaEstudiante: list[Estudiante]=[0]

    def guardar (self , estudianteNuevo: Estudiante):
        self.listaEstudiante.append(estudianteNuevo)
        return estudianteNuevo
        
    def mostrar (self):
        return self.listaEstudiante
       
    def actualizar (self, id :int , estudiante: Estudiante):
        for _, valor in enumerate (self.listaEstudiante):
             if valor.id== id :
                  valor.nombre = estudiante.nombre
                  valor.edad = estudiante.edad
                  valor.correo= estudiante.correo
                  
        return valor
        
    def eliminar (self):
            pass