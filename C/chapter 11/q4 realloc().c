// 4. Create an array dynamically capable of storing 5 integers. 
// Now use realloc so that it can now store 10 integers.

#include <stdio.h>
#include <stdlib.h>

int main() {
    int len = 5;
    int* ptr = (int*)calloc(len , sizeof(int));

    if (ptr == NULL) {
        printf("ptr didn't init");
    }

    for (int i = 0; i < len; i++) {
        ptr[i] = i;
    }

    for (int i = 0; i < len; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    len = 10;
    ptr = realloc(ptr , len * sizeof(int));

    for (int i = 0; i < len; i++) {
        ptr[i] = i;
    }

    for (int i = 0; i < len; i++) {
        printf("%d " , ptr[i]);
    }

    return 0;
}