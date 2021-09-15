#include <stdio.h>

static int state;

srand(seed) { 
    state = seed; 
  } 

rand() { 
    state = (state * 214013 + 2531011) & 0xFFFFFFFF; 
    return (state >> 16) & 0x7FFF; 
}

void main() {
    int n = 0;
    int var1, var2;
    int diff[6] = {895425380, 1848642222, 877650015, 813089424, 945746850, 926285019};
    char *ukey = "G7yTu83M";
    int *y = (int *)(ukey);
    srand(*y + 3 + *(y + 1) * 2);
    for (int i = 0; i <= 5; i++) {
        var2 = rand();
        printf("%x\n", var2 + diff[i]);
    }
}
