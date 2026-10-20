from fastapi import APIRouter
from .. services.estudiante_servicio import EstudianteServicio
from .. schemas.estudiante import Estudiante

router = APIRouter(prefix='/estudiantes', tags=['estudiantes'])
EstudianteServicio= EstudianteServicio()

@router.post('/')
def  guardar (estudianteNuevo:Estudiante):
    return EstudianteServicio.guardar(estudianteNuevo=estudianteNuevo)
@router.post('/')


def  mostrar ():
    pass

def  actualizar ():
    pass

def  guardar ():
    pass