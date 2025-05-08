// Write a program to dynamically create an array of size 6 capable of storing 6 integers.

#include <stdio.h>
#include <stdlib.h>

int main() {
    int length = 6;
    int* ptr;
    ptr = (int*)malloc(length * sizeof(int));

    ptr[0]=1;
    ptr[1]=2;
    ptr[2]=3;
    ptr[3]=4;
    ptr[4]=5;
    ptr[5]=6;

    printf("%d",ptr[5]);
    

    return 0;
}