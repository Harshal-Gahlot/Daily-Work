// Create an array of 5 complex numbers created in Problem 5 and display them with
// the help of a display function.The values must be taken as an input from the user.

#include <stdio.h>

typedef struct complex_number
{
    int a;
    int b;
} complex;


int main() {
    complex c1 = { 2, 3 };

    complex c2;
    complex* c2ptr = &c2;
    scanf("%d" , &c2ptr->a);
    scanf("%d" , &c2ptr->b);

    printf("%d %di\n" , (&c1)->a , (&c1)->b);
    printf("%d %di\n" , c2ptr->a , c2ptr->b);

    return 0;
}