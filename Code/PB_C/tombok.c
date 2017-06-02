// Tömbök, vektorok, mátrixok
// Statikus tömbök

#	include <stdio.h>


int main ( ) {
	
  // definiáljunk egy egyszerű integer tömböt: minden ilyen ún. statikus tömbnél meg kell adnunk előre a hosszat, ami nem változhat a program futása során.
	int t[2]; // a tömb 2 értéket tartalmaz; a tömb hossza csak pozitív egész lehet
  // FIGYELEM! A C nyelv 0-tól kezdi a tömb indexálását, nem 1-től	
	t[0] = 1; // adjunk értéket a tömb első elemének (aminek az indexe 0)
	t[1] = 2;
	printf("t: [%d, %d]\n", t[0], t[1]);
	
	// Indexelhatunk 1-től is, de akkor nagyobb tömböt kell foglalnunk!
	int x[3]; // egy új, 3 hosszúságú tömb
	x[1] = 1; // kihagyjuk a 0 indexű (azaz első) elemet
	x[2] = 2;
	printf("x: [%d, %d]\n", x[1], x[2]);
	
	// mi történik, ha inicializálatlan tömb-elemet hivatkozunk meg?
	double y[10000]; 
	printf("y[99] = %f\n", y[4547]); // Ne bízzunk abban, hogy alapból mindenhol 0 van!!
	double yy[100] = { 0 }; // // MINDIG inicializáljuk a tömbjeinket (és változóinkat): ez a módszer 0-val tölti fel a tömböt
	printf("yy[99] = %f\n", yy[99]);
	
	
	// mi történik, ha túlcímezzük a tömböt?
	//printf("y[3] = %d\n", y[3]); // ezt a hibás sort a fordító le sem fordítja.
	
	// egyszerű inicializálás
	int z[4] = { 1, 2, 3, 4 };
	printf("y: [%d, %d, %d, %d] (forditva)\n", z[3], z[2], z[1], z[0]); // fordított sorrendben írjuk ki az elemeket
	
	// Egy tömb egyféle típusú adatot tartalmazhat csak
	double valos[5] = { 1.1, 2.5, 3, 'a', 100}; // csöndben minden típus valós számmá konvertálódik
	printf("valos: [%f, %f, %f, %f, %f]\n", valos[0], valos[1], valos[2], valos[3], valos[4]);
	// FIGYELEM! A karakter típus is egész, valójában a karakter ASCII számát kódolja.
	
		
	// Többdimenziós tömbnél mindegyik dimenzió mentén meg kell adni a tömb hosszát
	int multi[2][3] = {{ 1, 2, 3}, {4, 5, 6}}; // az első dimenzió a sorok, a második az oszlopok számát adja meg - de ez csak konvenció, nem szabály
	printf("%d %d %d\n%d %d %d\n", multi[0][0],  multi[0][1],  multi[0][2],  multi[1][0],  multi[1][1],  multi[1][2]);
	
		
		
	return(0);
}
