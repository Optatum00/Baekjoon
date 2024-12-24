#include <stdio.h>
int main(){
    int A[10001];
    int N, X;
    scanf("%d %d", &N, &X);
    int i;
    for (i=0; i<N ;i++){
        scanf("%d", &A[i]);
    }
    for (int j=0;j<N;j++){
        if (A[j]<X){
            printf("%d ", A[j]);
        }
    }
    return 0;
}