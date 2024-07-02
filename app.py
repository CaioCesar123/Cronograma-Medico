from flask import Flask, jsonify, make_response,redirect
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
import config
from models import Session,Usuario,Base,Paciente,Receita
from schemas.usuarioSchema import usuarioSchema,return_usuario,loginSchema,deleteSchema
from schemas.pacienteSchema import return_Paciente,createPaciente, findPacienteById,updatePaciente,getAll_Paciente,findListPacinete
from schemas.receitaSchema import createReceita,return_Receita,findReceitaById,findListReceita,updateReceita,getAll_Receita
from logger import logger

info = Info(title="Cronograma Medico", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.config.from_object(config)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Criação, visualização e remoção de usuários")
paciente_tag = Tag(name="Paciente", description="Criação, visualização e remoção de paciente")
receita_tag = Tag(name="Receita", description="Criação, visualização e remoção de receita")


@app.post('/usuairo/create', tags=[usuario_tag])
def create_user(form : usuarioSchema):
    session = Session()

    usuario_email = session.query(Usuario).filter(Usuario.usuario_login.ilike(form.email)).first()

    if(usuario_email):
        error_msg = "Não foi possível criar o usuário, o email já está em uso."
        logger.warning(error_msg)
        return {"message": error_msg}, 400
    
    usuario = Usuario(
        login=form.email,
        nome=form.nome,
        senha=form.senha
    )
    logger.debug(f"Adcionando usuario : '{usuario.usuario_nome}'")
    try:
        session.add(usuario)
        session.commit()
        logger.info(f"Usuario adcionado com sucesso : '{usuario.usuario_nome}'")
        return {"usuario" : return_usuario(usuario)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível criar o usuário, o email já está em uso."
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível criar o usuário"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.post('/usuairo/login', tags=[usuario_tag])
def login_user(form : loginSchema):
    session = Session()

    usuario = session.query(Usuario).filter(Usuario.usuario_login.ilike(form.email)).first()

    if(not usuario):
        error_msg = "Não foi possível localizar usuário."
        logger.warning(error_msg)
        return {"message": error_msg}, 400
    
    if(usuario.usuario_senha != form.senha):
        error_msg = "Senha ou email errada."
        logger.warning(error_msg)
        return {"message": error_msg}, 400

    try:
        logger.info(f"Login feito com sucesso : '{usuario.usuario_nome}'")
        return {"usuario" : return_usuario(usuario)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Hove algum erro durante o loggin."
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg =  "Hove algum erro durante o loggin."
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400

@app.delete('/usuairo/delete', tags=[usuario_tag])
def delete_user(form : deleteSchema):
    session = Session()

    usuario = session.query(Usuario).filter(Usuario.id == form.idUser).first()

    if(not usuario):
        response_data = {
            "message": "Usuario não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)

    try:
        session.delete(usuario)
        session.commit()
        response_data = {
            "message": "Usuario apagado com sucesso"
        }
        logger.info(response_data)
        return make_response(jsonify(response_data), 200)
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possivel apagar o usuario."
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possivel apagar o usuario."
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.post('/paciente/create', tags=[paciente_tag])
def create_Paciente(form : createPaciente):
    session = Session()

    paciente = Paciente(
        nome= form.nome,
        doenca= form.doenca,
        notas= form.notas,
        consulta_data= form.dataConsulta
    )

    usuario = session.query(Usuario).filter(Usuario.id==form.userID).first()

    if(not usuario):
        response_data = {
            "message": "Usuario não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)
    
    paciente.usuario = usuario
    logger.debug(f"Adcionando paciente : '{paciente.paciente_nome}'")

    try:
        session.add(paciente)
        session.commit()
        logger.info(f"Paciente adcionado : '{paciente.paciente_nome}'")
        return {"paciente" : return_Paciente(paciente)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível criar o paciente"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível criar o paciente"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.delete('/paciente/delete', tags=[paciente_tag])
def delete_paciente(form : findPacienteById):
    session = Session()

    paciente = session.query(Paciente).filter(Paciente.id == form.idPaciente).first()

    if(not paciente):
        response_data = {
            "message": "Paciente não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)

    try:
        session.delete(paciente)
        session.commit()
        response_data = {
            "message": "Paciente apagado com sucesso"
        }
        logger.info(response_data)
        return make_response(jsonify(response_data), 200)
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possivel apagar o Paciente."
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possivel apagar o Paciente."
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.put('/paciente/update', tags=[paciente_tag])
def update_Paciente(form: updatePaciente) :
    session = Session()
    paciente = session.query(Paciente).filter(Paciente.id==form.idPaciente).first()

    if(not paciente):
        response_data = {
            "message": "Paciente não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)
    
    if form.dataConsulta is not None :
        paciente.paciente_data_consulta = form.dataConsulta
    if form.nome is not None :
        paciente.paciente_nome = form.nome
    if form.doenca is not None :
        paciente.paciente_doenca = form.doenca
    if form.notes is not None :
        paciente.pacinete_note = form.notes

    try:
        session.commit()
        logger.info(f"Paciente atualizado : '{paciente.paciente_nome}'")
        return {"paciente" : return_Paciente(paciente)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível atualizar o paciente"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível atualizar o paciente"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.get('/paciente', tags=[paciente_tag])
def list_Paciente(query : findListPacinete):
    session = Session()
    pacinetes = session.query(Paciente).filter(Paciente.usuario_id==query.idUser)
    try:
        logger.info(f"Pacientes localizados com sucesso!")
        return jsonify(getAll_Paciente(pacinetes)),200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível pegar a lista de paciente"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível pegar a lista de paciente"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.post('/receita/create', tags=[receita_tag])
def create_Receita(form : createReceita):
    session = Session()

    receita = Receita(
        nome= form.remedio,
        data= form.data,
        horas= form.hora
    )

    paciente = session.query(Paciente).filter(Paciente.id==form.pacienteId).first()

    if(not paciente):
        response_data = {
            "message": "Paciente não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)
    
    receita.paciente = paciente

    try:
        session.add(receita)
        session.commit()
        logger.info(f"Nova receita : '{receita.receita_remedio}'")
        return {"receita" : return_Receita(receita)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível criar a receita"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível criar a receita"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.delete('/receita/delete', tags=[receita_tag])
def delete_receita(form : findReceitaById):
    session = Session()

    receita = session.query(Receita).filter(Receita.id == form.idReceita).first()

    if(not receita):
        response_data = {
            "message": "Receita não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)

    try:
        session.delete(receita)
        session.commit()
        response_data = {
            "message": "Receita apagado com sucesso"
        }
        logger.info(response_data)
        return make_response(jsonify(response_data), 200)
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possivel apagar a Receita."
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possivel apagar a Receita."
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.put('/receita/update', tags=[receita_tag])
def update_Receita(form: updateReceita) :
    session = Session()
    receita = session.query(Receita).filter(Receita.id==form.idReceita).first()

    if(not receita):
        response_data = {
            "message": "Receita não encontrado"
        }
        logger.warning(response_data)
        return make_response(jsonify(response_data), 400)
    
    if form.data is not None :
        receita.receita_data = form.data
    if form.remedio is not None :
        receita.receita_remedio = form.remedio
    if form.hora is not None :
        receita.receita_hora = form.hora

    try:
        session.commit()
        logger.info(f"Receita atualizada : '{receita.receita_remedio}'")
        return {"Receita" : return_Receita(receita)}, 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível atualizar a receita"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível atualizar a receita"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400
    
@app.get('/receita', tags=[receita_tag])
def list_Receita(query : findListReceita):
    session = Session()
    receitas = session.query(Receita).filter(Receita.paciente_id==query.idPaciente)
    try:
        logger.info(f"Receitas encontradas")
        return getAll_Receita(receitas), 200
    except IntegrityError:
        session.rollback()
        error_msg = "Não foi possível achar as receitas"
        logger.error(error_msg)
        return {"message": error_msg}, 400
    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível achar as receitas"
        logger.error(f"'{error_msg}' : '{str(e)}")
        return {"message": error_msg}, 400



@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

if __name__ == '__main__':
    app.run(debug=True)