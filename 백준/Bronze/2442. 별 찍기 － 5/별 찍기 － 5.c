#include <stdio.h>

int main(void){
    int count;
    scanf("%d", &count);
    for (int i=0; i<count; i++){
        for (int j=i; j<count-1; j++){
            printf(" ");
        }
        for (int k=i; k<3*i+1; k++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}