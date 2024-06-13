// router.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../components/LoginPage.vue';
import ChatbotPage from '../components/ChatbotPage.vue';
import SettingsPage from '../components/SettingsPage.vue';
import SignupPage from '../components/SignupPage.vue';
import MainPage from '../components/MainPage.vue';
import AboutPage from '../components/AboutPage.vue';
import FAQsPage from '../components/FAQsPage.vue';
import FeaturesPage from '../components/FeaturesPage.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/main_page' },
    { path: '/features', component: FeaturesPage },
    { path: '/login', component: LoginPage },
    { path: '/chatbot', component: ChatbotPage },
    { path: '/settings/:board', component: SettingsPage },
    { path: '/about', component: AboutPage },
    { path: '/FAQs', component: FAQsPage },
    { path: '/signup', component: SignupPage},
    { path: '/main_page', component: MainPage},
    { path: '/:catchAll(.*)', redirect: "/main_page"},
    { path: '/faqs', component: FAQsPage}
  ],
});

export default router;
