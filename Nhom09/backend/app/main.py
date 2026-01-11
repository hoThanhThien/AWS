from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from app.controllers import (
    booking_controller, user_controller, tour_controller, payment_controller, 
    category_controller, discount_controller, photo_controller, 
    role_controller, support_controller,
    auth_controller, comment_controller, websocket_controller, momo_controller,
    admin_controller
)
from fastapi.staticfiles import StaticFiles
from app.controllers import upload_controller

app = FastAPI(title="Tour Booking API", version="1.0.0")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# CORS middleware
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://hothanhthien.io.vn",
        "http://localhost:5173",
        "http://localhost:3000",
	"http://13.55.40.240",
        "http://13.55.40.240:3000",
        "http://13.55.40.240:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include routers
app.include_router(auth_controller.router)
app.include_router(admin_controller.router)
app.include_router(booking_controller.router)
app.include_router(user_controller.router)
app.include_router(tour_controller.router)
app.include_router(comment_controller.router)
app.include_router(payment_controller.router)
app.include_router(category_controller.router)
app.include_router(discount_controller.router)
app.include_router(photo_controller.router)
app.include_router(role_controller.router)
app.include_router(support_controller.router)
app.include_router(websocket_controller.router)
app.include_router(upload_controller.router)
app.include_router(momo_controller.router)

@app.get("/")
async def root():
    return {"message": "Tour Booking API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/health")
async def api_health():
    return {"status": "ok"}
