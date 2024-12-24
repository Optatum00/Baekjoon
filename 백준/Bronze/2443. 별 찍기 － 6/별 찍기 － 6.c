#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    for (int i=N;i>0;i--){
        for (int m=N;m>i;m--){
            printf(" ");
        }
        for (int j=1;j<=2*i-1;j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}