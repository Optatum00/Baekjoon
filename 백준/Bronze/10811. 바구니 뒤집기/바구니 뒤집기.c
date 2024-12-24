#include <stdio.h>

int main(){
    int N, M;
    int i, j, x;
    scanf("%d %d", &N, &M);
    int A[N+1];
    for(int a=1;a<=N;a++){
        A[a] = a;
    }
    for(int k=1;k<=M;k++){
        scanf("%d %d", &i, &j);
        int cnt = 0;
        while(i + cnt <= j - cnt){
            x = A[j - cnt];
            A[j - cnt] = A[i + cnt];
            A[i + cnt] = x;
            cnt++;
        }
    }
    for(int c=1;c<=N;c++){
        printf("%d ", A[c]);
    }
    return 0;
}