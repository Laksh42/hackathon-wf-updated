import logging
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.errors import ConnectionFailure
from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global database connection
db_client: AsyncIOMotorClient = None
db: AsyncIOMotorDatabase = None

async def connect_to_mongo() -> AsyncIOMotorDatabase:
    """
    Create a MongoDB connection pool and connect to the database.
    Returns the database instance.
    """
    global db_client, db
    try:
        # Create client using the connection string property
        connection_string = settings.MONGODB_CONNECTION_STRING
        logger.info(f"Connecting to MongoDB at {connection_string.split('@')[-1]}")
        
        # Set a shorter server selection timeout for faster startup
        db_client = AsyncIOMotorClient(connection_string, serverSelectionTimeoutMS=5000)
        
        # Get database
        db = db_client[settings.MONGODB_DB]
        
        # Test connection
        await db.command("ping")
        logger.info("Connected to MongoDB")
        
        # List collections to verify database is fully accessible
        collections = await db.list_collection_names()
        logger.info(f"Available collections: {', '.join(collections) if collections else 'None'}")
        
        if not collections:
            logger.warning("MongoDB database is empty - no collections found. Data may need to be imported.")
        
        # Check specific collections needed for financial data
        required_collections = ["account_data", "credit_history", "demographic_data", "investment_data", "transaction_data", "products"]
        missing_collections = [coll for coll in required_collections if coll not in collections]
        
        if missing_collections:
            logger.warning(f"Missing required collections: {', '.join(missing_collections)}")
            logger.warning("Some financial data may not be available")
        
        return db
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")
        # Return None instead of raising to allow app to start without DB
        db = None
        return None

async def close_mongo_connection():
    """Close MongoDB connection."""
    global db_client
    if db_client:
        db_client.close()
        logger.info("MongoDB connection closed")

async def get_database():
    """
    Get the database instance. Used as a dependency.
    """
    global db
    if db is None:
        await connect_to_mongo()
    return db 