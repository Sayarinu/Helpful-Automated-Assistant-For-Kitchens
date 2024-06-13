<template>
  <div class="chat-page" style="background-color: #000;">
    <!-- Logo outside the chatbot -->
    <img src="@/assets/ChatbotLogo.png" alt="Chatbot logo" class="logo" />

    <div class="container py-5">
      <div class="row d-flex justify-content-center">
        <div class="col-md-8 col-lg-6 col-xl-4">
          <div class="card" id="chat1" style="border-radius: 15px;">
            <div class="card-header d-flex justify-content-between align-items-center p-3 bg-info text-white border-bottom-0" style="border-top-left-radius: 15px; border-top-right-radius: 15px;">
              <i class="fas fa-angle-left"></i>
              <p class="mb-0 fw-bold">Live chat</p>
              <i class="fas fa-times"></i>
            </div>
            <div class="card-body">
              <!-- Chat messages -->
              <div class="d-flex flex-row justify-content-start mb-4">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;" />
                <div class="p-3 ms-3" style="border-radius: 15px; background-color: rgba(57, 192, 237,.2);">
                  <p class="small mb-0">Hello and thank you for visiting MDBootstrap. Please click the video below.</p>
                </div>
              </div>

              <div class="d-flex flex-row justify-content-end mb-4">
                <div class="p-3 me-3 border" style="border-radius: 15px; background-color: #fbfbfb;">
                  <p class="small mb-0">Thank you, I really like your product.</p>
                </div>
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava2-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;" />
              </div>

              <!-- User input and send button -->
              <div class="form-outline">
                <textarea class="form-control" id="textAreaExample" rows="4" v-model="userMessage"></textarea>
                <label class="form-label" for="textAreaExample">Type your message</label>
              </div>

              <button class="btn btn-primary mt-3" @click="sendMessage">Send</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { sendRequest } from "@/path-to-your-sendRequest-file"; // Replace with the actual path

export default {
  name: "ChatComponent",
  data() {
    return {
      userMessage: '',
    };
  },
  methods: {
    sendMessage() {
      // Call the sendRequest function with userMessage
      sendRequest(this.userMessage);

      // Clear the input field
      this.userMessage = "";
    },
  },
};
</script>

<style scoped>
.chat-page {
  background-color: #000;
  color: #fff;
  text-align: center;
  height: 100vh;
}

.logo {
  width: 20%;
}

/* Add your additional styling as needed */
</style>
