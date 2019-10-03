StringTemplate@"
<html>
<body>

<input type=\"range\" id=\"x\" min=\"`x1`\" max=\"`x2`\" step=\"`x3`\" class=\"slider\" oninput=\"refresh();\">
<div id=\"result\"></div>
<script src="javascript.js">
<script>
	refresh = function(`v`) {
		const request = new XMLHttpRequest();
		const url = \"http://127.0.0.1:5859\";
		var `v` = document.getElementById(\"x\").value;

		data = \"`f`\";

		request.onload = function() {
			document.getElementById(\"result\").innerHTML = request.responseText;
		}

		request.open(\"POST\", url, true);
		request.send(data);
	}
</script>

</body>
</html>
"
