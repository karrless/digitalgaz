from fastapi import FastAPI, File, HTTPException, UploadFile
import io
import aiofiles as aiof

from digitalgaz.config import IMG_PATH

app = FastAPI()

@app.post("/")
async def get_flow_value(file: UploadFile = File(...)):
    """
    Обработка пост запроса на получение значения расхода с датчика на фото
    
    """
    if file.content_type.startswith('image'):
        raise HTTPException(status_code=400, detail="File is not a valid image.")
    
    file_path = IMG_PATH+file.filename
    async with aiof.open(file_path, mode='wb') as f:
        content = await file.read()
        await f.write(content)

    return {"value":file.filename}

@app.get("/")
async def index():
    
    return {"message":"Hello from ООСД!"}