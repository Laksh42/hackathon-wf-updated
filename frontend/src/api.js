import axios from 'axios';
import { config } from './config';
import mockApi from './mockApi';

// Configure axios
axios.defaults.baseURL = config.apiUrl;

// Setup response interceptor for error handling
axios.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error);
    return Promise.reject(error);
  }
);

// Create an API wrapper that uses either the real API or mockApi
const api = {
  // Auth functions
  auth: {
    login: async (username, password) => {
      if (config.features.enableMockData) {
        return mockApi.login(username, password);
      }
      
      const response = await axios.post(config.endpoints.auth.login, { username, password });
      return response.data;
    },
    
    register: async (username, password) => {
      if (config.features.enableMockData) {
        return mockApi.register(username, password);
      }
      
      const response = await axios.post(config.endpoints.auth.register, { username, password });
      return response.data;
    },
    
    getUserData: async () => {
      if (config.features.enableMockData) {
        return mockApi.getUserData('testuser');
      }
      
      const response = await axios.get(config.endpoints.auth.me);
      return response.data;
    }
  },
  
  // Recommendations functions
  recommendations: {
    getRecommendations: async () => {
      if (config.features.enableMockData) {
        return mockApi.getRecommendations();
      }
      
      const response = await axios.get(config.endpoints.recommendations.list);
      return response.data;
    },
    
    refreshRecommendations: async () => {
      if (config.features.enableMockData) {
        return mockApi.refreshRecommendations();
      }
      
      const response = await axios.post(config.endpoints.recommendations.refresh);
      return response.data;
    },
    
    provideFeedback: async (recommendationId, isRelevant) => {
      if (config.features.enableMockData) {
        return mockApi.provideFeedback(recommendationId, isRelevant);
      }
      
      const response = await axios.post(config.endpoints.recommendations.feedback, {
        recommendation_id: recommendationId,
        is_relevant: isRelevant
      });
      return response.data;
    }
  },
  
  // Chat functions
  chat: {
    sendMessage: async (message, sessionId = null) => {
      if (config.features.enableMockData) {
        return mockApi.sendChatMessage(message, sessionId);
      }
      
      const response = await axios.post(config.endpoints.chat.send, {
        message,
        session_id: sessionId
      });
      return response.data;
    },
    
    getConversations: async () => {
      if (config.features.enableMockData) {
        return [];
      }
      
      const response = await axios.get(config.endpoints.chat.conversations);
      return response.data;
    }
  }
};

// Set auth token for axios if it exists in localStorage
const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default api;