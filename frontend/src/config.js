// Configuration for the Financial Advisor frontend application

const environment = process.env.NODE_ENV || 'development';

// Configuration for different environments
const envConfig = {
  development: {
    baseApiUrl: 'http://localhost:8000/api', // Use the actual backend service
    debug: true
  },
  production: {
    baseApiUrl: '/api',
    debug: false
  }
};

// Export the configuration
export const config = {
  // Base URL for API requests
  apiUrl: envConfig[environment].baseApiUrl,
  
  // Application settings
  app: {
    name: 'Wells Fargo Financial Assistant',
    version: '1.0.0',
    logoUrl: '/logo.png'
  },
  
  // Authentication settings
  auth: {
    tokenStorageKey: 'token',
    userStorageKey: 'currentUser',
    refreshTokenKey: 'refreshToken',
    expiryKey: 'tokenExpiry'
  },
  
  // Chat interface settings
  chat: {
    maxMessages: 10,
    typingIndicatorDelay: 1000,
    aiResponseDelay: 800,
    sessionStorageKey: 'chatSession',
    welcomeMessage: 'Welcome to the Wells Fargo Financial Assistant! I\'m here to help you with your financial goals.'
  },
  
  // API endpoints
  endpoints: {
    auth: {
      register: '/auth/register',
      login: '/auth/login',
      verify: '/auth/verify',
      me: '/auth/me',
      userData: '/auth/user-data'
    },
    recommendations: {
      list: '/recommendations',
      details: '/recommendations/:id'
    },
    chat: {
      send: '/chat/send',
      history: '/chat/history'
    }
  },
  
  // Recommendation settings
  recommendations: {
    max: 5,
    storageKey: 'financial_advisor_recommendations',
    refreshInterval: 24 * 60 * 60 * 1000 // 24 hours
  },
  
  // Feature flags
  features: {
    enableMockData: true, // Enable mock data since MongoDB is not set up
    enableDebug: envConfig[environment].debug
  },
  
  // Services (for component-specific integrations)
  services: {
    understander: {
      url: envConfig[environment].baseApiUrl
    }
  },
  
  // Debug settings
  debug: {
    logApiCalls: envConfig[environment].debug
  },
  
  // UI Configuration
  ui: {
    theme: {
      primary: '#D41B2C', // Wells Fargo red
      secondary: '#FFCD34', // Wells Fargo yellow
    },
    layout: {
      sidebarWidth: 240,
      headerHeight: 64
    }
  }
};