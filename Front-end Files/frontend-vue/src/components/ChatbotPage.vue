<template>
  <div class="chat-page" :class="{ 'dark-mode': isDarkMode }">
    <NavBar :align-left="true" />
    <button @click="toggleDarkMode" class="dark-mode-btn">
      {{ isDarkMode ? 'Light Mode' : 'Dark Mode' }}
    </button>

    <!-- Full-page chat container -->
    <div class="full-page-chat-container">
      <div class="messages-body" ref="messageListContainer">
        <!-- Messages go here -->
        <!-- Inside your <div class="messages-body"> -->
        <div :key="index" v-for="(item, index) in messageList" class="message">
          <div v-if="item.userId === 0 && item.isRestaurant" class="restaurant-info">
            <div class="restaurant-details">
              <ul>
                <li><strong>Name:</strong> {{ item.restaurantData.name }}</li>
                <li><strong>Address:</strong> {{ item.restaurantData.address }}</li>
                <li><strong>Rating:</strong> {{ item.restaurantData.rating }}</li>
                <li><strong>Phone:</strong> {{ item.restaurantData.phone }}</li>
                <li><strong>URL:</strong> <a :href="item.restaurantData.url" target="_blank">Visit Website</a></li>
              </ul>
            </div>
            <img :src="item.restaurantData.imageUrl" alt="Restaurant Image" class="restaurant-image">
          </div>
          <div v-else-if="item.userId === 0" class="bot-message" v-html="item.message"></div>
          <div v-if="item.userId === 1" class="user-message" v-html="item.message"></div>
        </div>

        <div class="input-area">
          <!-- Reset button added next to send button -->
          <button class="btn reset-button" @click="resetChat">Reset</button>
          <textarea class="form-control" id="textAreaExample" rows="1" v-model="userMessage"
            placeholder="Type your message here..."></textarea>
          <button class="btn send-button" @click="sendMessage">Send</button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import NavBar from '../components/NavBar.vue';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';

export default {
  name: "ChatComponent",
  components: {
    NavBar
  },
  data() {
    return {
      userMessage: '',
      messageList: [],
      isDarkMode: false,
    };
  },
  created() {
    window.addEventListener('storage', this.syncDarkMode);
  },
  beforeUnmount() {
    window.removeEventListener('storage', this.syncDarkMode);
  },
  methods: {
    syncDarkMode(event) {
      if (event.key === 'darkMode') {
        this.isDarkMode = event.newValue === 'true';
      }
    },
    addRestaurantMessage(restaurantData) {
      this.messageList.push({
        userId: 0,
        username: 'bot',
        isRestaurant: true,
        restaurantData: {
          name: restaurantData.name,
          address: restaurantData.address,
          rating: restaurantData.rating,
          phone: restaurantData.phone,
          url: restaurantData.url,
          imageUrl: restaurantData.imageUrl // Make sure to include the image URL in the data you pass to this method
        }
      });
    },


    getSessionId() {
      let sessionId = localStorage.getItem('sessionId');
      if (!sessionId) {
        sessionId = uuidv4();
        localStorage.setItem('sessionId', sessionId);
      }
      return sessionId;
    },

    parseMessageForImages(message) {
      const urlRegex = /(https?:\/\/\S+\.(jpg|jpeg|png|gif))/g;
      const imageTags = message.match(urlRegex);
      if (imageTags) {
        imageTags.forEach((imgUrl) => {
          message = message.replace(imgUrl, `<img src="${imgUrl}" alt="Image" class="chat-image">`);
        });
      }

      message = message.replace(/\n/g, '<br>');
      return message;
    },


    async resetChat() {
      const sessionId = this.getSessionId();
      const token = localStorage.getItem('userToken'); // Retrieve stored token
      const headers = token ? { Authorization: `Bearer ${token}` } : {};

      try {
        await axios.post('http://localhost:8000/reset/', { session_id: sessionId }, { headers });
        this.messageList = []; // Clear the chat history
        localStorage.removeItem('chatMessages'); // Clear chat messages from localStorage

        this.fetchInitialMessage(); // Fetch the initial greeting message for the new chat session
      } catch (error) {
        console.error('Error resetting chat:', error);
      }
    },


    async sendMessage() {
      if (!this.userMessage.trim()) return;
      const userMessageProcessed = this.parseMessageForImages(this.userMessage);
      this.messageList.push({ userId: 1, username: 'user', message: userMessageProcessed });
      const sessionId = this.getSessionId();
      const token = localStorage.getItem('userToken');
      const headers = token ? { Authorization: `Bearer ${token}` } : {};
      try {
        const response = await axios.post('http://localhost:8000/chat/', {
          message: this.userMessage,
          session_id: sessionId
        }, { headers });
        const botMessageProcessed = this.parseMessageForImages(response.data.response);
        this.messageList.push({ userId: 0, username: 'bot', message: botMessageProcessed });
      } catch (error) {
        console.error(error);
        this.messageList.push({ userId: 0, username: 'bot', message: 'Sorry, I am having trouble responding right now.' });
      }
      this.userMessage = '';
      localStorage.setItem('chatMessages', JSON.stringify(this.messageList));
      this.scrollToBottom();
    },
    async fetchInitialMessage() {
      const sessionId = this.getSessionId();
      const token = localStorage.getItem('userToken'); // Retrieve stored token
      const headers = token ? { Authorization: `Bearer ${token}` } : {};

      try {
        const response = await axios.post('http://localhost:8000/chat/', {
          message: '',  // Empty message to trigger initial greeting
          session_id: sessionId
        }, { headers });

        this.messageList.push({ userId: 0, username: 'bot', message: response.data.response });
      } catch (error) {
        console.error('Error fetching initial message:', error);
      }
    },


    scrollToBottom() {
      this.$nextTick(() => {
        const container = this.$refs.messageListContainer;
        container.scrollTop = container.scrollHeight;
      });
    },

    watch: {
      messageList() {
        this.scrollToBottom(); // Scroll to bottom when messageList changes
      },
    },

    loadMessages() {
      const savedMessages = localStorage.getItem('chatMessages');
      if (savedMessages) {
        this.messageList = JSON.parse(savedMessages);
      }
    },
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      localStorage.setItem('darkMode', this.isDarkMode ? 'true' : 'false');
    },

  },
  updated() {
    this.scrollToBottom();
  },
  mounted() {
    const darkModePreference = localStorage.getItem('darkMode');
    this.isDarkMode = darkModePreference === 'true';
    const newSessionId = uuidv4();
    localStorage.setItem('sessionId', newSessionId);
    this.loadMessages();
    this.fetchInitialMessage();

  }
};
</script>

<style scoped>
.chat-page {
  background-color: #f8f9fa;
  /* Light background for light mode */
  color: #000;
  /* Black text for light mode */
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.full-page-chat-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  padding-bottom: 80px;
  /* Space for the input area */
}

.messages-body {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
  margin-bottom: 0;
  padding-bottom: 80px;
  /* Space at the bottom so content isn't hidden by the input area */
}

.input-area {
  position: fixed;
  /* Fixed at the bottom */
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 10px 20px;
  background-color: #fff;
  box-shadow: 0 -1px 10px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.form-control {
  flex-grow: 1;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.6;
  height: 50px;
  /* Larger input box */
}

.send-button,
.reset-button {
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  margin-left: 10px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: 1px solid #007bff;
}

.send-button:hover,
.reset-button:hover {
  background-color: #0069d9;
  border-color: #0062cc;
}

.dark-mode-btn {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 100;
  background-color: #444;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

/* Dark mode specific styles */
.dark-mode {
  background-color: #1a1a1a;
  color: #fff;
}

.dark-mode .messages-body {
  background-color: #333;
  color: #fff;
}

.dark-mode .input-area {
  background-color: #252525;
  color: #fff;
}

.dark-mode .form-control {
  background-color: #555;
  color: #fff;
  border-color: #444;
}

.dark-mode .send-button,
.dark-mode .reset-button {
  background-color: #0d6efd;
  border-color: #0a58ca;
}

/* Message styles */
.message {
  display: flex;
  justify-content: flex-start;
  /* Align to start by default */
  margin-bottom: 10px;
  /* Space between messages */
}

/* Bot message styles */
.bot-message {
  background-color: rgba(0, 123, 255, 0.1);
  /* Light blue background for bot messages */
  padding: 10px;
  border-radius: 10px;
  margin-right: auto;
  /* Push to the left side */
  max-width: 80%;
  /* Maximum width to avoid too wide messages */
}

/* User message styles */
.user-message {
  background-color: #007bff;
  /* Blue background for user messages */
  color: white;
  /* White text for visibility */
  padding: 10px;
  border-radius: 10px;
  margin-left: auto;
  /* Push to the right side */
  max-width: 80%;
  /* Maximum width to avoid too wide messages */
}

/* Dark mode message styles */
.dark-mode .bot-message {
  background-color: rgba(255, 255, 255, 0.1);
  /* Slightly lighter for dark mode */
}

.dark-mode .user-message {
  background-color: #0056b3;
  /* Darker blue for user messages in dark mode */
}

/* Styles to ensure visibility in both light and dark modes */
.dark-mode .messages-body {
  color: #fff;
}

.messages-body {
  color: #000;
}

.restaurant-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'Arial', sans-serif;
  /* Choose a font that suits your design */
}

.restaurant-info ul {
  padding: 0;
  list-style: none;
}

.restaurant-info li {
  margin-bottom: 0.5em;
}

.restaurant-info a {
  color: #007bff;
  text-decoration: none;
}

.restaurant-info a:hover {
  text-decoration: underline;
}

.restaurant-image {
  max-width: 100px;
  /* Adjust as necessary */
  height: auto;
  margin-left: 20px;
  /* Space between text and image */
}
</style>
