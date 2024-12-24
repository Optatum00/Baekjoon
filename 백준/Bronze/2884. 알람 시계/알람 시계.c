#include <stdio.h>

int main() {
    int H, M;
    scanf("%d %d", &H, &M);
    if (H == 0){
        if (M >= 45) {
            H = 0;
            M -= 45;
        }
        else if (H == 0 && M < 45) {
            H = 23;
            M += 15;
        }
    }
    else{
        if (M >= 45){
            M -= 45;
        }
        else if (H > 0 && M < 45){
            H -= 1;
            M += 15;
        }
    }
    printf("%d %d", H, M);
}