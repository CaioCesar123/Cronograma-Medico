from pydantic import BaseModel
from models.usuario import Usuario

class usuarioSchema(BaseModel):
    email : str
    nome : str
    senha : str

class loginSchema(BaseModel):
    email : str
    senha : str

class deleteSchema(BaseModel):
    idUser : str

def return_usuario(usuario : Usuario):
    return {
        "id" : usuario.id,
        "email" : usuario.usuario_login,
        "nome" : usuario.usuario_nome
    }