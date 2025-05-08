#include <stdio.h>
// #include <stdlib.h>

void cpy(char arr1[] , char arr2[]) {
    int i = 0;
    while (arr2[i] != '\0') {
        arr1[i] = arr2[i];
        i++;
    }
    arr1[i] = '\0';
}

int main() {

    char arr1[] = "not done";
    char arr2[] = "done";
    cpy(arr1 , arr2);
    printf("arr1: %s\n" , arr1);
    return 0;
}