from pydantic import BaseModel, Field
from models.receita import Receita
from datetime import datetime, time
from typing import Optional,List

class createReceita(BaseModel):
    remedio : str
    data : Optional[datetime] = datetime.now()
    hora : Optional[time] = datetime.now().time()
    pacienteId : int

class findReceitaById(BaseModel):
    idReceita : int

class findListReceita(BaseModel):
    idPaciente : int

class updateReceita(BaseModel):
    idReceita : int
    remedio : Optional[str] = Field(None)
    data : Optional[datetime] = Field(None)
    hora : Optional[time] = Field(None)

def return_Receita(receita : Receita):
    return {
        "id" : receita.id,
        "remedio" : receita.receita_remedio,
        "data" : receita.receita_data,
        "time" : receita.receita_hora.isoformat(),
        "idPaciente" : receita.paciente_id
    }

def getAll_Receita (receitas : List[Receita]):
    result = []
    for receita in receitas :
        result.append({
            "id" : receita.id,
            "remedio" : receita.receita_remedio,
            "data" : receita.receita_data,
            "hora" : receita.receita_hora.isoformat(),
            "idPaciente": receita.paciente_id
        })
    return {"receitas" : result}