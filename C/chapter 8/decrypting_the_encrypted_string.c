// Write a program to decrypt the string encrypted using encrypt programme.

#include <stdio.h>

int main() {

    char encryped[] = "Ibstibm";
    char decryped[] = "";
    int i = 0;

    while (encryped[i] != '\0') {
        decryped[i] = encryped[i]-1;
        i++;
    }
    
    decryped[i] = '\0';

    printf("%s", decryped);

    return 0;
}