function toggleReadMore(cardNumber) {
    var fullText = document.querySelector(".blog-item-" + cardNumber + " .full-text");
    var readMoreButton = document.querySelector(".blog-item-" + cardNumber + " .read-more");

    fullText.classList.toggle("hidden");

    if (fullText.classList.contains("hidden")) {
        readMoreButton.innerHTML = "Show More";
        readMoreButton.classList.remove("red-text");
    } else {
        readMoreButton.innerHTML = "Show Less";
        readMoreButton.classList.add("red-text");
    }
}
