// Write a program to encrypt a string by adding 1 to the ascii value of its characters.

#include <stdio.h>

int main()
{
    char word[] = "Harshal";
    char encrypt[] = "";
    int i = 0;

    while (word[i] != '\0') {
        encrypt[i] = word[i] + 1;
        i++;
    }
    encrypt[i] = '\0';

    printf("%s" , encrypt);

    return 0;
}
