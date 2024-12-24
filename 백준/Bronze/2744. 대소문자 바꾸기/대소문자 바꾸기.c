#include <stdio.h>
#include <string.h>

int main() {
    char n[100];
    scanf("%s", n);
    for (int i=0; i<strlen(n); i++){
        if (n[i]<=90){
            n[i]=n[i]+32;
        }
        else{
            n[i]=n[i]-32;
        }
    }
    printf("%s", n);

    return 0;
}