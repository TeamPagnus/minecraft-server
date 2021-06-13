function setSelectedWorld(world) {
	world = world.split("=")[1];
	document.getElementById("selected-world").innerHTML = world;
	document.getElementById("selected-world").innerHTML += ` <a href="/cgi-bin/downloadWorld.py?level-name=${world}">Download<a>`;
	document.getElementById("selected-world").innerHTML += ` <a href="/cgi-bin/deleteWorld.py?level-name=${world}">Delete<a>`;
}

function setAvailableWorlds(raw) {
	worlds = raw.split("\n");
	for (world of worlds) {
		document.getElementById("available-worlds").innerHTML += `<a href="/cgi-bin/setWorld.py?level-name=${world}">${world}<a> `;
	}
}

httpGetAsync("/cgi-bin/getCurrentWorld.py", setSelectedWorld);
httpGetAsync("/cgi-bin/getWorldsList.py", setAvailableWorlds);
