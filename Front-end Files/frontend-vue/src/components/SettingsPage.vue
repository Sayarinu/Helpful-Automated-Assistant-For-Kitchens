<template>
  <NavBar />
  <div class="settings-page">
    <!-- HAAK Logo -->
    <img src=".\..\assets/HAAKLogo.png" alt="HAAK logo" class="logo" />
    <div class="sidebar">
      <aside class="bd-sidebar">
        <nav class="bd-links w-100">
        <ul class="bd-links-nav py-2 list-unstyled mb-0 pb-3 pb-md-2">
          <li>
                <router-link 
                  to="/settings/profile" 
                  class="list-group-item"
                  :class="{ active: selectedTab === 'profile' }"
                >
                  Profile
                </router-link>
          </li>
          <li>
            <router-link 
                to="/settings/account"
                class="list-group-item"
                :class="{ active: selectedTab === 'account' }"
              >
                Account
              </router-link>
          </li>
        </ul>
      </nav>
      </aside>

      <div class="tab-content">
        <div
          class="tab-pane"
          :class="{ active: selectedTab === 'profile' }"
          id="profile"
        >
          <ProfilePage/>
        </div>

        <div
          class="tab-pane"
          :class="{ active: selectedTab === 'account' }"
          id="account"
        >
          <AccountPage />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '../components/NavBar.vue';
import { useRouter } from 'vue-router';
import ProfilePage from "./ProfilePage.vue";
import AccountPage from "./AccountPage.vue";
export default {
  name: "SettingsPage",
  components: {
    ProfilePage,
    AccountPage,
    NavBar
  },
  data() {
    return {
    };
  },
  computed: {
    selectedTab() {
      const router = useRouter();
      return router.currentRoute.value.params.board;
    },
  },
  methods: {
    selectTab(tab) {
      this.selectedTab = tab;
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
  width: 80vw;
  margin: auto;
}
.logo {
  width: 20%;
}
.card {
  background: #272e48;
  border-radius: 5px;
  border: 0;
  margin-bottom: 1rem;
}
.list-group-item{
  background: unset;
  padding: 0.1875rem 0.5rem;
  margin-top: 0.125rem;
  
}
.card-body {
  color: #bcd0f7;
}
/* .row {
  padding-top: 0px;
  padding-bottom: 0px;
} */
.form-control {
  border: 1px solid #596280;
  border-radius: 2px;
  font-size: 0.825rem;
  background: #1a233a;
  color: #bcd0f7;
}
.btn {
  margin-left: 10px;
}
.sidebar {
  padding: 0 20px;
  position: relative;
  display: grid;
  grid-template-areas: "sidebar main";
  grid-template-columns: 1fr 8fr;
  gap: 16px;
}
.bd-sidebar{
  background: #272e48;
  border-radius: 5px;
  border: 0;
}
.list-group-item.active {
    background: #fff;
    color: #000000;
}
.bd-links-nav{
  padding: 0.5rem !important;
}
.sidebar .list-group {
  min-width: 100px;
  max-width: 100%;
  margin-right: 16px;
  /* position: absolute; */
  /* background: #596280; */
}
</style>