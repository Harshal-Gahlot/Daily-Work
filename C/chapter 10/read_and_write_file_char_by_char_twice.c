// Write a program to read a text file character by 
// character and write its content twice in separate file.

#include <stdio.h>

int main() {
    FILE* fromf;
    FILE* tof;
    fromf = fopen("file.txt" , "r");
    tof = fopen("file2.txt" , "w");
    int chr = fgetc(fromf);
    /* although fgetc will return a char->letter/number/symbol, we init it as an int because of EOF.
    To recognize it correctly, we need to have int as datatype (-1), which especially can not
    happen in an unsigned char system. So, to avoid ambiguity, we just take it as an int, although we 
    treat it like a char. Similarly, fputc expects first argument as int which is like char */


    if (fromf == NULL || tof == NULL) {
        perror("Error opening file");
        return 1;
    }

    while (chr != EOF) {
        fputc(chr , tof);
        chr = fgetc(fromf);
    }

    rewind(fromf);

    while ((chr = fgetc(fromf)) != EOF) {
        fputc(chr , tof);
    }

    fclose(fromf);
    fclose(tof);


    return 0;
}