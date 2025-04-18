$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
        items: 3, // Number of visible cards
        loop: true, // Enable infinite looping
        margin: 10, // Space between cards
        nav: true, // Show navigation arrows
        dots: true, // Show dots
        autoplay: true, // Enable autoplay
        autoplayTimeout: 3000, // Autoplay interval
        responsive: {
            0: { items: 1 }, // 1 card for small screens
            600: { items: 2 }, // 2 cards for medium screens
            1000: { items: 3 } // 3 cards for large screens
        }
    });
});