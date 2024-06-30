from pydantic import BaseModel, validator
from models.usuario import Usuario

class usuarioSchema(BaseModel):
    email : str
    nome : str
    senha : str

    @validator('email','nome','senha', pre=True)
    def convert_str(cls, value):
        if not isinstance(value,str):
            return str(value)
        return value

class loginSchema(BaseModel):
    email : str
    senha : str

    @validator('email','senha', pre=True)
    def convert_str(cls, value):
        if not isinstance(value,str):
            return str(value)
        return value

class deleteSchema(BaseModel):
    idUser : str

def return_usuario(usuario : Usuario):
    return {
        "id" : usuario.id,
        "email" : usuario.usuario_login,
        "nome" : usuario.usuario_nome
    }