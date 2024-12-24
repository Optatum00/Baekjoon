#include <stdio.h>

int main() {
    int a[15] = {0,};
    int b[15] = {0,};
    int index;
    int result;
    for (int i=0;i<9;i++){
        scanf("%d", &a[i]);
    }
    for (int i=0;i<9;i++){
        b[i] = a[i];
    }
    for (int j=0;j<8;j++){
        if (a[j] < a[j+1]){
            a[j] = 0;
        }
        else if (a[j]==a[j+1]){
            continue;
        }
        else {
            a[j+1] = a[j];
            a[j] = 0;
        }
    }
    for (int j=0;j<9;j++){
        if (a[j] != 0){
            index = a[j];
            for (int i=0;i<9;i++){
                if (b[i] == index){
                    result = i+1;
                }
            }
            printf("%d\n", a[j]);
            printf("%d", result);
        }
    }
}