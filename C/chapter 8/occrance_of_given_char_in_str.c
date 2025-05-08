// Write a program to count the occurrence of a given character in a string.

#include <stdio.h>

int main () {
    char word[] = "harshal";
    char chr = 'a';
    int i = 0;
    int count = 0;

    while (word[i] != '\0') {
        if (word[i] == chr) {
            count++;
        }
        i++;
    }

    printf("%d", count);    

    return 0;
}