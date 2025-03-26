// Write a program to illustrate the use of arrow operator → in C.

#include <stdio.h>

struct myStruct
{
    char name[64];
    int age;
};


int main() {
    struct myStruct harshal;
    struct myStruct *harshal_ptr;

    harshal_ptr->age = 18;

    printf("%d", harshal_ptr->age);

    return 0;
}