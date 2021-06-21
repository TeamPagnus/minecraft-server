function fillNumbers(key, value) {
    var numberFields = ["max-players", "spawn-protection"];
    if (numberFields.includes(key)) {
        document.getElementById(key).value = value;
    }
}

function fillSelects(key, value) {
    var selectFields = ["difficulty"];
    if (selectFields.includes(key)) {
        document.getElementById(key).value = value;
    }
}

function fillRadios(key, value) {
    var radioFields = [
        "online-mode",
        "enable-command-block",
        "spawn-animals",
        "spawn-npcs",
        "force-gamemode",
        "white-list",
        "pvp",
        "allow-flight",
        "spawn-monsters",
        "allow-nether",
    ];
    if (radioFields.includes(key)) {
        document.getElementById(`${key}-${value}`).checked = true;
    }
}

function fillText(key, value) {
    var textFields = ["resource-pack"];
    if (textFields.includes(key)) {
        document.getElementById(key).value = value;
    }
}

function updateServerProperties(responseJSON) {
    var response = JSON.parse(responseJSON)["server-properties"];
    if (response === undefined) return;
    for (const [key, value] of Object.entries(response)) {
        fillNumbers(key, value);
        fillSelects(key, value);
        fillRadios(key, value);
        fillText(key, value);
    }
}

function setServerProperties(event) {
    var url = "/cgi-bin/setServerProperties.py";
    var request = new XMLHttpRequest();
    request.open("POST", url, true);
    request.onload = function () {
        // request successful
        // we can use server response to our request now
        var res = JSON.parse(request.responseText);
        if (res["success"] === "true") {
            document.getElementById(
                "server-properties-success"
            ).innerText = `server.properties saved. (${getCurrentDatetime()})`;
        } else {
            document.getElementById("server-properties-success").innerText =
                "Failed to save.";
        }
    };

    request.onerror = function () {
        // request failed
    };

    request.send(new FormData(event.target)); // create FormData from form that triggered event
    event.preventDefault();
}

document
    .getElementById("server-properties")
    .addEventListener("submit", setServerProperties);

httpGetAsync("/cgi-bin/getServerProperties.py", updateServerProperties);
