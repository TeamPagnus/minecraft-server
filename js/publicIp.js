var publicIp = document.getElementById("public-ip");

httpGetAsync("/cgi-bin/getPublicIp.py", function (responseJSON) {
	var res = JSON.parse(responseJSON)["ip-address"];
	publicIp.innerText = res;
});
