from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column("usuario_pk", Integer, primary_key=True)
    usuario_nome = Column(String(100))
    usuario_login = Column(String(100), unique=True, nullable=False)
    usuario_senha = Column(String(255), nullable=False)

    pacientes = relationship('Paciente', back_populates='usuario')

    def __init__(self, nome: str, login: str, senha: str):
        self.usuario_nome = nome
        self.usuario_login = login
        self.usuario_senha = senha