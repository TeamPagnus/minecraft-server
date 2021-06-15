function updateCurrentVersion() {
	httpGetAsync("/cgi-bin/getVersion.py", (responseJSON) => {
		var res = JSON.parse(responseJSON)["server-version"]
		document.getElementById("version").innerText = res;
	});
}

updateCurrentVersion();
