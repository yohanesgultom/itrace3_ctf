<?php

$check = 'secret';

// satisfy fourth condition
// exploit parse_str() to override $check
// by passing var named "check" in query string
parse_str($_SERVER['QUERY_STRING']);

// satisfy first and second condition
// can be any value x where 1 > x > 0
$f = "0.1";
$A = implode('', array_map(
    function ($i, $f) {
        $val = dechex(ord($f));
        return $val{0}.$val{1};
    },
    list($m,$n,$o)=range(0,2),
    array($f{0},$f{1},$f{2})
));

// satisfy first and third condition
// PHP int max limit = 9223372036854775807
// http://php.net/manual/en/function.intval.php
$limit_break = "9223372036854775808";
$A = $A.$limit_break;

echo "<p>A: $A</p>";

/** Testing **/

if (ctype_xdigit($A)) {
    echo '<p>ctype_xdigit OK</p>';
} else {
    echo "<p>ctype_xdigit FAILED</p>";
    die();
}

$e = implode('', array_map(function($i,$A){return chr(hexdec($A{$i+$i}.$A{$i+($i+1)}));},list($m,$n,$o)=range(0,2),array($A,$A,$A)));

echo "<p>e: $e</p>";

if ($e < 1 && $e > 0 && $e !== 0) {
    echo '<p>lt 1 and gt 0 and not 0 OK</p>';
} else {
    echo "<p>lt 1 and gt 0 and not 0 FAILED</p>";
    die();
}

$x = (int)(substr($A, strlen($e)*2)+0);
echo "<p>f(A,e): $x</p>";

if((int)(substr($A, strlen($e)*2)+0) < -1) {
    echo '<p>lt -1 OK</p> ';
} else {
    echo '<p>lt -1 FAILED</p>';
    die();
}

// in order to make this work,
// add query string var "password" and "check" eg. ?password=ganteng&check=ganteng
// with same values (can be anything)
if($check == $_GET['password']){
    echo '<p>VAR overriding OK</p> OK';
} else {
    echo '<p>VAR overriding FAILED</p>';
    die();
}

echo "<p>SUCCESS</p>"

?>
