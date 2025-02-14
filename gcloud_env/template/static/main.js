document.addEventListener("DOMContentLoaded", function () {
    let title = document.getElementById("title");

    title.addEventListener("mouseover", function () {
        this.style.color = "red";
    });

    title.addEventListener("mouseout", function () {
        this.style.color = "black";
    });
});