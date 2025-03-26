// Write a program to read three integers from a file.

#include <stdio.h> 

int main() {
    FILE* ptr;
    ptr = fopen("file.txt" , "r");
    int a , b , c;

    fscanf(ptr , "%d" , &a);
    fscanf(ptr , "%d" , &b);
    fscanf(ptr , "%d" , &c);

    printf("%d %d %d" , a , b , c);

    fclose(ptr);

    return 0;
}