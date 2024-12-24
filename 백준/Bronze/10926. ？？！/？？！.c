#include <stdio.h>
#include <string.h>

int main(){
    char A[51];
    char B[100] = "??!";
    scanf("%s", A);
    strcat(A, B);
    printf("%s", A);
    
    return 0;
}