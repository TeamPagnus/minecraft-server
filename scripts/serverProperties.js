function fillNumbers(key, value) {
	numberFields = ["max-players", "spawn-protection"];
	if (numberFields.includes(key)) {
		document.getElementById(key).value = value;
	}
}

function fillSelects(key, value) {
	selectFields = ["difficulty"];
	if (selectFields.includes(key)) {
		document.getElementById(key).value = value;
	}
}

function fillRadios(key, value) {
	radioFields = [
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
	textFields = ["resource-pack"];
	if (textFields.includes(key)) {
		document.getElementById(key).value = value;
	}
}

function updateServerProperties(responseJSON) {
	response = JSON.parse(responseJSON)["server-properties"];
	for (const [key, value] of Object.entries(response)) {
		fillNumbers(key, value);
		fillSelects(key, value);
		fillRadios(key, value);
		fillText(key, value);
	}
}

httpGetAsync("/cgi-bin/getServerProperties.py", updateServerProperties);
