(function (url) {
    sanitized = scriptPolicy.create;
})(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        let url = "https://127.0.0.1:8000/static/images/js/bookmarklet.js?r=";
        let source = String(Math.floor(Math.random() * 99999999999999999999));
        console.log(source);
        document.body.appendChild(document.createElement("script")).src =
            url + source;
    }
})();
