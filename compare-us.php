<?php
    error_reporting(0);
    include 'flag.php';
    // $check=thepassword();
    $check='dummy';
    parse_str($_SERVER['QUERY_STRING']);
    $A=$_GET['key'];
    if(ctype_xdigit($A)){
        $e=implode('',array_map(function($i,$A){return chr(hexdec($A{$i+$i}.$A{$i+($i+1)}));},list($m,$n,$o)=range(0,2),array($A,$A,$A)));
        if($e<1 && $e>0 && $e!==0){
            if((int)(substr($A,strlen($e)*2)+0) < -1){
                if($check==$_GET['password']){
                    echo flag();
                } else {
                    echo 'Bad 4.';
                }
            } else {
                echo 'Bad 3.';
            }
        } else {
            echo 'Bad 2.';
        }
    } else {
        echo 'Bad 1.';
    }
    echo "<pre>";
    echo htmlentities(highlight_string(file_get_contents(__FILE__)));
    echo "</pre>";
