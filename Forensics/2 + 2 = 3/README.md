# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Hint
The flag has two parts.

# Writeup
In this challenge a memory dump is given and so just use the volatility.
```
vol.py -f memory.raw imageinfo
```  
<p align="center">
  <img src="Writeup Files/1.png">
</p>


So profile is `win7`. Check the clipboard.
```
vol.py -f memory.raw --profile=Win7SP1x64 clipboard -v
```  
<p align="center">
  <img src="Writeup Files/2.png">
</p>

Search the file according to its path.
```
vol.py -f memory.raw --profile=Win7SP1x64 filescan | grep -i "Comonn"
```  
<p align="center">
  <img src="Writeup Files/3.png">
</p>

The pdf file is renamed to the log5413741 in wrong path name. Dump it.
```
vol.py -f memory.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000007d681aa0 -n -D ./
```  
<p align="center">
  <img src="Writeup Files/4.png">
</p>

Open the pdf file. It is a presentation about the mathematic. Go to the end of file. There is a tiny url, Open it and download the image.  
<p align="center">
  <img src="Writeup Files/5.png">
</p>

The header of the png file is damaged. Correct it with a hex editor (Change the 25 to 89) and open it. It is the first part of the flag.  
<p align="center">
  <img src="Writeup Files/6.png">
</p>

Search important directories for the first part of the flag.
```
vol.py -f memory.raw --profile=Win7SP1x64 filescan | grep -i downloads
```  
<p align="center">
  <img src="Writeup Files/7.png">
</p>

Dump `I'm here.png`  
<p align="center">
  <img src="Writeup Files/8.png">
</p>

This image is inverted QR code. Invert and scan it. This gives us the second part of the flag.  
<p align="center">
  <img src="Writeup Files/9.png">
</p>

The flag:
```
TMUCTF{M@y8e_1_@M_6oOD_iN_ch3mI$7ry}
```
