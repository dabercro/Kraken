<?php
$name = shell_exec('pwd');
$f = explode("/",$name);
$name = array_pop($f);

print '<!DOCTYPE html>';
print '<html>';
print '<head>';
print '<title>'. $name .'</title>';
print '</head>';
print '<h1 style="font-family: arial;font-size: 20px;font-weight: medium;color:#222222;">Sample: ' . $name . '</h1>';
print '<style>';
print 'a:link{color:#000000; background-color:transparent; text-decoration:none}';
print 'a:visited{color:#009000; background-color:transparent; text-decoration:none}';
print 'a:hover{color:#900000;background-color:transparent; text-decoration:underline}';
print 'a:active{color:#900000;background-color:transparent; text-decoration:underline}';
print 'body.ex{margin-top:25px; margin-bottom:25px; margin-right: 25px; margin-left: 25px;}';
print '</style>';
print '<body class="ex" bgcolor="#EFEFEF">';
print '<body style="font-family: arial;font-size: 16px;font-weight: medium;color:#444444;">';
print '<hr>';

// add the error analysis overview here
$output = shell_exec('cat README');
if ($output != '') {
  print '<pre>';
  $f = explode("\n",$output);
  foreach ($f as &$file) {
    print $file.'<br>';
  }
  //print $output;
  print '</pre><hr>';
}

// list the log files and provide link access
$output = shell_exec('ls -t *.err');
$f = explode("\n",$output);
if (sizeof($f) > 1) {
  print '<code><ul>';
  foreach ($f as &$file) {
    $search = array(".err");
    $replace1 = array(".out");
    $replace2 = array("");
    if ($file != "") {
      $err = $file;
      $out = str_replace($search,$replace1,$file);
      $stub = str_replace($search,$replace2,$file);
      print '<li> '. $stub . ' <a href="' . $out . '">out</a>, ' . '<a href="' . $err . '">err</a>';
    }
  }
}
print '</ul></code>';
?>

<hr>
<p style="font-family: arial;font-size: 10px;font-weight: bold;color:#900000;">
<!-- hhmts start -->
Modified: Sat Dec 17 14:23:04 EST 2016
<a href="http://web.mit.edu/physics/people/faculty/paus_christoph.html">Christoph Paus</a>
<!-- hhmts end -->
</p>
</body></html>
