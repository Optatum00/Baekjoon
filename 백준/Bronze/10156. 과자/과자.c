#include <stdio.h>

int main() {
    int K, N, M;
    scanf("%d %d %d", &K, &N, &M);
    int result = K * N - M;
    if(result >= 0){
        printf("%d", result);
    }
    else{
        printf("%d", 0);
    }
    
    return 0;
}