function showAvailableVersions(responseJSON) {
    var versions = JSON.parse(responseJSON)["versions"];
    if (versions === undefined) return;
    document.getElementById("version-links").innerHTML = "";
    for (version of versions) {
        var version_number = version["version"];
        var buttonId = `version=${version_number}`;
        document.getElementById("version-links").innerHTML += newButton(
            buttonId,
            version_number
        );
    }
    for (version of versions) {
        var version_number = version["version"];
        var buttonId = `version=${version_number}`;
        var button = document.getElementById(buttonId);
        button.addEventListener("click", (e) => {
            var url = `/cgi-bin/setVersion.py?${e["target"]["id"]}`;
            var request = new XMLHttpRequest();
            request.open("GET", url, true);
            request.onload = function () {
                var res = JSON.parse(request.responseText);
                if (res["success"] === "true") {
                    updateCurrentVersion();
                }
            };
            request.onerror = function () {};
            request.send(); // create FormData from form that triggered event
            event.preventDefault();
        });
    }
}

function parseGetVersionList(raw) {
    var versionList = [];
    raw.forEach((e) => {
        versionList.push(e["version"]);
    });
    return versionList;
}

function getVersionLinks() {
    httpGetAsync("/cgi-bin/getVersionList.py", showAvailableVersions);
}

function updateVersionLinks() {
    httpGetAsync("/cgi-bin/updateVersionList.py", (res) => {
        getVersionLinks();
    });
}

function updateCurrentVersion() {
    httpGetAsync("/cgi-bin/getVersion.py", (responseJSON) => {
        var res = JSON.parse(responseJSON)["server-version"];
        document.getElementById("version").innerText = res;
    });
}

updateCurrentVersion();
getVersionLinks();

var updateVersionLinksButton = document.getElementById(
    "update-version-links-button"
);
updateVersionLinksButton.addEventListener("click", updateVersionLinks);
