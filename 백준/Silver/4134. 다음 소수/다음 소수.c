#include <stdio.h>
#include <math.h>
int primeNum(long n) {
    int max = sqrt(n);
    for(int i = 2;  i <= max; i++) {
        if(n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(){
    int T;
    scanf("%d", &T);
    
    for(int i = 0; i < T; i++) {
        long N;
        scanf("%ld", &N);
        while(1) {
            if(N == 0 || N == 1) {
                printf("2\n");
                break;
            }
            if(primeNum(N) == 1) {
                printf("%ld\n", N);
                break;
            }
            N++;
        }
    }
    return 0;
}