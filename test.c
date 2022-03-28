#include "gdef.h"
#include "swrite.h"
#include "bbattery.h"
#include <stdlib.h>
#include <stdio.h>

int count = 0;

int main(){

	FILE *fp;
	int c;
	int n = 0;

	int i =0;
	int bin[800000];
	int bit;
  
	fp = fopen("qrng/QNGFile5.dat","rb");
	if(fp == NULL) {
 		perror("Error in opening file");
		return(-1);
	} do {
		c = fgetc(fp);
		if( feof(fp) ) {
         		break ;
		}
		bin[i] = c;
		bit = bin[i];
		i++;

		printf("%d", bin[i]);

	} while(i<1000);
	count++;
	fclose(fp);
	return 0;
}
