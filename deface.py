##################
#!/usr/bin/python#
##################
# JANGAN NGE RECODE YA BGSD!!
# YA ALLAH JIKA SAYA RECODE SCRIPT INI, AMBILLAH NYAWA SAYA!
# UDAH SUMPAH LOH GAN...

logo = """    _   ___          _____           _       __
   / | / (_)_______ / ___/__________(_)___  / /_
  /  |/ / / ___/ _ \\__ \/ ___/ ___/ / __ \/ __/
 / /|  / / /__/  __/__/ / /__/ /  / / /_/ / /_
/_/ |_/_/\___/\___/____/\___/_/  /_/ .___/\__/
                                  /_/
[==========================]
[=====Author : MiSetya=====] ANTI RECODE
[=====Team   : LCI    =====] JANGAN RECODE
[=====Ver    : 1.0    =====] YA BOSQUEE..
[==========================]"""

print logo
print
print "[===Make Your Deface Script===]"
title = raw_input("[=Judul/Title=> ")
alert = raw_input("[=Alert=> ")
head = raw_input("[=Header=> ")
gambar = raw_input("[=Link Gambar=> ")
musik = raw_input("[=Link Musik=> ")
pesan1 = raw_input("[=Masukkan pesan (gunakan <br> untuk baris baru) => ")
pesan2 = raw_input("[=Masukkan Tulisan bergerak=> ")
team = raw_input("[=Team=> ")
logotim = raw_input("[=Logo Team=> ")
thanksto = raw_input("[=Thanks to=> ")


#Open index
fo = open("depes.html","w")

script1 = """<html><head><head><title>[+]"""

script2 = title

script3 = """[+]</title>
	<meta charset="UTF-8">
	<meta name="Author" content="MiSetya"/>
	<meta name="copyright" content="MiSetya"/>
<link href='http://fonts.googleapis.com/css?family=Megrim' rel='stylesheet' type='text/css'>   <link href='http://fonts.googleapis.com/css?family=Quicksand' rel='stylesheet' type='text/css'>     <script src="http://e-mete.com/js/kdsnow.js"></script>  <style>    body{     background-image: url(index.html);     background-repeat: no-repeat;      background-attachment: fixed;      background-position: top;     background-color:#000000;     position: relative;     background-size:100% 100vh;          }    .logo {     width: 300px;     height: 300px;     margin: 0 auto;     margin-top: 50px;     -webkit-filter: drop-shadow(0px 0px 7px #0080FF);     filter: drop-shadow(0px 0px 7px #0080FF);    }    .logo:hover{     width: 300px;     height: 300px;     -webkit-filter: drop-shadow(0px 0px 10px #0080FF);     opacity:0.4;     filter:alpha(opacity=40);     transition: opacity .2s ease-out;     -moz-transition: opacity .2s ease-out;     -webkit-transition: opacity .2s ease-out;     -o-transition: opacity .2s ease-out;    }    .defacedby{     font-family: Megrim;     text-align: center;     color: black;     font-weight: bold;     font-size: 40px;   text-shadow: #0080FF 1px 2px 1px;        }    .glow {     font-family: Quicksand;     text-align: center;     color: grey;     font-style: bold;     font-size: 20px;    margin-top: 16px;    text-shadow: black 1px 2px 1px;        }    .greetings{     font-family: Quicksand;     text-align: center;     color: #ffffff;     font-size: 20px;     margin-top: 50px; text-shadow: black 1px 2px 1px;    }    </style>   
</head>
<body>
<script>    alert"""

script4 = alert

script5 = """script>
<center>
<center>
<script type="text/javascript">
//Define first typing example:
new TypingText(document.getElementById("example1"));
//Define second typing example (use "slashing" cursor at the end):
new TypingText(document.getElementById("example2"), 80, function(i){
var ar = new Array("_"," ","_","_"); return " " + ar[i.length %
ar.length]; });
//Type out examples:
TypingText.runAll();
</script>
<style type="text/css">body {cursor:url(""),default}</style>
<div align="center"><table border="0" width="100%"><tr><td>
<font size="7">
<b><font face="times"><b><center><SCRIPT>
farbbibliothek = new Array();
farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");
farbbibliothek[1] = new Array("#FF0000","#FFFFFF","#FFFFFF","#FF0000");
farbbibliothek[2] = new Array("#FFFFFF","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF");
farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");
farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");
farbbibliothek[5] = new Array("#FF0000","#FF0000","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF");
farbbibliothek[6] = new Array("#FF0000","#FDF5E6");
farben = farbbibliothek[4];
function farbschrift()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.all["a"+i].style.color=farben[i];
}
farbverlauf();
}
function string2array(text)
{
Buchstabe = new Array();
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
k=0;
while(k<=text.length)
{
Buchstabe[k] = text.charAt(k);
k++;
}
}
function divserzeugen()
{
for(var i=0 ; i<Buchstabe.length; i++)
{
document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>");
}
farbschrift();
}
var a=1;
function farbverlauf()
{
for(var i=0 ; i<farben.length; i++)
{
farben[i-1]=farben[i];
}
farben[farben.length-1]=farben[-1];

setTimeout("farbschrift()",30);
}
//
var farbsatz=1;
function farbtauscher()
{
farben = farbbibliothek[farbsatz];
while(farben.length<text.length)
{
farben = farben.concat(farben);
}
farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));
}
setInterval("farbtauscher()",5000);
text ='[+]"""

script6 = head

script7 = """[+]';//h
string2array(text);
divserzeugen();
//document.write(text);
</script>
<br><br>

<marquee behavior="alternate" scrollamount="20" ;="">
      <img src='"""

script8 = gambar

script9 = """' width="500" height="500"></marquee>
      <br><br>

<marquee behavior="scroll" direction="left" scrollamount="5" scrolldelay="5" width="100%">
<audio autoplay="autoplay" controls="controls" src='"""

script10 = musik

script11 = """' type="audio/mpeg"></audio></marquee>

</div>

<div class="glow">

    <h2>
<b><font color=white><br>"""

script12 = pesan1

script13 = """<br><b><br>
<font color="red" size="6" face="Iceberg">
     <marquee behavior="alternate" scrollamount="15" ;="">
      <font size="50" color="red" ;="" face="times new roman">"""

script14 = pesan2

script15 = """</font>
     </marquee> <br> <font size="2" color="Blue"> </font><span style="color: aqua;"></span></font>
     <marquee behavior="scroll" direction="right" scrollamount="5" scrolldelay="90" width="50%"></marquee>
<br><br>
<marquee behavior="scroll" direction="left" scrollamount="90" scrolldelay="40" width="100%">
	<font color="White">___________________________________________________________</font></marquee><br><br>

<marquee behavior="alternate" scrollamount="15" ;="">
      <font size="75" color="red" ;="" face="fourty two">[+]"""

script16 = team

script17 = """[+]</font></marquee><br><br>
<marquee behavior="scroll" direction="right" scrollamount="90" scrolldelay="40" width="100%">
	<font color="white">___________________________________________________________</font></marquee>
<br><br>
     <center> <img src='"""

script18 = logotim

script19 = """' width="750" height="750"></center><br><br>

<div class="greetings">

<footer id="det" style="position:fixed; left:0px; right:0px; bottom:0px; background:black ; text- align:center; border- top: 1px solid GRAY; border-bottom: 1px solid #fffff ">

<hr color=darkred>

<font color="red" face="Quicksand">

<b>Greetz : </b>

</font>

<i>

<marquee scrollamount="8" scrolldelay="50" width="100%">

<i>

</font>

<font face="Quicksand" color="white">"""

script20 = thanksto

script21 = """</i></marquee></font></div>
  <DIV style="DISPLAY: none">

<script type="text/javascript" language="JavaScript">

    </DIV>

    </body>

 </html>"""

fo.write(script1)
fo.write(script2)
fo.write(script3)
fo.write(script4)
fo.write(script5)
fo.write(script6)
fo.write(script7)
fo.write(script8)
fo.write(script9)
fo.write(script10)
fo.write(script11)
fo.write(script12)
fo.write(script13)
fo.write(script14)
fo.write(script15)
fo.write(script16)
fo.write(script17)
fo.write(script18)
fo.write(script19)
fo.write(script20)
fo.write(script21)

print
print "[===Make The Script > SUCCESFULL!===]"
print "[===Silahkan Tulis cp depes.html /sdcard"
print "[===Dan Lihat scriptnya di penyimpanan internal===]"

fo.close()
