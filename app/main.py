from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.simplify import router as simplify_router

app = FastAPI(title="Rafiq MVP Backend")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
    "https://rafiq-frontend-rouge.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_origin(request, call_next):
    print("METHOD:", request.method, "PATH:", request.url.path, "ORIGIN:", request.headers.get("origin"))
    response = await call_next(request)
    return response

app.include_router(simplify_router)

@app.get("/")
def root():
    return {"message": "Rafiq backend is running"}