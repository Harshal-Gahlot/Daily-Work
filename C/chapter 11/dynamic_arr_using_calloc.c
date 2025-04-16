// 3. Write a program using calloc() to dynamically create an array of size 6 capable of storing 6 integers.

#include <stdio.h>
#include <stdlib.h>

int main() {
    int length = 6;
    int* arr = (int*)calloc(length , sizeof(int));

    if(arr == NULL) {
        printf("arr not initalized, error");
    }

    for (int i = 0; i < length; i++) {
        scanf("%d", &arr[i+1]);
    }

    for (int i = 0; i < length; i++) {
        printf("%d " , arr[i]);
    }

    return 1;
}

