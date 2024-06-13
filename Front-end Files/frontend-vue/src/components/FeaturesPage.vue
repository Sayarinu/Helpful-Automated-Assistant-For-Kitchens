<template>
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
        <header class="mb-auto">
            <div>
                <h3 class="float-md-start mb-0">HAAK</h3>
                <nav class="nav nav-masthead justify-content-center float-md-end">
                    <router-link class="nav-link fw-bold py-1 px-0 active" to="/">Home</router-link>
                    <router-link class="nav-link fw-bold py-1 px-0" to="/features">About Us</router-link>
                    <router-link class="nav-link fw-bold py-1 px-0" to="/signup">Log In</router-link>
                </nav>
            </div>
        </header>

        <main class="px-3">
            <h1>Welcome to HAAK</h1>
            <p>Introducing HAAK - Your Personalized Dining Companion</p>
            <p>HAAK (Helpful Automated Assistant for Kitchens) is a revolutionary chatbot service designed to transform how you discover and book restaurants. Tailored to your preferences and location, HAAK offers a seamless, interactive dining experience right at your fingertips.</p>
            
            <section>
                <h2>Personalized Recommendations</h2>
                <p>HAAK excels in providing customized restaurant suggestions. By analyzing your preferences, location, and dining history, it offers relevant choices that align perfectly with your tastes and needs.</p>
            </section>

            <section>
                <h2>Predictive Suggestions</h2>
                <p>HAAK stays a step ahead by offering predictive recommendations based on your location, time of day, and past interactions, ensuring you always have dining options at your fingertips.</p>
            </section>

            <section>
                <h2>Multi-Platform Notifications</h2>
                <p>Never miss a beat with HAAK's diverse notification system. Whether it's through email, text, or app notifications, HAAK keeps you updated on your dining plans and suggestions.</p>
            </section>
        </main>

        <footer class="mt-auto text-white-50">
            <p>© 2023 HAAK. All rights reserved.</p>
        </footer>
    </div>
</template>
  
<script>
export default {
    name: 'FeaturesPage',
    // Add your component logic here
};
</script>
  
<style scoped>
/* Custom default button */
.btn-light,
.btn-light:hover,
.btn-light:focus {
    color: #333;
    text-shadow: none;
    /* Prevent inheritance from `body` */
}

/* Base structure */
body {
    text-shadow: 0 .05rem .1rem rgba(0, 0, 0, .5);
    box-shadow: inset 0 0 5rem rgba(0, 0, 0, .5);
}

/* Header */
.nav-masthead .nav-link {
    color: rgba(255, 255, 255, .5);
    border-bottom: .25rem solid transparent;
}

.nav-masthead .nav-link:hover,
.nav-masthead .nav-link:focus {
    border-bottom-color: rgba(255, 255, 255, .25);
}

.nav-masthead .nav-link+.nav-link {
    margin-left: 1rem;
}

.nav-masthead .active {
    color: #fff;
    border-bottom-color: #fff;
}
</style>
  