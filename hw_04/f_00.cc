#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// declare ece_3822_add_sin
float ece_3822_add_sin(float x, float y);

// main program: calls ece_3822_add_sin and prints hello world.
int main(){
  float sum_sine;
  float x = M_PI/6;
  float y = M_PI/6;
  sum_sine = ece_3822_add_sin(x,y);
  printf("hello world\n");
  printf("sum of sin(x) and sin(y) is %f.\n",sum_sine);
  
  return 0;
}
