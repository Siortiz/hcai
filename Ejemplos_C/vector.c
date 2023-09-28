#include <stdio.h>
#include <stdlib.h>

int main()
{
	//Así definimos nuestro array:
	int contador[10];
	//Ahora lo inicializamos:
	for (int i=0; i<10; i++)
		contador[i] = i;
	// Mostremos sus elementos en stdout:
	for (int i=0; i<10; i++)
                printf("contador[%d] = %d\n", i, contador[i]);

	return 0;
}

