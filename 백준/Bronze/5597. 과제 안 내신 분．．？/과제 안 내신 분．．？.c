#include <stdio.h>

int a[31];

int main(){
    int N;
    for (int i=1;i<=30;i++){
        scanf("%d",&N);
        a[N]++;
    }
    for (int i=1;i<=30;i++){
        if(a[i] == 0){
            printf("%d\n", i);
        }
    }
}