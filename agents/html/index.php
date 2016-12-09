<!DOCTYPE html>
<html>
<head>
<title>Agent Smith</title>
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
<img src="agents.jpg" alt="The Agents">
<h1>The Agents</h1>
<ul>
  <li> <a href="reviewd">reviewd</a> -- reviews request database and submits missing pieces
  <li> <a href="catalogd">catalogd</a> -- catalogs all files from ongoing productions
  <li> <a href="cleanupd">cleanupd</a> -- cleans up ongoing production and removes once complete
  <li> <a href="uploadd">uploadd</a> -- uploads samples into dropbox
</ul>
<?php
$output = shell_exec('ls -t reviewd/status*');
$f = explode("\n",$output);
if (sizeof($f) > 1) {
  print '<h2>Status</h2>';
  print '<ul>';
  foreach ($f as &$file) {
    if ($file != "")
      print '<li> <a href="' . $file . '">' . $file . '</a>';
  }
  print '</ul>';
}
?>
<h2>Other info</h2>
<ul>
  <li> <a href="https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes">job exit codes</a>
</ul>
<hr>
<p style="font-family: arial;font-size: 10px;font-weight: bold;color:#900000;">
<!-- hhmts start -->
Modified: Thu Oct  8 12:55:46 EDT 2015
<a href="http://web.mit.edu/physics/people/faculty/paus_christoph.html">Christoph Paus</a>
<!-- hhmts end -->
</p>
</body>
</html>
