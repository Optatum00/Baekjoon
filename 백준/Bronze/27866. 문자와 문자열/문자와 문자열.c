#include <stdio.h>
int main()
{
    char s[1001];
    scanf("%s\n", s);
    int i;
    scanf("%d", &i);
    printf("%c", s[i - 1]);
    return 0;
}