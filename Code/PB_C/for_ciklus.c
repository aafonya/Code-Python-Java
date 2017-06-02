// For ciklus
// adott számú iterációt vérehajtó ciklus

// for(kezdés; teszt; lépés) parancs

// vagy

// for(kezdés; teszt; lépés) {
//		parancs1;
//    parancs2;
//  	...
// }

// A 'for' ciklus elsőként végrehajtja a 'kezdés'-t. Ezután kiértékeli a 'teszt'-et: ha 'teszt' hamis, akkor a ciklus megáll, és a program futása a 'parancs' után folytatódik. Ha a 'teszt' igaz, akkor 'parancs' végrehajtódik. Végül a ciklus végrehajtja a 'lépés'-t, majd a ciklus küvetkező ismétlése kezdődik meg, 'teszt' kiértékelésével.


#include <stdio.h>


int main ( ) {
	int a[10] = { 4, 2, 6, 3, 4, 1, 6, 9, 8, 7 };
	int i;
	
	
	// Példa: Írassuk ki az első 10 egész számot!
	int n;
	for (n = 0; n < 10; n++) printf("%d ", n);
	printf("\n");
	
	
	
	// Írassuk ki az 'a' tömb elemeit!
	for(i = 0; i < 10; i++) {
		printf("a[%d]=%d\n", i, a[i]);
	}
	printf("\n");
	
	
	// Másoljuk át 'a' tömb elemeit 'b' tömb megfelelő elemeibe
	int b[10]; // deklaráljuk 'b'-t ugyanakkorának, mint 'a'
	for(i = 0; i < 10; i++) {
		b[i] = a[i];
		printf("a[%d] = %d   b[%d] = %d\n", i, a[i], i, b[i]);
	}
	printf("\n");
	
	
	// vektor szorzása skalárral: szorozzuk be a tömb elemeit egy egész számmal, és tároljuk el 'c'-ben
	int skalar = 10;
	int c[10] = { 0 };
	for(i = 0; i < 10; i++) c[i] = a[i] * skalar;
	printf("c[...] = ");
	for(i = 0; i < 10; i++) printf("%d ", c[i]);
	printf("\n");
	
	
	// Adjuk össze az 'a' tömb elemeit
	int sum = 0;
	for(i = 0; i < 10; i++) sum = sum + a[i];
	printf("osszeg: %d\n", sum);
	
	
	// Ugyanez, inkrements hozzárendeléssel (+=)
	sum = 0;
	for(i = 0; i < 10; i++) sum += a[i];
	printf("osszeg: %d\n", sum);
	
	
	// Szorozzuk össze az 'a' tömb elemeit
	// Figyelem! Ha a tömbben van 0, akkor a szorzat is 0 lesz!
	int szorzat = 1;
	for(i = 0; i < 10; i++) szorzat *= a[i];
	printf("osszeg: %d\n", szorzat);
	
	

	
	return(0);
}
