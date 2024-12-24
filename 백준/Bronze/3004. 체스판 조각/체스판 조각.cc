#include <stdio.h>

int main(){
    int count, N;
    scanf("%d", &count);
    if (count%2 == 0){
        N = (count/2+1)*(count/2+1);
    }
    else{
        N = (count/2+1)*(count/2+2);
    }
    printf("%d",N);
}