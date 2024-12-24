#include <stdio.h>

int main() {
    int N;
    char C = '*';
    scanf("%d", &N);
    for (int i=0;i<N;i++){
        for (int j=i+1;j<N;j++){
            printf(" ");
        }
        for (int k=0;k<=i;k++){
            printf("%c", C);
        }
        printf("\n"); 
    }
    return 0;
}