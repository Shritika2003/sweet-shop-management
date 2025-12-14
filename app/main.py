from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, sweets, inventory

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sweet Shop Management System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# register routers
app.include_router(auth.router)
app.include_router(sweets.router)
app.include_router(inventory.router)
