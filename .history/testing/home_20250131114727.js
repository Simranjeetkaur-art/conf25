// Snippet 1: Navigation Toggle
document.querySelector(".nav-toggle").addEventListener("click", event => {
    const nav = document.querySelector(".nav");
    const header = document.querySelector(".header");

    if (event.target.dataset.menustate === "closed") {
        event.target.dataset.menustate = nav.dataset.state = header.dataset.menustate = "open";
    } else {
        event.target.dataset.menustate = nav.dataset.state = header.dataset.menustate = "closed";
    }
});

// Snippet 3: Contact Form Submission
document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    if (name && email && message) {
        document.getElementById("form-status").textContent = "Message Sent Successfully!";
        document.getElementById("form-status").style.color = "green";
        this.reset();
    } else {
        document.getElementById("form-status").textContent = "Please fill in all fields.";
        document.getElementById("form-status").style.color = "red";
    }
});
