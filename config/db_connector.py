import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models.table import Base


load_dotenv()

db_host = os.environ.get('DBHOST')
db_name = os.environ.get('DBNAME')
db_user = os.environ.get('DBUSER')
db_password = os.environ.get('DBPASSWORD')
db_port = os.environ.get('DBPORT')
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_url)
Base.metadata.create_all(engine)