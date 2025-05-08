// Write a program to generate multiplication table of a given number 
// in text format.Make sure that the file is readable and well formatted.

#include <stdio.h>

int main() {
    int n = 5;
    FILE* ptr;
    ptr = fopen("file.txt" , "w");

    for (int i = 1; i < 11; i++) {
        fprintf(ptr , "%d X %d = %d\n" , n , i , n * i);
    }
    
    fclose(ptr);

    return 0;
}