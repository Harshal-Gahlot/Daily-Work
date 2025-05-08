// Create a two-dimensional vector using structures in C.

#include <stdio.h>
#include <string.h>

struct two_dimensional_vector_structure
{
    int arr[5][3];
};

void sum_of_2d_vector(struct two_dimensional_vector_structure struct1 ,
    struct two_dimensional_vector_structure struct2) {
        struct two_dimensional_vector_structure ans;

        for (int i = 0; i < sizeof(struct1.arr)/4; i++)
        {
            for (int j = 0; j < sizeof(struct1.arr[0])/4; j++)
            {
                ans.arr[i][j] = struct1.arr[i][j] + struct2.arr[i][j];
                printf("%d ", ans.arr[i][j]);
            }
            printf("\n");
        }
}


int main() {

    struct two_dimensional_vector_structure myArr1;
    struct two_dimensional_vector_structure myArr2;
    int two_d[5][3] = { {1,2,3} ,{1,2,3},{1,2,3},{1,2,3},{1,2,3} };
    memcpy(myArr2.arr , two_d, sizeof(two_d));
    memcpy(myArr1.arr , two_d, sizeof(two_d));

    sum_of_2d_vector(myArr1 , myArr2);

    return 0;
}