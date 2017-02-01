<!DOCTYPE html>
<html>
<head>
<title>Agents</title>
</head>
<style>
a:link{color:#000000; background-color:transparent; text-decoration:none}
a:visited{color:#009000; background-color:transparent; text-decoration:none}
a:hover{color:#900000;background-color:transparent; text-decoration:underline}
a:active{color:#900000;background-color:transparent; text-decoration:underline}
body.ex{margin-top: 0px; margin-bottom:25px; margin-right: 25px; margin-left: 25px;}
</style>

<body class="ex" bgcolor="#EEEEEE">
<body style="font-family: arial;font-size: 20px;font-weight: bold;color:#900000;">
<hr>
<img src="Kraken.jpg" width="850px" alt="The Agents">
<h1>The Agents</h1>
<ul>
  <li> <a href="reviewd">reviewd</a> -- reviews request database and submits missing pieces
  <li> <a href="catalogd">catalogd</a> -- catalogs all files from ongoing productions
</ul>
<!-- <img src="agents.jpg" alt="The Agents"> -->
<hr>
<p style="font-family: arial;font-size: 10px;font-weight: bold;color:#900000;">
<!-- hhmts start -->
<?php
$output = shell_exec('cat heartbeat');
$f = explode("\n",$output);
foreach ($f as &$line) {
  print $line;
}
?>
-- <a href="http://web.mit.edu/physics/people/faculty/paus_christoph.html">Christoph Paus</a>
<!-- hhmts end -->
</p>
</body>
</html>
