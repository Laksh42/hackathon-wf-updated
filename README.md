# Wells Fargo Financial Assistant

A modern financial assistant application built with React and FastAPI for Wells Fargo customers.

## Features

- Personalized financial recommendations
- AI-powered chat interface
- Authentication system
- Portfolio management
- Spending analysis

## Project Structure

```
.
├── app/                    # Backend FastAPI application
│   ├── api/                # API endpoints
│   ├── database/           # Database models and connection
│   ├── models/             # AI and data models
│   ├── utils/              # Utility functions
│   └── main.py             # Main entry point
└── frontend/               # React frontend
    ├── public/             # Static assets
    └── src/                # React source code
        ├── components/     # Reusable UI components
        ├── pages/          # Page components
        ├── services/       # API client services
        └── utils/          # Utility functions
```

## Getting Started

### Prerequisites

- Node.js (v16+)
- Python (v3.9+)
- MongoDB (or Docker for MongoDB container)

### Installation

1. Clone the repository
```bash
git clone https://github.com/Laksh42/hackathon-wf-updated.git
cd hackathon-wf-updated
```

2. Install backend dependencies
```bash
pip install -r requirements.txt
```

3. Install frontend dependencies
```bash
cd frontend
npm install
```

### Running the application

1. Start the backend server
```bash
cd app
python -m uvicorn main:app --reload
```

2. Start the frontend development server
```bash
cd frontend
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## Development

### Backend

The backend is built with FastAPI and provides the following endpoints:

- Authentication (`/api/auth/*`)
- Chat (`/api/chat/*`)
- Recommendations (`/api/recommendations/*`)

For development, you can use the mock data by enabling it in the configuration.

### Frontend

The frontend is built with React and Material-UI. The main configuration can be found in `frontend/src/config.js`.

For development, you can switch between using mock data or the real backend API by setting the `enableMockData` feature flag.

## License

This project is proprietary and confidential.

## Contact

For questions or support, please contact the development team.