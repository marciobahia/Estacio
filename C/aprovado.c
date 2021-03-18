#include <stdio.h>

int main()
{
float nota1,nota2,nota3,media;
int contalunos;
for (contalunos=1;contalunos<=40;contalunos++)
{
printf("Entre com a nota 1 do aluno: ");
scanf("%f",&nota1);
printf("\n Entre com a nota 2 do aluno: ");
scanf("%f",&nota2);
printf("\n Entre com a nota 3 do aluno: ");
scanf("%f",&nota3);
media=(nota1+nota2+nota3)/3;
if (media>=7)
{
printf("Aluno APROVADO com média : %.2f",media);
}
else
{
printf("\nAluno REPROVADO com média : %.2f\n",media);
}
}
return 0;
}