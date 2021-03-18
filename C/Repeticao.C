#include <stdio.h>
#include <stdlib.h>


int main () 
{
    int num, cont;
    printf("Digite um número:");
    scanf("%d", &num);
    for (cont=1; cont<=20; cont=cont+1)
{
    printf("\n Número = %d", num);
}
return 0;
}
