from sqlalchemy import Column, Integer, String, DateTime,ForeignKey,Time
from sqlalchemy.orm import relationship
from datetime import datetime, time
from typing import Union

from .base import Base

class Receita(Base):
    __tablename__ = 'receitas'
    id = Column("pk_receita",Integer, primary_key=True)
    receita_remedio = Column(String(200))
    receita_data = Column(DateTime)
    receita_hora = Column(Time)

    paciente_id = Column(Integer, ForeignKey('pacientes.paciente_pk'))
    paciente = relationship('Paciente', back_populates='receitas')

    def __init__(self, nome : str,horas: Union[time, None] = None ,data : Union[DateTime, None] = None):
        self.receita_remedio = nome
        if data:
            self.receita_data = data
        if horas:
            self.receita_hora = horas