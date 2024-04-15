// Get all the navigation links
var navLinks = document.querySelectorAll("nav a");

// Add an event listener for when a user clicks on a navigation link
for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener("click", function () {
        // Remove the active class from all the navigation links
        var navLinks = document.querySelectorAll("nav a");
        for (var i = 0; i < navLinks.length; i++) {
            navLinks[i].className = navLinks[i].className.replace(" active", "");
        }

        // Add the active class to the clicked navigation link
        this.className += " active";
    });
}