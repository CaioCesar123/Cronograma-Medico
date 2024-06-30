from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from typing import Union
from datetime import datetime

from .base import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column("paciente_pk", Integer, primary_key=True)
    paciente_nome = Column(String(100))
    paciente_data_consulta = Column(DateTime)
    paciente_doenca = Column(String(150))
    pacinete_note = Column(String(5000))

    receitas = relationship('Receita', back_populates='paciente')

    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_pk"))
    usuario = relationship('Usuario', back_populates='pacientes')

    def __init__(self, nome: str, notas: str, doenca: str, consulta_data: Union[DateTime, None] = None):
        self.paciente_nome = nome
        self.pacinete_note = notas
        self.paciente_doenca = doenca
        if consulta_data:
            self.paciente_data_consulta = consulta_data