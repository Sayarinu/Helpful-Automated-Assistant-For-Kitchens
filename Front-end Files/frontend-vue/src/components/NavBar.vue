<template>
  <nav class="navbar navbar-expand-lg navbar-dark" :class="{ 'align-left': alignLeft }">
    <div class="container">

      <!-- Navbar buttons -->
      <div class="navbar-collapse" id="navbarNav">
        <ul class="navbar-nav"> 
          <li class="nav-item">
            <router-link to="/chatbot" :class="active.startsWith('/chatbot')?'nav-link active':'nav-link'">Chatbot</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/settings/profile" :class="active.startsWith('/settings') ?'nav-link active':'nav-link'">Settings</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/faqs" :class="active.startsWith('/faqs') ?'nav-link active':'nav-link'">FAQs</router-link>
          </li>

        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'NavBar',
  props: {
    alignLeft: Boolean,
  },
  computed: {
    active() {
      const router = useRouter();
      return router.currentRoute.value.path
    },
  },
}
</script>

<style scoped>
.navbar {
  background-color: #262a2e;
}

/* Removed justify-content to allow items to align to the left */
.navbar > .container {
  display: flex;
}

.align-left > .container {
  justify-content: flex-start;
}

/* Ensure navbar-collapse aligns to the left without any additional spacing */
.navbar-collapse {
  flex-grow: 0; /* Changed from unset to 0 to avoid taking unnecessary space */
  padding-left: 0; /* Ensure no padding on the left */
  margin-left: 0; /* Ensure no margin on the left */
}

.navbar-nav .nav-link {
  color: #ffffff;
}

.navbar-nav .nav-link.active {
  background-color: #0c53be;
  border-radius: 0.375rem;
}

.nav-link {
  margin-right: 15px; /* Add margin between buttons */
}

/* Your existing styles can remain unchanged */
</style>
