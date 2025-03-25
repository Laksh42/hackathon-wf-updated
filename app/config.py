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
    
    # CORS settings
    ALLOWED_ORIGINS: str = clean_env_var("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000")
    CORS_ORIGINS: List[str] = get_list_env("CORS_ORIGINS", ["http://localhost:3000"])
    
    # Feature flags
    ENABLE_IMAGE_ANALYSIS: bool = get_bool_env("ENABLE_IMAGE_ANALYSIS", True)
    ENABLE_RECOMMENDATIONS: bool = get_bool_env("ENABLE_RECOMMENDATIONS", True)
    ENABLE_RLHF: bool = get_bool_env("ENABLE_RLHF", False)
    ENABLE_SENTIMENT_ANALYSIS: bool = get_bool_env("ENABLE_SENTIMENT_ANALYSIS", True)
    ENABLE_ADAPTIVE_RECOMMENDATIONS: bool = get_bool_env("ENABLE_ADAPTIVE_RECOMMENDATIONS", True)
    ENABLE_MOCK_DATA: bool = get_bool_env("ENABLE_MOCK_DATA", True)  # Enable mock data by default

settings = Settings() 