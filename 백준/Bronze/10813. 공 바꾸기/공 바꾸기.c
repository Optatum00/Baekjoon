#include <stdio.h>

int main(){
    int N, M;
    int i, j, k;
    int A[101] = {0,};
    int temp[101] = {0,};
    scanf("%d %d", &N, &M); 
    for (int k=1;k<=N;k++){
        A[k] = k; //처음에 for문 변수 i로 잡아놨는데 안고쳐놔서 틀림 변수 통일 확실히하기!
    }
    for (k=0;k<M;k++){
        scanf("%d %d", &i, &j);
        temp[i] = A[i];
        temp[j] = A[j];
        A[i] = temp[j];
        A[j] = temp[i];
    }
    for (k=1;k<=N;k++){
        printf("%d ", A[k]);
    }
    return 0;
}