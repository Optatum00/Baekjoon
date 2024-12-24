#include <stdio.h>

int main(){
    int N, M;
    scanf("%d %d", &N, &M);
    int map[N][M];
    int map1[N][M];
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            scanf("%d",&map[i][j]);
        }
    }
    for (int m=0;m<N;m++){
        for (int n=0;n<M;n++){
            scanf("%d",&map1[m][n]);
        }
    }
    int total[N][M];
    for (int a=0;a<N;a++){
        for (int b=0;b<M;b++){
            total[a][b] = map[a][b]+map1[a][b];
        }
    }
    for (int a=0;a<N;a++){
        for (int b=0;b<M;b++){
            printf("%d ",total[a][b]);
        }
        printf("\n");
    }
    
}