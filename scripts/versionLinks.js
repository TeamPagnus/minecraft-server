function generateVersionLink(version) {
	var versionLinkHTML = `<a href="/cgi-bin/setVersion.py?version=${version}">${version}</a> `;
	return versionLinkHTML;
}

function parseGetVersionList(raw) {
	var versionList = [];
	raw.forEach((e) => {
		versionList.push(e["version"]);
	});
	return versionList;
}

function getVersionLinks() {
	httpGetAsync("/cgi-bin/getVersionList.py", (responseJSON) => {
		res = JSON.parse(responseJSON)["versions"]
		var versionList = parseGetVersionList(res);
		document.getElementById("version-links").innerHTML = "";
		versionList.forEach((e) => {
			document.getElementById("version-links").innerHTML += generateVersionLink(e);
		});
	});
}

function updateVersionLinks() {
	httpGetAsync("/cgi-bin/updateVersionList.py", (res) => {
		getVersionLinks();
	});
}

getVersionLinks();

var updateVersionLinksButton = document.getElementById("update-version-links-button");
updateVersionLinksButton.addEventListener("click", updateVersionLinks);
