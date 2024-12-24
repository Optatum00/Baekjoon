#include <stdio.h>

int main() {
    int N, M;
    int i,j,k;
    scanf("%d %d",&N,&M);
    int A[101] = {0,};
    for (int a=0;a<M;a++){
        scanf("%d %d %d",&i,&j,&k);
        for (int a=i;a<=j;a++){
            A[a] = k;
        }
    }
    for (int a=1;a<=N;a++){
        printf("%d ", A[a]);
    }
    
    return 0;
}