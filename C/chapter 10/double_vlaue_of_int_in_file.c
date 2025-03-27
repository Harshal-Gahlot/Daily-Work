// Write a program to modify a file containing an integer to double its value.

#include <stdio.h>

int main() {
    FILE* ptr;
    ptr = fopen("file.txt" , "r+");

    int num;
    int chr = fscanf(ptr , "%d" , &num);
    rewind(ptr);
    fprintf(ptr , "%d" , (num * 2));

    fclose(ptr);

    return 0;
}