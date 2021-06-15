// Get elements
var startStopButton = document.getElementById("start-stop-button");
var consoleOut = document.getElementById("console-out");
var sendBtn = document.getElementById("send-command");
var commandText = document.getElementById("command");

// Utility functions
function enableBtns(isEnabled) {
    startStopButton.disabled = !isEnabled;
    sendBtn.disabled = !isEnabled || startStopButton.innerText == "Start";
}

function updateBtn() {
    console.log("updating btn");
    httpGetAsync("/cgi-bin/getServerStatus.py", async function (responseText) {
        var res = JSON.parse(responseText)["server-status"];
        console.log(responseText);
        if (responseText.includes("started")) {
            startStopButton.innerText = "Stop";
            enableBtns(true);
        } else if (responseText.includes("stopped")) {
            startStopButton.innerText = "Start";
            enableBtns(true);
        } else {
            startStopButton.innerText = "Waiting...";
            enableBtns(false);
            await sleep(2000);
            updateBtn();
        }
    });
    httpGetAsync("/cgi-bin/getLastConsoleOutput.py", function (responseText) {
        var res = JSON.parse(responseText)["console-output"];
        consoleOut.innerText = res;
        consoleOut.scrollHeight;
    });
}

// Main
updateBtn();
consoleOut.scrollHeight;
sendBtn.onclick = function () {
    var command = commandText.value;
    // btoa codifica en base 64
    var commandBase64 = btoa(command);
    httpGetAsync(
        "/cgi-bin/sendConsoleCommand.py?command=" + commandBase64,
        function (responseText) {
            console.log(responseText);
            updateBtn();
        }
    );
    commandText.value = "";
};

startStopButton.onclick = function () {
    console.log(startStopButton.innerText);
    if (startStopButton.innerText == "Stop") {
        enableBtns(false);
        httpGetAsync("/cgi-bin/stopServer.py", function () {
            updateBtn();
        });
    } else if (startStopButton.innerText == "Start") {
        enableBtns(false);
        httpGetAsync("/cgi-bin/startServer.py", function () {
            updateBtn();
        });
    }
};

commandText.addEventListener("keyup", function (event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        sendBtn.click();
    }
});
