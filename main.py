
#fastapi 가져오기 
from fastapi import FastAPI
#정적파일 서버에 올리기 
from fastapi.staticfiles import StaticFiles
# 데이터 타입의 유효성 검사 
from pydantic import BaseModel


app = FastAPI()


#서버 띄우기 
# uvicorn main:app --reload
app.mount("/", StaticFiles(directory="static", html= True), name="static")



