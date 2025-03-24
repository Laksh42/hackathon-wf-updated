from typing import Optional, Any, Union, List
import os
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Clean environment variables with comments
def clean_env_var(var_name, default=None):
    val = os.getenv(var_name, default)
    if val and isinstance(val, str):
        # Remove any trailing comments (assuming comments start with #)
        val = val.split('#')[0].strip()
    return val

def get_int_env(var_name, default=0):
    """Get an integer environment variable, handling comment issues"""
    val = clean_env_var(var_name, str(default))
    try:
        # Extract just the first number part and convert to int
        match = re.search(r'^\d+', val)
        if match:
            return int(match.group(0))
        return int(val)
    except (ValueError, TypeError):
        return default

def get_bool_env(var_name, default=False):
    """Get a boolean environment variable, handling various formats"""
    val = clean_env_var(var_name, str(default)).lower()
    return val in ("true", "1", "t", "yes", "y")

def get_list_env(var_name, default=None, separator=","):
    """Get a list environment variable by splitting a string"""
    if default is None:
        default = []
    val = clean_env_var(var_name)
    if not val:
        return default
    return [item.strip() for item in val.split(separator)]

class Settings:
    # Application settings
    APP_NAME: str = clean_env_var("APP_NAME", "Multi-Modal Financial Advisor Chatbot")
    APP_VERSION: str = clean_env_var("APP_VERSION", "0.1.0")
    DEBUG: bool = get_bool_env("DEBUG", False)
    HOST: str = clean_env_var("HOST", "0.0.0.0")
    PORT: int = get_int_env("PORT", 8000)

    # Security
    SECRET_KEY: str = clean_env_var("SECRET_KEY", "your-secret-key")
    JWT_SECRET: str = clean_env_var("JWT_SECRET", "your-jwt-secret-here")
    JWT_ALGORITHM: str = clean_env_var("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = get_int_env("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    # MongoDB configuration - use simpler URL for local development
    MONGODB_URL: str = clean_env_var("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DB: str = clean_env_var("MONGODB_DB", "financial_advisor")
    # Only use credentials if they are actually set and not default placeholders
    MONGODB_USER: str = clean_env_var("MONGODB_USER", "")
    MONGODB_PASSWORD: str = clean_env_var("MONGODB_PASSWORD", "")
    
    # MongoDB connection string builder
    @property
    def MONGODB_CONNECTION_STRING(self) -> str:
        """Build MongoDB connection string with or without credentials based on env vars."""
        if self.MONGODB_USER and self.MONGODB_PASSWORD and self.MONGODB_USER != "your_mongodb_user":
            # If credentials are provided and not defaults, use them
            auth_part = f"{self.MONGODB_USER}:{self.MONGODB_PASSWORD}@"
            url_parts = self.MONGODB_URL.split("://")
            if len(url_parts) > 1:
                return f"{url_parts[0]}://{auth_part}{url_parts[1]}"
            return f"mongodb://{auth_part}localhost:27017"
        # Otherwise return the URL as is
        return self.MONGODB_URL
    
    # Redis configuration
    REDIS_URL: str = clean_env_var("REDIS_URL", "redis://localhost:6379")
    REDIS_DB: int = get_int_env("REDIS_DB", 0)
    REDIS_PASSWORD: Optional[str] = clean_env_var("REDIS_PASSWORD")
    
    # API Keys
    OPENAI_API_KEY: Optional[str] = clean_env_var("OPENAI_API_KEY")
    HUGGINGFACE_TOKEN: Optional[str] = clean_env_var("HUGGINGFACE_TOKEN")
    MISTRAL_API_KEY: Optional[str] = clean_env_var("MISTRAL_API_KEY")
    
    # CORS settings
    ALLOWED_ORIGINS: str = clean_env_var("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000")
    CORS_ORIGINS: List[str] = get_list_env("CORS_ORIGINS", ["http://localhost:3000"])
    
    # Model configurations
    DEFAULT_MODEL: str = clean_env_var("DEFAULT_MODEL", "mistralai/Mistral-7B-v0.1")
    CHAT_MODEL: str = clean_env_var("CHAT_MODEL", "mistralai/Mistral-7B-v0.1")
    EMBEDDING_MODEL: str = clean_env_var("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    OPENAI_VISION_MODEL: str = clean_env_var("OPENAI_VISION_MODEL", "gpt-4-vision-preview")
    
    # LLM Service configurations
    LLM_MODEL: str = clean_env_var("LLM_MODEL", "gpt-3.5-turbo") 
    LLM_API_URL: str = clean_env_var("LLM_API_URL", "https://api.openai.com/v1/chat/completions")
    LLM_MAX_TOKENS: int = get_int_env("LLM_MAX_TOKENS", 1000)
    LLM_TEMPERATURE: float = float(clean_env_var("LLM_TEMPERATURE", "0.7"))
    
    # File storage paths
    UPLOAD_DIR: str = clean_env_var("UPLOAD_DIR", "uploads")
    TEMP_DIR: str = clean_env_var("TEMP_DIR", "temp")
    DATA_DIR: str = clean_env_var("DATA_DIR", "./data")
    PRODUCTS_FILE: str = clean_env_var("PRODUCTS_FILE", "./data/products.csv")
    MAX_UPLOAD_SIZE: int = get_int_env("MAX_UPLOAD_SIZE", 10485760)

    # Cache Settings
    # 1 hour in seconds
    CACHE_TTL: int = get_int_env("CACHE_TTL", 3600)
    # 24 hours in seconds
    CONVERSATION_HISTORY_TTL: int = get_int_env("CONVERSATION_HISTORY_TTL", 86400)

    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = get_int_env("RATE_LIMIT_REQUESTS", 100)
    # 1 hour in seconds
    RATE_LIMIT_PERIOD: int = get_int_env("RATE_LIMIT_PERIOD", 3600)

    # Logging
    LOG_LEVEL: str = clean_env_var("LOG_LEVEL", "INFO")
    LOG_FILE: str = clean_env_var("LOG_FILE", "app.log")

    # Feature flags
    ENABLE_IMAGE_ANALYSIS: bool = get_bool_env("ENABLE_IMAGE_ANALYSIS", True)
    ENABLE_RECOMMENDATIONS: bool = get_bool_env("ENABLE_RECOMMENDATIONS", True)
    ENABLE_RLHF: bool = get_bool_env("ENABLE_RLHF", False)
    ENABLE_SENTIMENT_ANALYSIS: bool = get_bool_env("ENABLE_SENTIMENT_ANALYSIS", True)
    ENABLE_ADAPTIVE_RECOMMENDATIONS: bool = get_bool_env("ENABLE_ADAPTIVE_RECOMMENDATIONS", True)

settings = Settings() 