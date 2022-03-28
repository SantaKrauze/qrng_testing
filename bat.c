#include "gdef.h"
#include "swrite.h"
#include "bbattery.h"
#include <stdlib.h>
#include <stdio.h>

int count = 0;

unsigned int genFromFile(){

	FILE *fp;
	int c;
	int n = 0;

	int i =0;
	int bin[800000000];
	int bit;
  
	fp = fopen("qrng/QNGFile5.dat","r");
	if(fp == NULL) {
 		perror("Error in opening file");
		return(-1);
	} do {
		c = fgetc(fp);
		if( feof(fp) ) {
         		break ;
		}
		bin[i] = c;
		bit = bin[count];
		i++;

		//printf("%c", c);

	} while(i<=count);

	fclose(fp);
	return bit;
}

static double unixRand (){
	double r = random()/(RAND_MAX);
	return r;
}

int main (int argc, char *argv[]){
   if(argc < 3){
      printf("Too few arguments, provide path and string lenght");
   }
   swrite_Basic = TRUE;
   //bbattery_SmallCrushFile (argv[1]);
   unif01_Gen *gen;
   //for (int i =0; i<10; i++){
   //	   gen();
   //}
   gen = unif01_CreateExternGenBits("Binary File",genFromFile);
   bbattery_SmallCrush(gen);
   //bbattery_RabbitFile (argv[1], atoi(argv[2]));
   //bbattery_AlphabitFile (argv[1], atoi(argv[2]));
   //bbattery_FIPS_140_2File (argv[1]);
   unif01_DeleteExternGenBits(gen);
   return 0;
}
