#include <stdio.h>

int a[42];

int main(){
    int N;
    int count = 0;
    for (int i=0; i<10; i++){
        scanf("%d", &N);
        a[N%42]++;    
    }
    for (int j=0; j<42; j++){
        if (a[j] != 0){
            count++;
        }
    }
    printf("%d", count);
    return 0;
}