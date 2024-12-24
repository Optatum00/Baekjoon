#include <stdio.h>

int main() {
    int a[6];
    int average;
    for (int i=0;i<5;i++){
        scanf("%d\n", &a[i]);
    }
    
    for (int i=0;i<5;i++){
        if(a[i]<40){
            a[i] = 40;
        }
    }
    
    average = (a[0]+a[1]+a[2]+a[3]+a[4])/5;
    printf("%d", average);

    return 0;
}