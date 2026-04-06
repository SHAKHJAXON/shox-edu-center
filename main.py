from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Sayt va API bir-biri bilan gaplashishi uchun ruxsat berish (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# O'quvchi ma'lumotlari modeli
class Student(BaseModel):
    name: str
    phone: str
    course: str

# Kurslar ro'yxati
COURSES = [
    {"id": 1, "name": "Ingliz tili (IELTS)", "price": "450,000 UZS", "duration": "6 oy", "icon": "🇬🇧"},
    {"id": 2, "name": "Matematika", "price": "350,000 UZS", "duration": "9 oy", "icon": "🔢"},
    {"id": 3, "name": "Web Dasturlash", "price": "600,000 UZS", "duration": "8 oy", "icon": "💻"},
    {"id": 4, "name": "Rus tili", "price": "300,000 UZS", "duration": "4 oy", "icon": "🇷🇺"},
]

@app.get("/courses")
def get_courses():
    return COURSES

@app.post("/register")
def register(student: Student):
    # Terminalda kelgan ma'lumotni ko'rsatadi
    print(f"Yangi ariza: {student.name} | Tel: {student.phone} | Kurs: {student.course}")
    return {"status": "success", "message": "Ro'yxatga olindi!"}