const axios = require('axios');

// Configuration
const CONFIG = {
  ENDPOINT_URL: 'https://4f0e-79-155-84-44.eu.ngrok.io',
  SLACK_URL: '<YOUR_SLACK_WEBHOOK_URL>',
  THRESHOLD_UNAUTHORIZED: 10,
  USERNAME: 'user1',
  PASSWORD: 'pass1'
};

// Function to send Slack notification
const sendSlackMessage = async (message) => {
  try {
    await axios.post(CONFIG.SLACK_URL, { text: message });
    console.log('Slack notification sent.');
  } catch (error) {
    console.error('Error sending Slack notification:', error);
  }
};

// Function to monitor the API endpoint
const monitorEndpoint = async () => {
  try {
    const response = await axios.get(CONFIG.ENDPOINT_URL, {
      auth: {
        username: CONFIG.USERNAME,
        password: CONFIG.PASSWORD
      }
    });

    if (response.status !== 200) {
      const errorMessage = `Website is unavailable. Status code: ${response.status}`;
      await sendSlackMessage(errorMessage);
    }

    if (response.status === 401) {
      const unauthorizedCount = response.data.filter((status) => status === 'Unauthorized').length;

      if (unauthorizedCount >= CONFIG.THRESHOLD_UNAUTHORIZED) {
        const unauthorizedMessage = `A large number of 'Unauthorized' statuses detected: ${unauthorizedCount}`;
        await sendSlackMessage(unauthorizedMessage);
      }
    }
  } catch (error) {
    console.error('Error monitoring the endpoint:', error);
  }
};

// Start monitoring the endpoint
monitorEndpoint();
