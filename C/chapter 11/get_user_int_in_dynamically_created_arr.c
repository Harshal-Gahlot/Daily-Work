// Use the array in problem 1 to store 6 integers entered by the user.

#include <stdio.h>
#include <stdlib.h>

int main() {
    int length = 6;
    int* ptr;
    ptr = (int*)malloc(length * sizeof(int));

    if (ptr == NULL) {
        printf("memory allocation failed");
    }

    for (int i = 0; i < length; i++) {
        scanf("%d" , &ptr[i]);
    }

    for (int i = 0; i < length; i++) {
        printf("%d " , ptr[i]);
    }

    return 0;
}