from fastapi import APIRouter
from dotenv import load_dotenv
from config.db_connector import engine
from sqlalchemy.exc import SQLAlchemyError 
from models.table import FilesTable
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
import os
import logging
import time


api = APIRouter()
load_dotenv()


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.post("/upload", tags=["Upload File"])
async def upload(file_name: str):
    try :
        session = Session(bind=engine)
        add_file =FilesTable(name=file_name)
        session.add(add_file)
        session.commit()
        return {'message':'success'}
    except SQLAlchemyError as e:
        print('\n')
        print('There is an error ==> ',e)
        print('\n')
    finally:
        session.close()

@api.delete('/delete', tags=['Upload File'])
async def delete(uuid: str):
    try :
        session = Session(bind=engine)
        delete_file = session.query(FilesTable).filter(FilesTable.uuid == uuid).first()
        print(delete_file)
        session.delete(delete_file)
        session.commit()
        return {'message':'success'}
    except SQLAlchemyError as e:
        print('\n')
        print('There is an error ==> ',e)
        print('\n')
    finally:
        session.close()
        
@api.get('/get', tags=['Upload File'])
async def get(file_name: str):
    try :
        session = Session(bind=engine)
        get_file = session.query(FilesTable).filter(FilesTable.name == file_name).first()
        return get_file
    except SQLAlchemyError as e:
        print('\n')
        print('There is an error ==> ',e)
        print('\n')
    finally:
        session.close()

@api.get('/stream', tags=['Stream'])
async def steaming():
    logger = logging.getLogger(__name__)
    # music_file_path = "./vivalavida_lofi.mp3"
    current_folder = os.path.dirname(os.path.abspath(__file__))
    # Membangun path ke file musik dari path file codingan
    music_file_path = os.path.join(current_folder, 'vivalavida_lofi.mp3')
    if not os.path.isfile(music_file_path):
        raise HTTPException(status_code=404, detail="File not found")
    def generate():
        with open(music_file_path, "rb") as file:
            while chunk := file.read(1024):
                logger.info("Streaming music: %s", music_file_path)
                time.sleep(1)
                yield chunk
    
    return StreamingResponse(generate(), media_type="audio/mp3")