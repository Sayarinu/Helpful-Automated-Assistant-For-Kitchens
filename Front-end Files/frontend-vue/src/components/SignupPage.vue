<template>
  <div class="signup" style="background-color: black; height: auto;">
    <div class="image">
      <img src=".\..\assets\HAAKLogo.png" alt="HAAK logo">
    </div>
    <div class="mask d-flex align-items-center h-10000 gradient-custom-3" data-bs-theme="dark">
      <div class="container h-10000">
        <div class="row d-flex justify-content-center align-items-center h-10000">
          <div class="col-12 col-md-9 col-lg-7 col-xl-6">
            <div class="card" style="border-radius: 15px;">
              <div class="card-body p-5">
                <h2 class="text-center mb-5">Create an account</h2>

                <form>

                  <div class="form-outline mb-4">
                    <input type="text" id="firstName" class="form-control form-control-lg" />
                    <label class="form-label" for="firstName">First Name</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="text" id="lastName" class="form-control form-control-lg" />
                    <label class="form-label" for="lastName">Last Name</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="email" id="email" class="form-control form-control-lg" />
                    <label class="form-label" for="email">Your Email</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="password" id="password" class="form-control form-control-lg" />
                    <label class="form-label" for="password">Password</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="password" id="confirmPassword" class="form-control form-control-lg" />
                    <label class="form-label" for="confirmPassword">Repeat your password</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="tel" id="phoneNumber" class="form-control form-control-lg" />
                    <label class="form-label" for="phoneNumber">Phone Number (Optional)</label>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="text" id="location" class="form-control form-control-lg" />
                    <label class="form-label" for="location">Location (Optional)</label>
                  </div>

                  <div class="form-check d-flex justify-content-center mb-5">
                    <input class="form-check-input me-2" type="checkbox" value="" id="termsAgreed" />
                    <label class="form-check-label" for="termsAgreed">
                      I agree to all statements in the <a href="#!" class="text-body"><u>Terms of service</u></a>
                    </label>
                  </div>

                  <div class="d-flex justify-content-center">
                    <button type="button" class="btn btn-success btn-block btn-lg gradient-custom-4 text-body"
                      @click="registerUser">Register</button>
                  </div>
                  <br>

                  <div>
                    <button type="button" class="btn btn-primary btn-block btn-lg gradient-custom-4 text-body"
                      @click="continueAsGuest">Continue as Guest</button>

                  </div>

                  <p class="text-center text-muted mt-5 mb-0">Have already an account?
                    <router-link to="/login" class="fw-bold text-body"><u>Login here</u></router-link>
                  </p>

                </form>

              </div>
            </div>
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
    continueAsGuest() {
      this.$router.push('/chatbot');
    },
    registerUser() {
      const firstName = document.getElementById("firstName").value;
      const lastName = document.getElementById("lastName").value;
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirmPassword").value;
      const phoneNumber = document.getElementById("phoneNumber").value;
      const location = document.getElementById("location").value;
      const termsAgreed = document.getElementById("termsAgreed").checked;

      if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
      }

      if (!termsAgreed) {
        alert('You must agree to the terms of service to register.');
        return;
      }

      const registrationData = {
        first_name: firstName,
        last_name: lastName,
        email: email,
        password: password,
        // Only include phone number and location if they have been provided.
        ...(phoneNumber && { phone_number: phoneNumber }),
        ...(location && { location: location })
      };

      axios.post('http://127.0.0.1:8000/api/signup', registrationData)
        .then(response => {
          console.log(response.data);
          alert('Registered successfully. Please login.');
          this.$router.push('/login');
        })
        .catch(error => {
          console.error('There was an error!', error);
        });
    }
  }
};
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
}

.mask{
  background-color: black;
  height: 170vh;
}
</style>
