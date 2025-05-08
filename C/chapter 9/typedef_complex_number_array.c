// Create an array of 5 complex numbers created in Problem 5 and display them with
// the help of a display function.The values must be taken as an input from the user.

#include <stdio.h>

typedef struct complex_number
{
    int a;
    int b;
} complex;

void displayComplex(complex c) {
    printf("%d %di\n" , c.a , c.b);
}

void displayComplexArray(complex arr[]) {
    for (int i = 0; i < 5; i++) {
        displayComplex(arr[i]);
    }
    
}

int main() {

    complex c1;
    complex* c1ptr = &c1;
    scanf("%d" , &c1ptr->a);
    scanf("%d" , &c1ptr->b);

    complex c2 = { 1, 2 };
    complex c3 = { 3, 4 };
    complex c4 = { 5, 6 };
    complex c5 = { 7, 8 };

    complex arr[5] = {c1, c2, c3, c4, c5};

    displayComplexArray(arr);

    // displayComplex(c1);
    // displayComplex(c2);
    // printf("%d %di\n" , c1ptr->a , c1ptr->b);
    // printf("%d %di\n" , (&c2)->a , (&c2)->b);

    return 0;
}