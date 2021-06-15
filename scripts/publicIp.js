var publicIp = document.getElementById("public-ip");

httpGetAsync("/cgi-bin/getPublicIp.py", function (responseJSON) {
	var res = JSON.parse(responseJSON)["ip-address"];
	console.log(res);
	publicIp.innerText = res;
});
