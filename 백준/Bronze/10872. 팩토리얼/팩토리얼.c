#include <stdio.h>

int main(){
    int n;
    int j=1;
    scanf("%d", &n);
    if (n==0){
        j = 1;
    }
    else{
        for (int i=1; i<=n; i++){
        j *= i; 
    }
    }
    printf("%d", j);
}