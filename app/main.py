import logging
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from app.database.mongodb import connect_to_mongo, close_mongo_connection
from app.config import settings
import os

# Import API routers
from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.recommendations import router as recommendations_router

# Configure logging
logging.basicConfig(
    level=logging.INFO if not settings.DEBUG else logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Multi-Modal Financial Advisor Chatbot API",
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Register startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the Financial Advisor API")
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the Financial Advisor API")
    await close_mongo_connection()

# Include API routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(chat_router, prefix="/api/chat", tags=["Chat"])
app.include_router(recommendations_router, prefix="/api/recommendations", tags=["Recommendations"])

# Simple chat endpoint for testing
@app.post("/api/chat/send")
async def send_chat_message(request: Request):
    try:
        data = await request.json()
        message = data.get("message", "")
        session_id = data.get("session_id")
        
        response_text = f"You said: {message}"
        if "invest" in message.lower():
            response_text = "Based on your profile, I recommend considering our diversified index funds."
        elif "saving" in message.lower():
            response_text = "Our high-yield savings account offers 2.15% APY, which is ideal for emergency funds."
        
        return {
            "text": response_text,
            "session_id": session_id or "test-session-id",
            "state": {"is_complete": False}
        }
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok", "app_name": settings.APP_NAME, "version": settings.APP_VERSION}

# Root route redirects to documentation or static home page
@app.get("/")
async def root():
    return {"message": "Welcome to the Financial Advisor API", "docs_url": "/api/docs"}

# Run the application if this file is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)