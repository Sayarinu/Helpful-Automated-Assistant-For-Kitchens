<template>
  <div class="row gutters">
    <!-- Left Column -->
    <div class="col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12">
      <div class="card h-100">
        <div class="card-body">
          <div class="account-settings">
            <div class="user-profile">
              <h5 class="user-name">{{ userFirstName }} {{ userLastName }}</h5>
              <h6 class="user-email">{{ userEmail }}</h6>
              <h6 class="user-phone">{{ userPhone }}</h6>
            </div>

          </div>
        </div>
      </div>
    </div>

    <!-- Right Column -->
    <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12" card-block>
      <div class="card h-100">
        <div class="card-body">
          <div class='edit-button' @click="toggleEdit">
            {{ edit? 'Cancel Edit': 'Edit' }}
          </div>
          <div class="row gutters">

            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
              <h6 class="mb-3 text-primary">Account Details</h6>
            </div>

            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label for="email" class = "card-info">Email</label>
                <input v-if = "edit" type="email" v-model="userEmail" :readonly="isReadonly()" class="form-control" id="email" placeholder="Enter Email">
                <p v-else>{{ userEmail }}</p>

              </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label for="password" class = "card-info">Password</label>
                <input v-if = "edit" type="password" v-model="userPassword" :readonly="isReadonly()" class="form-control" id="password" placeholder="Enter Password">
                <p v-else></p>

              </div>
            </div>

          </div>
          <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
              <div class="text-right">
                <button v-if="!isReadonly()" type="button" id="submit" name="submit" class="btn btn-secondary" @click="cancelEdit">Cancel</button>
                <button v-if="!isReadonly()" type="button" id="submit" name="submit" class="btn btn-primary" @click="updateCredentials">Update</button>
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
  name: "AccountPage",
  data() {
    return {
      edit: false,
      userFirstName: '',
      userLastName: '',
      userEmail: '',
      userPhone: '',
      userPassword: '',
    };
  },
  mounted() {
    this.fetchAccountData();
  },
  methods: {
    isReadonly() {
      return !this.edit;
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    fetchAccountData() {
      // Replace with actual API endpoint
        axios.get('http://127.0.0.1:8000/api/user_data', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('userToken')}`
          }
        })
        .then(response => {
          this.userEmail = response.data.email;
          this.userFirstName = response.data.first_name;
          this.userLastName = response.data.last_name;
          this.userPhone = response.data.phone;

         this.originalUserData = {
          first_name: response.data.first_name,
          last_name: response.data.last_name,
          email: response.data.email,
          phone: response.data.phone,
          location: response.data.location
        };
        })
        .catch(error => console.error('Error', error));
    },
    updateCredentials() {
      const updateData = {
        email: this.userEmail,
        password: this.userPassword,
      };
        axios.put('http://127.0.0.1:8000/api/update_credentials', updateData, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('userToken')}` // Assuming the token is stored in localStorage
          }
        })
        .then(response => {
          console.log(response.data);
          alert('Credentials updated');
          this.toggleEdit();
        })
        .catch(error => {
          console.error('Error', error);
        });
    },
        cancelEdit() {
            this.edit = false;

            // Reset data to original values
            this.userFirstName = this.originalUserData.first_name;
            this.userLastName = this.originalUserData.last_name;
            this.userEmail = this.originalUserData.email;
            this.userPhone = this.originalUserData.phone;
            this.userLocation = this.originalUserData.location;
          },
  },
};
</script>



<style scoped>
  .card {
    background: #272E48;
    border-radius: 5px;
    border: 0;
    margin-bottom: 1rem;
  }

  .card-body {
    color: #bcd0f7;
  }

  .row {
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .form-control {
    border: 1px solid #596280;
    border-radius: 2px;
    font-size: 0.825rem;
    background: #1A233A;
    color: #bcd0f7;
  }

  .edit-button {
    position: absolute;
    right: 16px;
    cursor: pointer;
    color: #0d6efd;
  }

  .btn {
    margin-left: 10px;
  }
    .user-avatar img {
    border-radius: 50%;
  }
  .user-name{
    padding-top: 30px;
  }
  .about {
    padding-top: 30px;
  }
  .card-block {
    text-align: left;
  }

  .card-info {
    padding-top: 10px;
    padding-bottom: 5px;
  }
  .form-group p{
    color:rgb(163, 163, 163);
  }
</style>
