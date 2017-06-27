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
<?php
$cycle = '/home/cmsprod/Tools/Kraken/agents/cycle.cfg';
$output = shell_exec('ls -1r reviewd/*/*/status*.html');
$f = explode("\n",$output);
if (sizeof($f) > 1) {

  $active = shell_exec('source ' . $cycle . '; echo $KRAKEN_REVIEW_CYCLE');
  print '<h2>Active Reviews</h2>';
  print '<ul>';
  $f = explode(" ",$active);
  foreach ($f as &$request) {
    print '<li>' . $request . "</li>\n";
  }
  print '</ul>';

  print '<h2>Status</h2>';
  print '<ul>';
  $f = explode("\n",$output);
  $book = "";
  $pys = array();
  $search = array("status-",".html");
  $replace = array("","");
  foreach ($f as &$file) {
    if ($file != "") {
      $text = str_replace($search,$replace,$file);
      $g = explode("/",$text);
      $agent = $g[0];
      if ($g[1].'/'.$g[2] == $book) {
	$pys[] = $g[3];
      }
      else {
	if ($book != '') {
	  print '<li> '.$book.' : ';
	  foreach ($pys as &$py) {
	    print ' <a href="'.$agent.'/'.$book.'/status-'.$py.'.html">'.$py.'</a>';
	  }
	}
	$book = $g[1].'/'.$g[2];
	$pys = array();
	$pys[] = $g[3];
      }
    }
  }
  // do not forget last elemet
  print '<li> '.$book.' : ';
  foreach ($pys as &$py) {
    print ' <a href="'.$agent.'/'.$book.'/status-'.$py.'.html">'.$py.'</a>';
  }

  print '</ul>';
}
?>
<h2>The Agents</h2>
<ul>
  <li> <a href="reviewd">reviewd</a> -- reviews request database and submits missing pieces
  <li> <a href="catalogd">catalogd</a> -- catalogs all files from ongoing productions
  <li> <a href="cleanupd">cleanupd</a> -- cleans up all ongoing productions
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
