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

function updateServerProperties(response) {
	response = response.split("\n");
	for (l of response) {
		property = l.split("=");
		key = property[0];
		value = property[1];
		fillNumbers(key, value);
		fillSelects(key, value);
		fillRadios(key, value);
		fillText(key, value);
	}
}

httpGetAsync("/cgi-bin/getServerProperties.py", updateServerProperties);
