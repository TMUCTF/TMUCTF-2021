# Challenge Description
<p align="center">
  <img src="Challenge.png">
</p>
<br>

# Writeup
In this challenge a 64-bit ELF file is given. Run the file and see that it first asks us for a key. Decompile the file with Ghidra or IDA Pro.  
By analyzing the code, we find that this is a two-factor authentication program that first takes the key and then, if the key is correct, takes the password from the user. 
If the password is also correct, we must enter a secret correctly and get the flag.  
A closer look at the program reveals that the key entered by the user is compared to the main key in the `verify` function. 
Carefully in the `verify` function we see that the user key and the main key characters are compared one by one in a loop and as soon as the first incorrect character is reached, an error message is printed. 
Due to the fact that there is a one-second `sleep` call in each round of the loop, it is possible to determine whether the entered key characters are correct or incorrect by calculating the time that the error message is printed. 
This type of timing attacks is called `side channel` attacks. The solution code for this part of the challenge is available in solve_part1.py.

G7yTu83M


After entering the correct value of the key, we must enter the password.
Carefully in the code we see that the password is evaluated in the factor2 function.
The factor2 function generates a number of random numbers.
Since the value of seed is fixed and obtained from the key (we have the key in this step), so by fixing seed, we can get random numbers and simply invert the function and obtain the password.
The solution code for this part of the challenge is available in solve_part2.c.

50_57R0nG_P455w02d_83467


In the third part of the challenge, you must enter a secret message to get the flag.
To see how to solve this part, refer to the collision challenge.
