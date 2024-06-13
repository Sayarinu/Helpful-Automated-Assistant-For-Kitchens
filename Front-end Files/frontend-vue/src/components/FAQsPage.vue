<template>
    <div class="faq-page" style="background-color: #000;">
      <NavBar />
      <div class="container py-5">
        <div class="row d-flex justify-content-center">
          <div class="card-box col-md-8 col-lg-6 col-xl-4">
            <div class="card" style="border-radius: 15px; background-color: #333;"> <!-- Darker background for the card -->
              <div class="card-header d-flex justify-content-between align-items-center p-3" style="border-top-left-radius: 15px; border-top-right-radius: 15px; background-color: #222;"> <!-- Even darker header -->
                <p class="mb-0 fw-bold" style="color: #fff;">FAQs</p> <!-- Text color for visibility -->
              </div>
              <div class="card-body" style="color: #ddd;"> <!-- Light grey text for visibility -->
                <div v-for="(faq, index) in faqs" :key="index" class="faq mb-3">
                  <h5 class="faq-question">{{ faq.question }}</h5>
                  <p class="faq-answer">{{ faq.answer }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import NavBar from '../components/NavBar.vue';
  export default {
    name: "FAQPage",
    components: {
      NavBar
    },
    data() {
      return {
        faqs: [
        {
          question: "How do I start a chat with the chatbot?",
          answer: "Just type your message in the text area and hit send. The chatbot will respond to your query."
        },
        {
          question: "Can I reset the chat history?",
          answer: "Yes, there's a 'Reset Chat' button. Clicking it will clear your current chat history."
        },
        {
          question: "What kind of questions can I ask the chatbot?",
          answer: "You can ask about restaurant recommendations, locations, and other related queries."
        },
        {
          question: "Is my conversation with the chatbot private?",
          answer: "Yes, your privacy is important to us. Conversations are not shared with third parties."
        },
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .faq-page {
    background-color: #000;
    color: #fff;
    text-align: center;
  }
  
  .card-box {
    width: 50vw;
  }
  
  .faq-question {
    color: #57c0e7; /* Adjust if needed */
    margin-bottom: 0.5rem;
  }
  
  .faq-answer {
    color: #ddd; /* Light grey for better visibility */
    margin-bottom: 1rem;
  }
  </style>
  
