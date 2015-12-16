// file: hw_06.h
// description: header file with all imported libraries, defined constants
// and function prototypes.

// make for each definition only occurs once
#ifndef HW_06_H
#define HW_06_H
  // include libraries
  #include <stdio.h>
  #include <stdlib.h>
  #include <strings.h>
  #include <unistd.h>
  #include <getopt.h>

  //declare byte read size
  #define BSIZE 1024

  // define functions prototypes
  void help();
  int read_signal(bool is_stdin , bool flag_i, bool flag_f, bool flag_n, char* fname);
#endif

//
// end file
