function toggleFavorite(element) {
    if (element.innerText === "Add to Favorites") {
        element.innerText = "Added";
    } else {
        element.innerText = "Add to Favorites";
    }
}