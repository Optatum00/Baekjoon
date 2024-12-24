#include <stdio.h>

int main(){
    int N;
    int arr[101];
    scanf("%d", &N);
    for (int i=0;i<N;i++){
        scanf("%d",&arr[i]);
    }
    int v;
    scanf("%d", &v);
    int count = 0;
    for (int j=0;j<N;j++){
        if (v==arr[j]){
            count++;
        }
    }
    printf("%d", count);
}