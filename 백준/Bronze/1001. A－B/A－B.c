#include <stdio.h>

int SUBSTRACT(int a, int b){
    int result = a - b;
    return result;
}

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    printf("%d",SUBSTRACT(A,B));
}