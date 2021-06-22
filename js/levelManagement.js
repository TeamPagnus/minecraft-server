function configureDownloadLevelButton() {
    var downloadLevelButton = document.getElementById(
        "selected-level-download"
    );
    refreshElement(downloadLevelButton);
    var downloadLevelButton = document.getElementById(
        "selected-level-download"
    );
    downloadLevelButton.addEventListener("click", (e) => {
        var level = document.getElementById("selected-level").innerHTML;
        var url = `/cgi-bin/downloadLevel.py?level-name=${level}`;
        httpGetAsync(url, (res) => {
            res = JSON.parse(res);
            if (res["success"] === "true") {
                window.open(res["url"]);
            }
        });
    });
}

function configureDeleteLevelButton() {
    var deleteLevelButton = document.getElementById("selected-level-delete");
    refreshElement(deleteLevelButton);
    var deleteLevelButton = document.getElementById("selected-level-delete");
    deleteLevelButton.addEventListener("click", (e) => {
        var level = document.getElementById("selected-level").innerHTML;
        var url = `/cgi-bin/deleteLevel.py?level-name=${level}`;
        httpGetAsync(url, (res) => {
            res = JSON.parse(res);
            if (res["success"] === "true") {
                updateLevelModule();
            }
        });
    });
}

function getSelectedLevel(responseJSON) {
    var level = JSON.parse(responseJSON)["level-name"];
    document.getElementById("selected-level").innerHTML = level;
    configureDownloadLevelButton();
    configureDeleteLevelButton();
}

function getAvailableLevels(responseJSON) {
    var levels = JSON.parse(responseJSON)["levels"];
    document.getElementById("available-levels").innerHTML = "";
    for (level of levels) {
        var level_name = level["level-name"];
        var buttonId = `level-name=${level_name}`;
        document.getElementById("available-levels").innerHTML += newButton(
            buttonId,
            level_name
        );
    }
    for (level of levels) {
        var level_name = level["level-name"];
        var buttonId = `level-name=${level_name}`;
        var button = document.getElementById(buttonId);
        button.addEventListener("click", (e) => {
            var url = `/cgi-bin/setLevel.py?${e["target"]["id"]}`;
            httpGetAsync(url, (res) => {
                res = JSON.parse(res);
                if (res["success"] === "true") {
                    updateLevelModule();
                }
            });
        });
    }
}

function setLevelName(event) {
    var url = "/cgi-bin/setLevel.py";
    var request = new XMLHttpRequest();
    request.open("POST", url, true);
    request.onload = function () {
        // request successful
        // we can use server response to our request now
        updateLevelModule();
    };

    request.onerror = function () {
        // request failed
    };

    request.send(new FormData(event.target)); // create FormData from form that triggered event
    event.preventDefault();
}

function uploadLevel(event) {
    var url = "/cgi-bin/uploadLevel.py";
    var request = new XMLHttpRequest();
    request.open("POST", url, true);
    request.onload = function () {
        var res = JSON.parse(request.responseText);
        if (res["success"] === "true") {
            document.getElementById(
                "upload-level-success"
            ).innerText = `Upload successful. (${getCurrentDatetime()})`;
            updateLevelModule();
        }
    };

    request.onerror = function () {
        // request failed
    };

    request.send(new FormData(event.target)); // create FormData from form that triggered event
    event.preventDefault();
}

function updateLevelModule() {
    httpGetAsync("/cgi-bin/getCurrentLevel.py", getSelectedLevel);
    httpGetAsync("/cgi-bin/getLevelsList.py", getAvailableLevels);
}

document
    .getElementById("set-level-name")
    .addEventListener("submit", setLevelName);
document.getElementById("upload-level").addEventListener("submit", uploadLevel);

updateLevelModule();
