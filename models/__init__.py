from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from .base import Base
from .usuario import Usuario
from .receita import Receita
from .paciente import Paciente

project_dir = "database/"

if not os.path.exists(project_dir):
    os.mkdir(project_dir)

db_path = os.path.join(project_dir, 'db.sqlite3')

db_url = f'sqlite:///{db_path}'

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url) :
    create_database(engine.url)

Base.metadata.create_all(bind=engine)