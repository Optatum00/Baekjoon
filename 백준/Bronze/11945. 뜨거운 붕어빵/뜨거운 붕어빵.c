#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    char fish[N][M];
    for (int i=0;i<N;i++){
        scanf("%s", fish[i]);            
    }
    for (int j=0;j<N;j++){
        for (int k=M-1;k>=0;k--){
            printf("%c", fish[j][k]);
        }
        printf("\n");
    }
    return 0;
}