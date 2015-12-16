#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// this function returns the sum of the sine of each value.
float ece_3822_add_sin(float x, float y){
  float sinx = sin(x);
  float siny = sin(y);
  printf("sin(x) = %f\n", sinx);
  printf("sin(y) = %f\n", siny);
  float sum = sinx + siny;
  return sum;
}
