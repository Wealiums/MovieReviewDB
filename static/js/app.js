if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("static/js/serviceworker.js")
            .then((res) => console.log("Service worker registered"))
            .catch((err) => console.log("Service worker not registered", err));
    });
}