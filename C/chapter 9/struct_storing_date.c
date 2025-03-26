// Write a structure using typedef capable of storing date. Write a function to compare those dates.

#include <stdio.h>

typedef struct date
{
    int date;
    int month;
    int year;
} date;

date dateCompare(date d1 , date d2) {
    if (d1.year > d2.year) {
        return d1;
    } else if (d1.year < d2.year) {
        return d2;
    } else if (d1.month > d2.month) {
        return d1;
    } else if (d1.month < d2.month) {
        return d2;
    } else if (d1.date > d2.date) {
        return d1;
    } else if (d1.date < d2.date) {
        return d2;
    } else {
        return d1;
    }

}

int main() {
    date d1 = { 26,3,2025 };
    date d2 = { 15,5,2024 };



    printf("%d %d %d\n" , d1.date , d1.month , d1.year);
    printf("%d %d %d\n" , d2.date , d2.month , d2.year);

    printf("%d %d %d", dateCompare(d1, d2));

    return 0;
}