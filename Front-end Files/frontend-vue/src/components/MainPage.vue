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
            <div class="pages">
                <div class="pages-content">
                    <div class="page" id="page-0">
                        <div class="page-content">
                            <h1>Helpful Automated Assistant for Kitchens</h1>
                            <p class="lead">Discover perfect dining spots with HAAK, your concierge that
                                personalizes recommendations based on your location, time, and taste.</p>
                            <p class="lead">
                                <router-link to="#page-1" class="btn btn-lg btn-light fw-bold border-white bg-white">Learn
                                    more</router-link>
                                <router-link to="/signup" class="btn btn-lg btn-light fw-bold border-white bg-white">Try
                                    Now</router-link>
                            </p>
                        </div>
                    </div>
                    <div class="page" id="page-1">
                        <div class="page-content">
                            <h2>Personalized recommendations. When you want them.</h2>
                            <p class="lead">HAAK learns about your eating preferences and recommends restaurants based on what you
                                previously booked. A unique experience awaits every time.</p>
                        </div>
                    </div>
                    <div class="page" id="page-2">
                        <div class="page-content">
                            <h2>Location. A good place to start.</h2>
                            <p class="lead">Start by telling the chatbot the area you are looking for restaurants.</p>
                            <div class="collapsible collapsed">
                                <a class="btn btn-lg btn-light fw-bold border-white bg-white collapsible-button"
                                    data-show="See example" data-hide="Hide example">See example</a>
                                <div class="collapsible-content">
                                    <p>HAAK: Hi, I am HAAKY, your restaurant chatbot assistant, and I am here to help you
                                        recommend restaurants. First, I will need some information to best assist you.
                                        Please give a description of the location you would like me to find recommendations.
                                    </p>
                                    <p>User: Brooklyn</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="page" id="page-3">
                        <div class="page-content">
                            <h2>What kind of cuisine would you like?</h2>
                            <p class="lead">HAAK takes the cuisine you'd like when making its first recommendations.</p>
                            <div class="collapsible collapsed">
                                <a class="btn btn-lg btn-light fw-bold border-white bg-white collapsible-button"
                                    data-show="See example" data-hide="Hide example">See example</a>
                                <div class="collapsible-content">
                                    <p>HAAK: Hi, I am HAAKY, your restaurant chatbot assistant, and I am here to help you
                                        recommend restaurants. First, I will need some information to best assist you.
                                        Please give a description of the location you would like me to find recommendations.
                                    </p>
                                    <p>User: Brooklyn</p>
                                    <p>HAAK: What cusine are you interested in?</p>
                                    <p>User: Mexican</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="page" id="page-4">
                        <div class="page-content">
                            <h2>Now pick a restaurant.</h2>
                            <p class="lead">HAAK searches for restaurants matching your cuisine preference through Yelp.</p>
                            <div class="collapsible collapsed">
                                <a class="btn btn-lg btn-light fw-bold border-white bg-white collapsible-button"
                                    data-show="See example" data-hide="Hide example">See example</a>
                                <div class="collapsible-content">
                                    <p>HAAK: Hi, I am HAAKY, your restaurant chatbot assistant, and I am here to help you
                                        recommend restaurants. First, I will need some information to best assist you.
                                        Please give a description of the location you would like me to find recommendations.
                                    </p>
                                    <p>User: Brooklyn</p>
                                    <p>HAAK: What cusine are you interested in?</p>
                                    <p>User: Mexican</p>
                                    <p>HAAK: Here are some options: ... 1. Restaurant - Address 2, Some Other Restaurant - Address ...</p>
                                    <p>User: 2</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="page" id="page-4">
                        <div class="page-content">
                            <h2>Ready to reserve.</h2>
                            <p class="lead">HAAK will send an invite for the restaurant you picked.</p>
                            <div class="collapsible collapsed">
                                <a class="btn btn-lg btn-light fw-bold border-white bg-white collapsible-button"
                                    data-show="See example" data-hide="Hide example">See example</a>
                                <div class="collapsible-content">
                                    <p>HAAK: Hi, I am HAAKY, your restaurant chatbot assistant, and I am here to help you
                                        recommend restaurants. First, I will need some information to best assist you.
                                        Please give a description of the location you would like me to find recommendations.
                                    </p>
                                    <p>User: Brooklyn</p>
                                    <p>HAAK: What cusine are you interested in?</p>
                                    <p>User: Mexican</p>
                                    <p>HAAK: Here are some options: 1. Restaurant - Address 2, Some Other Restaurant - Address ...</p>
                                    <p>User: 2</p>
                                    <p>HAAK: Restaurant selected: Some Other Restaurant. Would you like to make a reservation?</p>
                                    <p>User: Yes</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="page" id="page-5">
                        <div class="page-content">
                            <h2>Try it out now.</h2>
                            <p class="lead">Ready to get started? </p>
                            <router-link to="/signup" class="btn btn-lg btn-light fw-bold border-white bg-white">Try
                                    Now</router-link>
                        </div>
                    </div>
                </div>
                <div class="page-navigation">
                    <router-link class="page-back" to="#">&leftarrow;</router-link>
                    <router-link to="#page-0">1</router-link>
                    <router-link to="#page-1">2</router-link>
                    <router-link to="#page-2">3</router-link>
                    <router-link to="#page-3">4</router-link>
                    <router-link to="#page-4">5</router-link>
                    <router-link to="#page-5">6</router-link>
                    <router-link class="page-forward" to="#">&rightarrow;</router-link>
                </div>
            </div>
        </main>

        <footer class="mt-auto text-white-50">
            <p>©️ HAAK</p>
        </footer>
    </div>
</template>

<script>
import $ from "jquery";
var checkPages;

export default {
    name: 'MainPage',
    mounted: function () {
        $(document).ready(function () {
            $('.pages').each(function() {
                var pages = $(this).find(".pages-content .page").toArray();
                //             $('style').eq($('style').length - 1).after(`
                // <style>
                // .pages {
                //     height: ${pages.length * 100}%
                // }
                // </style>
                // `)
                var pageNumber = 0;
                // console.log(pageNumber);
                var oldurl = new URL("https://localhost/");
                var that = this;
                var pagination = function(init) {
                    var url = new URL(window.location);
                    if (url.href != oldurl.href) {
                        if (url.hash && url.hash != "#") {
                            for (var i in pages) {
                                if ($(pages[i]).attr('id').startsWith("page-")) {
                                    if ($(pages[i]).attr('id') == url.hash.substring(1, url.hash.length)) {
                                        $(that).find('.pages-content').animate({scrollTop: $(that).find('.pages-content').innerHeight() * i }, 2000);
                                        pageNumber = i;
                                        oldurl = new URL(window.location);
                                        return;
                                    }
                                }
                            }
                        }
                    }
                    if (init) {
                        for (i in pages) {
                            if ($(pages[i]).attr('id').startsWith("page-")) {
                                $(`a[href="#${$(pages[i]).attr('id')}"], a[href="${window.location.href}#${$(pages[i]).attr('id')}"], a[href="${window.location.pathname}#${$(pages[i]).attr('id')}"]`).click(function(e) {
                                    e.preventDefault();
                                    pageNumber = i;
                                    $(that).find('.pages-content').animate({scrollTop: $(that).find('.pages-content').innerHeight() * i }, 2000);
                                })
                            }
                        }
                    }
                    oldurl = new URL(window.location);
                }
                pagination(true);
                checkPages = window.setInterval(pagination, 100);
                // function freezeScrollBar(e) {
                //     e.preventDefault();
                //     $(this).scrollTop(lsp);
                // }
                function handlePageScrolling(e) {
                    // $("#page-" + pageNumber).removeClass("currentPage");
                    // var csp = $(this).scrollTop();
                    //e.preventDefault();
                    $(this).off("mousewheel");
                    if (e.originalEvent.wheelDelta < 0) {
                        pageNumber += 1;
                    } else if (e.originalEvent.wheelDelta > 0) {
                        pageNumber -= 1;
                    } else {
                        $(this).on("mousewheel", handlePageScrolling);
                        return;
                    }
                    var that = this;
                    if (pageNumber >= pages.length) {
                        pageNumber = pages.length - 1;
                    }
                    if (pageNumber < 0) {
                        pageNumber = 0;
                    }
                    $(this).animate({ scrollTop: $(this).innerHeight() * pageNumber }, 2000);
                    window.setTimeout(function () {
                        $(that).on("mousewheel", handlePageScrolling);
                    }, 2500);
                    // $("#page-" + pageNumber).addClass("currentPage");
                    // console.log(pageNumber);
                }
                $(this).find(".pages-content").on("mousewheel", handlePageScrolling);
                $(this).find(".page-forward").click(function(e) {
                    e.preventDefault();
                    pageNumber += 1;
                    if (pageNumber >= pages.length) {
                        pageNumber = pages.length - 1;
                        return;
                    }
                    $(that).find(".pages-content").animate({scrollTop: $(that).find('.pages-content').innerHeight() * pageNumber }, 2000);
                })
                $(this).find(".page-back").click(function(e) {
                    e.preventDefault();
                    pageNumber -= 1;
                    if (pageNumber < 0) {
                        pageNumber = 0;
                        return;
                    }
                    $(that).find(".pages-content").animate({scrollTop: $(that).find('.pages-content').innerHeight() * pageNumber }, 2000);
                })
            })
            $('.collapsible').each(function () {
                console.log(this);
                var that = this;
                console.log($(this).find('.collapsible-button'));
                $(this).find('.collapsible-button').click(function (e) {
                    e.preventDefault();
                    $(that).toggleClass('collapsed');
                })
            });
        });
    },
    beforeUnmount: function () {
        $("*").each(function () {
            $(this).off();
        })
        window.clearInterval(checkPages);
    }
    // Add your component logic here
};
</script>
  
<style scoped>
/* Custom default button */

.pages .pages-content {
    width: 100%;
    height: 80vh;
    overflow: hidden;
}

.pages .pages-content .page {
    width: 100%;
    height: 100%;
    overflow: auto;
}

.pages .pages-content .page .page-content {
    padding: 10% 20% 10% 20%;
}

.pages .page-navigation a {
    padding: 3px;
    color: white;
    text-align: center;
    font-size: 120%;
}

.btn-light,
.btn-light:hover,
.btn-light:focus {
    color: #333;
    text-shadow: none;
    /* Prevent inheritance from `body` */
    margin: 3px;
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

.collapsible.collapsed .collapsible-content {
    display: none;
}</style>
  