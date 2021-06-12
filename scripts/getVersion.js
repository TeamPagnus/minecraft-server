function updateCurrentVersion() {
	httpGetAsync("/cgi-bin/getVersion.py", (res) => {
		document.getElementById("version").innerText = res;
	});
}

updateCurrentVersion();
