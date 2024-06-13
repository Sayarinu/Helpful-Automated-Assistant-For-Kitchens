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
              <h6 class="mb-3 text-primary">Personal Details</h6>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label class = "card-info" for="firstName">First Name</label>
                <input v-if = "edit" type="text" v-model="userFirstName" :readonly="isReadonly()" class="form-control" id="firstName" placeholder="Enter first name">
                <p v-else>{{ userFirstName }}</p>

              </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label class = "card-info" for="lastName">Last Name</label>
                <input v-if = "edit" type="text" v-model="userLastName" :readonly="isReadonly()" class="form-control" id="lastName" placeholder="Enter last name">
                <p v-else>{{ userLastName }}</p>
              </div>
            </div>

            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label class = "card-info" for="phone">Phone</label>
                <input v-if = "edit" type="text" v-model="userPhone" :readonly="isReadonly()" class="form-control" id="phone" placeholder="Enter phone number">
                <p v-else>{{ userPhone }}</p>
              </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label class = "card-info" for="location">Location</label>
                <input v-if = "edit" type="text" v-model="userLocation" :readonly="isReadonly()" class="form-control" id="location" placeholder="Enter location">
                <p v-else>{{ userLocation }}</p>
              </div>
            </div>
          </div>
          <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
              <div class="text-right">
                <button v-if="!isReadonly()" type="button" id="cancel" name="cancel" class="btn btn-secondary" @click="cancelEdit">Cancel</button>
                <button v-if="!isReadonly()" type="button" id="submit" name="submit" class="btn btn-primary" @click="updateUserData">Update</button>
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
  name: "ProfilePage",
  data() {
    return {
      edit: false,
      userFirstName: '',
      userLastName: '',
      userEmail: '',
      userPhone: '',
      userLocation: '',
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    isReadonly() {
      return !this.edit;
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    fetchUserData() {
      // Replace with actual API endpoint
        axios.get('http://127.0.0.1:8000/api/user_data', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('userToken')}` // Assuming the token is stored in localStorage
          }
        })
        .then(response => {
          this.userFirstName = response.data.first_name;
          this.userLastName = response.data.last_name;
          this.userEmail = response.data.email;
          this.userPhone = response.data.phone;
          this.userLocation = response.data.location;

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
    updateUserData() {
      const updateData = {
        first_name: this.userFirstName,
        last_name: this.userLastName,
        email: this.userEmail,
        phone: this.userPhone,
        location: this.userLocation
      };
        axios.put('http://127.0.0.1:8000/api/update_user_data', updateData, {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('userToken')}` // Assuming the token is stored in localStorage
          }
        })
        .then(response => {
          console.log(response.data);
          alert('User data updated');
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
  .settings-page {
    background-color: #000000;
    color: #bcd0f7;
    padding-top: 20px;
    text-align: center;
  }
  
  .logo {
    width: 20%;
  }
  
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

  .tab-pane >.row{
    padding-top: 0;
    padding-bottom: 0;
  }
  
  .form-control {
    border: 1px solid #596280;
    border-radius: 2px;
    font-size: 0.825rem;
    background: #1A233A;
    color: #bcd0f7;
  }

  .edit-button{
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
  
