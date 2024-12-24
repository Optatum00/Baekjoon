#include <stdio.h>

int main() {
    int C, N;
    scanf("%d\n", &C);
    int A[1001];
    double avg[1001];
    double result[1001];
    
    for (int k=1;k<=C;k++){
        scanf("%d", &N);
        for (int i=1;i<=N;i++){
            scanf("%d", &A[i]);
            avg[k] = (avg[k] + A[i]);
        }
        avg[k] = avg[k]/N;
        double cnt = 0;
        for (int j=1;j<=N;j++){
            if (avg[k]<A[j]){
            cnt += 1;
            }
        }
        result[k] = cnt/N*100;
    }
    for (int m=1;m<=C;m++){
        printf("%.3lf%\n", result[m]);
    }
}
