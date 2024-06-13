
<template >
    <div class="image">
    <img src=".\..\assets/HAAKLogo.png" alt="HAAK logo">
    </div>
    <div class="container py-3 h-500" data-bs-theme="dark">
      <div class="row d-flex justify-content-center align-items-center h-50">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card shadow-2-strong" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">
  
              <h3 class="mb-5">Sign in</h3>
  
              <div class="form-outline mb-4">
                <input type="email" id="typeEmailX-2" class="form-control form-control-lg" />
                <label class="form-label" for="typeEmailX-2">Email</label>
              </div>
  
              <div class="form-outline mb-4">
                <input type="password" id="typePasswordX-2" class="form-control form-control-lg" />
                <label class="form-label" for="typePasswordX-2">Password</label>
              </div>
  
              <!-- Checkbox -->
              <div class="form-check d-flex justify-content-start mb-4">
                <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                <label class="form-check-label" for="form1Example3"> Remember Password </label>
              </div>
  
              <button class="btn btn-primary btn-lg btn-block" @click="login" type="button">Login</button>
  
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  methods: {
    login() {
      const email = document.getElementById("typeEmailX-2").value;
      const password = document.getElementById("typePasswordX-2").value;

      axios.post('http://127.0.0.1:8000/api/login', {
        email: email,
        password: password
      })
      .then(response => {
        if (response.data.access_token) {
          // Store the JWT token in local storage
          localStorage.setItem('userToken', response.data.access_token);
          alert('Logged in successfully');
          this.$router.push('/chatbot');
        } else {
          alert('Login failed');
        }
      })
      .catch(error => {
        console.error('There was an error during the login process:', error);
        alert('There was an error during the login process.');
      });
    }
  }
}
</script>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 25%;
}

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
}

</style>