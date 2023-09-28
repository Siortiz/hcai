#include <stdio.h>
int main(){
	// C nos permite definir tipos de variables:
	int var;
	// Si la imprimimos, nos mostrará lo que tenía la RAM al momento de ejecutar:
	printf("%d\n", var);
	// Toda variable debe ser inicializada.
	var=0;
	printf("%d\n", var);
	// Esto se puede hacer en una línea:
	int var1 = 1;
	printf("%d\n", var1);
}
