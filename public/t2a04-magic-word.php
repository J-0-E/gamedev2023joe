<?php$myCheck = false;
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$myInputText01 = $_POST['myText01'];
// if (strpos($myInputText01, 'fred') !== false) {if ($myInputText01 == 'fred') {$myCheck = true;}}?>
<!DOCTYPE html>
<html>
<head>
<title>Browser Title</title>
</head>
<body>
<h3 align=center>T2A06-php-codesandbox</h3>
<label for="myText01">Enter Text:</label>
<input type="text" id="myText01" name="myText01">
<input type="submit" value="Submit">
</form>
<?php
    if ($myCheck ) {echo "<b style='color:red'> Try the magic word</b>span>":}
    else {echo "<span style='color:red'> Try the magic word</span>";}
    ?>
  </body>
  </html>
  
