// Create an array of multiplication table of 7 upto 10 (7 x 10 = 70). 
// Use realloc to make it store 15 number(from 7 x 1 to 7 x 15).

#include <stdio.h>
#include <stdlib.h>

int main() {
    int len = 10;
    int* arr = malloc(len * sizeof(int));

    for (int i = 1; i < len+1; i++) {
        arr[i] = i * 7;
        printf("%d ", arr[i]);
    }

    printf("\n");

    len = 15;
    arr = malloc(len * sizeof(int));

    for (int i = 1; i < len+1; i++) {
        arr[i] = i * 7;
        printf("%d ", arr[i]);
    }

    return 0;
}