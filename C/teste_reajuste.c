#include <stdio.h>

int main() {

float reajuste, salario, salarioreaj, maior_salario;
int cont;
maior_salario=0;
printf("Digite o percentual de Reajuste: ");
scanf("%f", &reajuste);
for (cont=1;cont<=10;cont++) // se colocar ; dá erro
{
    printf("Informe o salário do Funcionário: ");
    scanf("%f",&salario);
    salarioreaj= salario+(salario*reajuste/100);
    printf("O Salário reajustado é : %.2f \n\n", salarioreaj);
    if (salarioreaj>maior_salario)
    maior_salario=salarioreaj;
}
printf("O Maior Salário reajustado é : %.2f", maior_salario);
return 0;

}