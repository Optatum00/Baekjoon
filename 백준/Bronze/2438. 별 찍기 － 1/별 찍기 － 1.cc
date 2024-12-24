#include <stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    char k = '*';
    for(int j = 1; j <= n; j++){
        for (int i = 0; i < j; i++){
            printf("%c", k);
        }
        printf("\n");
    }
}