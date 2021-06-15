function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function getCurrentDatetime() {
    var today = new Date();
    var date =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();
    var time =
        today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    var dateTime = date + " " + time;
    return dateTime;
}

function newButton(buttonId, text) {
    var button = `<button id="${buttonId}" type="button">${text}</button>`;
    return button;
}

/*
 * // This function serves as a preset for custom form submitting.
 * function formSubmit(event) {
 *     var url = "";
 *     var request = new XMLHttpRequest();
 *     request.open("POST", url, true);
 *     request.onload = function () {
 *         // request successful
 *         // we can use server response to our request now
 *         console.log(request.responseText);
 *     };
 *
 *     request.onerror = function () {
 *         // request failed
 *     };
 *
 *     request.send(new FormData(event.target)); // create FormData from form that triggered event
 *     event.preventDefault();
 * }
 * // It can be attached to a form with the following command.
 * document.getElementById(formId).addEventListener("submit", formSubmit);
 */
