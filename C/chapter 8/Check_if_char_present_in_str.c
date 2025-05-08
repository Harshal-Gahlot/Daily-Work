// Write a program to check whether a given character is present in a string or not.

#include <stdio.h>

int main () {
    char word[] = "harshal";
    char chr = 'r';
    int i = 0;
    int is_present = 0;

    while (word[i] != '\0') {
        if (word[i] == chr) {
            is_present = 1;
            break;
        }
        i++;
    }

    printf("%d", is_present);
    

    return 0;
}