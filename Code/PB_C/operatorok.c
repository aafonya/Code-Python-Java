#include <stdio.h>

int main() {
	int x = 0, y = 3;
	
	// értékadás: x új értéke legyen x régi értéke plusz 1!
	x = x + 1;
	printf("x = %d\n", x);
	
	// ugyanaz röviden: pre-inkrementálás: x új értéke legyen x régi értéke plusz 1!
	x++;
	printf("x = %d\n", x);
	
	// értékadás: add össze x-et és y-t, és az eredmény legyen x új értéke
 	x = x + y;
	printf("x = %d\n", x);
	
	// ugyanaz röviden: add össze x-et és y-t, és az eredmény legyen x új értéke
 	x += y;
	printf("x = %d\n", x);
	
	// értékadás: x = x*y;
	x *= y;
	printf("x = %d\n\n", x);
	
	
	// maradékos (modulo) osztás
	// a '%' kiíratásához írjunk két '%' jelet
	printf("10 %% 3 = %d\n", 10%3);
	printf("9 %% 6 = %d\n\n", 9%6);
	
	
	// preinkrementálás
	x = 0;
	printf("x = %d\n", x); // x értéke 0
	printf("x = %d (after x++)\n", x++); // előbb kiírja x értékét, majd emeli x-et
	printf("x = %d\n\n", x); // x értéke már 1
	
	// posztinkrementálás
	x = 0;
	printf("x = %d\n", x); // x értéke 0
	printf("x = %d (after ++x)\n", ++x); // előbb kiírja x értékét, majd emeli x-et
	printf("x = %d\n\n", x); // x értéke már 1
	
	return 0;
}

