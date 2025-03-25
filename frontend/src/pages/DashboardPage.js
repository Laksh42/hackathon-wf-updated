import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Grid, 
  Paper, 
  Typography, 
  Button, 
  Box,
  Card,
  CardContent,
  CardHeader,
  Divider,
  List,
  ListItem,
  ListItemText,
  CircularProgress
} from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';
import { getRecommendations } from '../api';
import ChatWidget from '../components/ChatWidget';

const DashboardPage = () => {
  const theme = useTheme();
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [chatOpen, setChatOpen] = useState(false);
  
  // Sample data for the portfolio chart
  const portfolioData = [
    { name: 'Stocks', value: 45 },
    { name: 'Bonds', value: 30 },
    { name: 'Cash', value: 15 },
    { name: 'Other', value: 10 },
  ];
  
  const COLORS = [theme.palette.primary.main, theme.palette.secondary.main, theme.palette.success.main, theme.palette.warning.main];
  
  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const data = await getRecommendations();
        setRecommendations(data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
        setLoading(false);
      }
    };
    
    fetchRecommendations();
  }, []);
  
  const toggleChat = () => {
    setChatOpen(!chatOpen);
  };
  
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Grid container spacing={3}>
        {/* Welcome Card */}
        <Grid item xs={12}>
          <Paper sx={{ p: 3, display: 'flex', flexDirection: 'column' }}>
            <Typography variant="h4" component="h1" gutterBottom>
              Welcome back, John!
            </Typography>
            <Typography variant="body1">
              Here's an overview of your financial health and personalized recommendations.
            </Typography>
          </Paper>
        </Grid>
        
        {/* Portfolio Summary */}
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: 300 }}>
            <Typography variant="h6" gutterBottom component="div">
              Portfolio Summary
            </Typography>
            <Divider />
            <Box sx={{ height: '100%', width: '100%', display: 'flex', alignItems: 'center' }}>
              <Grid container>
                <Grid item xs={12} md={6}>
                  <ResponsiveContainer width="100%" height={200}>
                    <PieChart>
                      <Pie
                        data={portfolioData}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        outerRadius={80}
                        fill="#8884d8"
                        dataKey="value"
                      >
                        {portfolioData.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                      </Pie>
                    </PieChart>
                  </ResponsiveContainer>
                </Grid>
                <Grid item xs={12} md={6}>
                  <List>
                    {portfolioData.map((item, index) => (
                      <ListItem key={item.name}>
                        <Box
                          sx={{
                            width: 16,
                            height: 16,
                            bgcolor: COLORS[index % COLORS.length],
                            mr: 1
                          }}
                        />
                        <ListItemText
                          primary={`${item.name}: ${item.value}%`}
                        />
                      </ListItem>
                    ))}
                  </List>
                </Grid>
              </Grid>
            </Box>
          </Paper>
        </Grid>
        
        {/* Account Summary */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: 300 }}>
            <Typography variant="h6" gutterBottom component="div">
              Account Summary
            </Typography>
            <Divider />
            <CardContent>
              <Typography variant="h4" component="div" gutterBottom>
                $125,430.00
              </Typography>
              <Typography color="text.secondary" gutterBottom>
                Total Balance
              </Typography>
              
              <Box sx={{ mt: 2 }}>
                <Typography variant="body2" gutterBottom>
                  Checking: $12,250.00
                </Typography>
                <Typography variant="body2" gutterBottom>
                  Savings: $35,680.00
                </Typography>
                <Typography variant="body2" gutterBottom>
                  Investment: $77,500.00
                </Typography>
              </Box>
            </CardContent>
          </Paper>
        </Grid>
        
        {/* Recommendations */}
        <Grid item xs={12}>
          <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
            <Typography variant="h6" gutterBottom component="div">
              Personalized Recommendations
            </Typography>
            <Divider />
            <Box sx={{ mt: 2 }}>
              {loading ? (
                <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
                  <CircularProgress />
                </Box>
              ) : (
                <Grid container spacing={2}>
                  {recommendations.map((rec, index) => (
                    <Grid item xs={12} sm={6} md={4} key={index}>
                      <Card>
                        <CardHeader
                          title={rec.title}
                          subheader={rec.category}
                        />
                        <CardContent>
                          <Typography variant="body2">
                            {rec.description}
                          </Typography>
                        </CardContent>
                      </Card>
                    </Grid>
                  ))}
                </Grid>
              )}
            </Box>
          </Paper>
        </Grid>
      </Grid>
      
      {/* Chat Widget */}
      <Box
        sx={{
          position: 'fixed',
          bottom: '20px',
          right: '20px',
          zIndex: 1000
        }}
      >
        <Button
          variant="contained"
          color="primary"
          onClick={toggleChat}
          sx={{ borderRadius: '50%', width: 64, height: 64 }}
        >
          {chatOpen ? 'X' : 'Chat'}
        </Button>
      </Box>
      
      {chatOpen && <ChatWidget onClose={toggleChat} />}
    </Container>
  );
};

export default DashboardPage;