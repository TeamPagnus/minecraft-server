function setSelectedLevel(responseJSON) {
	var level = JSON.parse(responseJSON)["level-name"];
	document.getElementById("selected-level").innerHTML = level;
	document.getElementById(
		"selected-level"
	).innerHTML += ` <a href="/cgi-bin/downloadLevel.py?level-name=${level}">Download<a>`;
	document.getElementById(
		"selected-level"
	).innerHTML += ` <a href="/cgi-bin/deleteLevel.py?level-name=${level}">Delete<a>`;
}

function setAvailableLevels(responseJSON) {
	var levels = JSON.parse(responseJSON)["levels"];
	for (level of levels) {
		level_name = level["level-name"];
		document.getElementById(
			"available-levels"
		).innerHTML += `<a href="/cgi-bin/setLevel.py?level-name=${level_name}">${level_name}<a> `;
	}
}

httpGetAsync("/cgi-bin/getCurrentLevel.py", setSelectedLevel);
httpGetAsync("/cgi-bin/getLevelsList.py", setAvailableLevels);
