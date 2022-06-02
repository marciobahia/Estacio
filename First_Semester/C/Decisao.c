#include <stdio.h>

int main () {
int cadastrado, ativo, logado;
char opcao;

cadastrado = ativo = logado = 0;


printf("Deseja cadastrar sua conta? S/N \n");
scanf(" %c", &opcao);

if (opcao == 'S') {
    cadastrado = 1;
    printf("\nConta cadastrada. \n\n");
}

printf("Deseja ativar sua conta? S/N \n");
scanf(" %c", &opcao);

if (opcao == 'S') { 
    ativo = 1;
    printf("\nConta ativada.\n\n");
}

printf("Deseja logar? S/N \n");
scanf(" %c", &opcao);

if (opcao == 'S') {
    logado = 1;
    printf("\nConta logada.\n\n");
}
if ((cadastrado == 1) && (ativo == 1 ) && (logado == 1)){
    printf("\nSeja Bem Vindo!\n");
} else {
    printf("\nAlgo deu errado");
}

}
