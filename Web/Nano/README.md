# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Hint
The challenge name may be a good starting point for solving it.

# Writeup
In this challenge we are given a website.
By looking at the different parts of it, the only information we get is in the flag page where the path if flag on the server is specified.
Flag page of index.html ===>>> Flag is in /etc/ff3efa4307078c85678c6adee3b5f1b1af2ba16e/nanoflag/

Given the hint and the name of the challenge, we try to see if there is backup of website pages on the server.
This attempt is successful and we find the index.html~ page which is a backup of the index.html page.
In the source code of the index.html~ page, we find the following help, which is the starting point for solving this challenge:
This URI may help you: /801910ad8658876d56f5c8b24a563096.php

We open the /801910ad8658876d56f5c8b24a563096.php page.
The PHP code on this page indicates that the /etc/tmuctf/another_flag_help.txt file has been opened.
This code also indicates that this page has a LFI vulnerability.
In this way, by placing a file in the flag_help variable and sending it through the GET request, the contents of that file are displayed.
The only limitation is that the total size of the path and the file name should not be more than 10 characters.
So we can not open the flag file this way.
Since the /etc/tmuctf/another_flag_help.txt file has been opened, we try to see its contents from the /dev/fd/ path and by trying different identifiers.
Fortunately, we succeed and by entering /dev/fd/10 in the flag_help variable, we can see the contents of the /etc/tmuctf/another_flag_help.txt file.
This file contains another help for us and guides us to the following page:
/ffc14c6eb03e852ea2d2cbe18b3f4d76.php

On this page, it is possible to upload and extract the contents of zip files.
Given that and since we have the path of the flag, the first thing that comes to mind is the Zip Slip Vulnerability.
Therefore, using the following commands, we create a symbolic link to the flag file and zip it:
ln -s "/etc/ff3efa4307078c85678c6adee3b5f1b1af2ba16e/nanoflag/flag.txt" symlink
zip --symlinks symlink.zip symlink

We upload and extract the symlink.zip file.
Just because the directory listing is disabled, use the URL to open it, and finally this file is opened and the flag is displayed.
