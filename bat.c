#include "gdef.h"
#include "ulcg.h"
#include "ulec.h"
#include "swrite.h"
#include "bbattery.h"
#include <stdlib.h>
#include <stdio.h>
#include "ufile.h"

//int count = 0;

int main (int argc, char *argv[]){
   if(argc < 3){
      printf("Too few arguments, provide path and string lenght");
   }

   if (atoi(argv[3]) == 1) swrite_Basic = TRUE;
   else swrite_Basic = FALSE;
   
   int buff = atoi(argv[2]);

   /*
   unif01_Gen* gen;
   gen = ulec_CreateMRG32k3a (123., 123., 123., 123., 123., 123.);
   
   bbattery_Rabbit(gen,buff);
   bbattery_Alphabit(gen,buff,0,32);
   bbattery_FIPS_140_2(gen);

   ulec_DeleteGen (gen);

   gen = ulcg_CreateLCGFloat (2147483647, 16807, 0, 12345);
   
   bbattery_Rabbit(gen,buff);
   bbattery_Alphabit(gen,buff,0,32);
   bbattery_FIPS_140_2(gen);

   ulcg_DeleteGen (gen);
   */
   bbattery_RabbitFile (argv[1], atoi(argv[2]));
   bbattery_AlphabitFile (argv[1], atoi(argv[2]));
   bbattery_FIPS_140_2File (argv[1]);
   return 0;
}
