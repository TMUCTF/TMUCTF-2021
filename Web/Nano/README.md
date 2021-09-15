# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Hint
The challenge name may be a good starting point for solving it.

# Writeup
In this challenge we are given a website. 
By looking at the different parts of it, the only information we get is in the `Flag` page where the path of the flag on the server is specified.
```
Flag is in /etc/ff3efa4307078c85678c6adee3b5f1b1af2ba16e/nanoflag/
```
<p align="center">
  <img src="Writeup Files/1.png">
</p>

Given the hint and the name of the challenge, we try to see if there are backups of website pages on the server.
This attempt is successful and we find the `index.html~` page which is a backup of the `index.html` page.
In the source code of the `index.html~` page, we find the following help, which is the starting point for solving this challenge:
```
This URI may help you: /801910ad8658876d56f5c8b24a563096.php
```
<p align="center">
  <img src="Writeup Files/2.png">
</p>

We open the `/801910ad8658876d56f5c8b24a563096.php` page. It contains the following PHP code:
```php
<?php
    $fp = fopen("/etc/tmuctf/another_flag_help.txt", "r");
    if($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['flag_help']) && strlen($_GET['flag_help']) <= 10) {
        include($_GET['flag_help']);
    }
    fclose($fp);
    echo highlight_file(__FILE__, true);
?>
```  
This PHP code indicates that the `/etc/tmuctf/another_flag_help.txt` file has been opened.
This code also shows that this page has a LFI (Local File Inclusion) vulnerability.
In this way, by placing a file in the `flag_help` variable and sending it through the GET request, the contents of that file are displayed.
The only limitation is that the total size of the path and the file name should not be more than 10 characters.
So we cannot open the flag file this way.  
Since the `/etc/tmuctf/another_flag_help.txt` file has been opened, we try to see its contents from the `/dev/fd/` path and by trying different identifiers.
Fortunately, we succeed and by entering `/dev/fd/10` in the `flag_help` variable, we can see the contents of the `/etc/tmuctf/another_flag_help.txt` file.
This file contains another help for us and guides us to the `/ffc14c6eb03e852ea2d2cbe18b3f4d76.php` page.
<p align="center">
  <img src="Writeup Files/3.png">
</p>

On the `/ffc14c6eb03e852ea2d2cbe18b3f4d76.php` page, it is possible to upload and extract the contents of zip files.
<p align="center">
  <img src="Writeup Files/4.png">
</p>

Given that and since we have the path of the flag, the first thing that comes to mind is the `Zip Slip` vulnerability.
Therefore, using the following commands, we create a symbolic link to the flag file and zip it:
```
ln -s "/etc/ff3efa4307078c85678c6adee3b5f1b1af2ba16e/nanoflag/flag.txt" symlink
zip --symlinks symlink.zip symlink
```  
We upload and extract the `symlink.zip` file.
Just because the directory listing is disabled, use the URL to open `symlink` file, and finally this file is opened and the flag is displayed.
<p align="center">
  <img src="Writeup Files/5.png">
</p>

The flag:
```
TMUCTF{Z1P_5l1p_15_4_D4n63r0u5_4rch1v3_3x7r4c710N_Vuln3r4b1l17Y___4nd_4_f0rm_0f_D1r3c70rY_7r4v3r54L!!}
```
