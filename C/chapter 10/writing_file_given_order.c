/* Take name and salary of two employees as input from the
user and write them to a text file in the following format:
Name1, 3300
Name2, 7700
*/

#include <stdio.h>

int main() {
    int salary1, salary2;
    char name1[32], name2[32];
    
    scanf("%s", name1);
    scanf("%d", &salary1);
    scanf("%s", name2);
    scanf("%d", &salary2);

    FILE* ptr;
    ptr = fopen("file.txt", "w");

    fprintf(ptr, "%s, %d\n" , name1 , salary1);
    fprintf(ptr, "%s, %d" , name2 , salary2);
    
    fclose(ptr);
    printf("%s, %d\n" , name1 , salary1);
    printf("%s, %d" , name2 , salary2);

    return 0;
}