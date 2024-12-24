#include <stdio.h>

int main(){
    int N, M, K;
    int row1, column1, row2, column2;
    int total[10001];
    int A[301][301] = {0,};
    scanf("%d %d", &N, &M);
    for (int i=1;i<=N;i++){
        for(int j=1;j<=M;j++){
            scanf("%d ", &A[i][j]);
        }
    }
    scanf("%d", &K);
    for (int m=0;m<K;m++){
        scanf("%d %d %d %d", &row1, &column1, &row2, &column2);
        if (row1==row2){
            if (column1==column2){
                total[m] = A[row1][column1];
            }
            else {
                for (int n=column1;n<=column2;n++){
                    total[m] += A[row1][n];
                }
            }
        }
        else {
            if (column1==column2){
                for (int n=row1;n<=row2;n++){
                    total[m] += A[n][column1];
                }
            }
            else {
                for (int n=row1;n<=row2;n++){
                    for (int r=column1;r<=column2;r++){
                        total[m] += A[n][r];
                    }
                }
            }
        }
    }
    for (int y=0;y<K;y++){
        printf("%d\n", total[y]);
    }  
}