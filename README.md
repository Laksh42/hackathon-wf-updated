# Wells Fargo Financial Advisor Dashboard

A React-based frontend application with a FastAPI backend that provides personalized financial recommendations and an AI assistant chatbot to help users with their financial goals.

## Features

- 🔒 **User Authentication**: Secure login and registration system
- 📊 **Financial Dashboard**: View personalized financial recommendations
- 💬 **AI Chatbot**: Get instant financial advice through a conversational interface
- 📱 **Responsive Design**: Mobile-friendly interface using Material UI

## Tech Stack

### Frontend
- React with Material UI
- React Router for navigation
- Axios for API requests
- Context API for state management

### Backend
- FastAPI with Python
- MongoDB for data storage (with in-memory mock data fallback)
- JWT authentication
- Python 3.8+

## Quick Start

### Prerequisites
- Node.js and npm
- Python 3.8+
- MongoDB (optional - system supports mock data mode)

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/Laksh42/hackathon-wf-updated.git
   cd hackathon-wf-updated
   ```

2. Create a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```
   python -m app.main
   ```
   
   The backend will be available at http://localhost:8000/api

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install frontend dependencies:
   ```
   npm install
   ```

3. Start the frontend development server:
   ```
   npm start
   ```

   The frontend will be available at http://localhost:3000

## Configuration

### Backend Configuration

The backend can be configured through environment variables in a `.env` file:

```
# Application settings
APP_NAME="Multi-Modal Financial Advisor Chatbot"
APP_VERSION="0.1.0"
DEBUG=True
PORT=8000

# Security
SECRET_KEY=your-secret-key
JWT_SECRET=your-jwt-secret-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# MongoDB configuration
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB=financial_advisor
ENABLE_MOCK_DATA=True  # Set to True to use mock data if MongoDB is unavailable
```

### Frontend Configuration

The frontend configuration is managed in `frontend/src/config.js`. Key settings include:

- API endpoints 
- Feature flags (enableMockData)
- UI theme settings
- Authentication storage keys

## Development Mode

The application supports a development mode with mock data:

1. In the frontend, set `enableMockData: true` in `frontend/src/config.js`
2. In the backend, set `ENABLE_MOCK_DATA=True` in your environment or `.env` file

This allows you to develop and test without requiring a real MongoDB database.

## License

MIT

## Contact

For any questions or feedback, please contact the project maintainers.