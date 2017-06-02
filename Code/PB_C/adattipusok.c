#include <stdio.h>

int main () {
	//deklarálás
	int x, y, z = 3; // lehetséges közvetlenül a deklarációban értéket adni.
	double r = 2.5, s;
	char c = 'A';
	
	// inicializálás (értékadás, hozzárendelés)
	x = 1;
	y = 4;
	s = 1.5;
	
	// kiíratás
	printf("x = %d   y = %d   z = %d \n", x, y, z);
	printf("r = %f   s = %f \n", r, s);
	printf("c = %c \n", c);
	
	// Típuskonverzió
	// két 'int' összege, szorzata, hányadosa, stb. is 'int' típusú!
	printf("z/y = %d\n", z/y);
	//printf("%f\n", z/y); // ez nem működik, mert z/y eredménye 'int' típusú!
	printf("(double)z/y = %f\n", (double)z/y); // típuskonverzióval már jó lesz!
	printf("(double)z/y = %f\n", (double)z/y); // mindegy, hogy a számlálót vagy a nevezőt konvertáljuk!
	printf("(double)(z/y) = %f\n", (double)(z/y)); // ha a számot a művelet elvégzése UTÁN konvertáljuk, akkor a rossz értéket alakítjuk 'double' típussá!
	
	// ha legalább az egyik szám 'double' típusú, a típuskonverzió automatikus
	// nem kell konvertálnunk az 'int' típusú tagot
	printf("r/y = %f\n", r/y);
	printf("y/s = %f\n", y/s);
	
	return(0);
}
