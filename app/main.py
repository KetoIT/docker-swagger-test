from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth  # ���������, ��� ����� ������� ���������� ��������������
from app.database import init_db

app = FastAPI()

# ��������� CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ������������� ���� ������
@app.on_event("startup")
async def startup():
    await init_db()

# ���������� �����
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
