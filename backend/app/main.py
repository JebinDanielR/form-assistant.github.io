from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import extract, ask, submit, sessions

app = FastAPI(
    title="Gov Form Assistant API",
    description="AI-powered government form filling assistant",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(extract.router, prefix="/api/extract", tags=["Extract"])
app.include_router(ask.router,     prefix="/api/ask",     tags=["Ask"])
app.include_router(submit.router,  prefix="/api/submit",  tags=["Submit"])
app.include_router(sessions.router,prefix="/api/sessions",tags=["Sessions"])

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/", tags=["Health"])
def root():
    return {"message": "Gov Form Assistant API is running"}