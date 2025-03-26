// Write a program to read three integers from a file.

#include <stdio.h> 

int main() {
    FILE* ptr;
    int a , b , c;
    ptr = fopen("file.txt" , "r"); // Assuming file.txt exist with content as 3 number with space.

    fscanf(ptr , "%d" , &a);
    fscanf(ptr , "%d" , &b);
    fscanf(ptr , "%d" , &c);

    printf("%d %d %d" , a , b , c);

    fclose(ptr);

    return 0;
}