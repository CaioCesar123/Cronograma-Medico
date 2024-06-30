from pydantic import BaseModel, Field,validator
from models.paciente import Paciente
from datetime import datetime
from typing import Optional,List

class createPaciente(BaseModel):
    nome : str
    dataConsulta : Optional[datetime] = datetime.now()
    doenca : Optional[str]
    notas : Optional[str] = ""
    userID : int

    @validator('nome','doenca','notas', pre=True)
    def convert_str(cls, value):
        if not isinstance(value,str):
            return str(value)
        return value

class findPacienteById(BaseModel):
    idPaciente : int

class findListPacinete(BaseModel):
    idUser : int

class updatePaciente(BaseModel):
    idPaciente : int
    nome : Optional[str] = Field(None)
    dataConsulta : Optional[datetime] = Field(None)
    doenca : Optional[str] = Field(None)
    notes : Optional[str] = Field(None)

    @validator('nome','doenca','notes', pre=True)
    def convert_str(cls, value):
        if not isinstance(value,str):
            return str(value)
        return value

def return_Paciente(paciente : Paciente):
    return {
        "id" : paciente.id,
        "nome" : paciente.paciente_nome,
        "notas" : paciente.pacinete_note,
        "data" : paciente.paciente_data_consulta,
        "doenca" : paciente.paciente_doenca,
        "userID": paciente.usuario_id
    }

def getAll_Paciente (pacientes : List[Paciente]):
    result = []
    for paciente in pacientes :
        result.append({
            "id" : paciente.id,
            "nome" : paciente.paciente_nome,
            "notas" : paciente.pacinete_note,
            "data" : paciente.paciente_data_consulta,
            "doenca" : paciente.paciente_doenca,
        })
    return {"pacientes" : result}