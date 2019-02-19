<!DOCTYPE html>
<HTML>
<HEAD>
<META http-equiv='Content-Type' content='text/html; charset=utf-8' />
<TITLE>サンプル</TITLE>
</HEAD>
<BODY>

<?php
    $cmd = (isset($_POST['cmd']))? $_POST['cmd'] : 0;
    if($cmd > 0){
        if(is_uploaded_file($_FILES['upfile']['tmp_name'])){
        move_uploaded_file($_FILES['upfile']['tmp_name'], 'tmp.csv');
        exec('python csv_calc.py tmp.csv $cmd', $resp, $code);
        echo $resp[0];
        unlink('tmp.csv');
        }
    }
?>

<hr />
<form enctype='multipart/form-data' action='./' method=post>
<input type=file name=upfile><br />
<select name=cmd>
    <option value=1>sum
    <option value=2>ave
    <option value=3>max
    <option value=4>min
</select>
<input type=submit value='result'>
</form>

</BODY>
</HTML>

