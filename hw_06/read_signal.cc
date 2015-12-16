// read_signal.cc
// description: this file contains a function that reads a raw data file and
// and prints the data to standard output.
//

// include hw_06 header file
#include "hw_06.h"

// function: read_signal
// arguments: bool is_stdin, flag_i, flag_f, flag_n, char* fname (filename)
// return: 0 for successful execution
//
int read_signal(bool is_stdin , bool flag_i, bool flag_f, bool flag_n, char* fname){
  // declare file pointer
  FILE *fp;

  // check if file is from standard input using cat
  if (is_stdin == true) {
    fp = stdin;
  }
  // else read from file
  else {
    is_stdin = false;
    fp = fopen(fname,"r");
  }

  // number of samples read
  long nsamples_read;

  // declare short int and float arrays BSIZE long
  short int si_buf[BSIZE];
  float f_buf[BSIZE];

  // check i flag, if true then read from stdin
  if (flag_i == true){
    // read while there is data
    while ( (nsamples_read = fread(si_buf, sizeof(short int), BSIZE, fp)) > 0){
      // check n flag, if true print line numbers
      if (flag_n == true) {
        for (int i = 0; i < nsamples_read; i++) {
          fprintf(stdout, "%07d: [%hi]\n", i, si_buf[i]);
        } // end for loop
      } // end if

      // no line numbers
      else{
        for (int i = 0; i < nsamples_read; i++) {
          fprintf(stdout, "[%hi]\n", si_buf[i]);
        } // end for loop
      } // end else
    } // end while loop
  } // end if

  // if flag_i is false
  else{
    // read from file
    while ( (nsamples_read = fread(f_buf, sizeof(float), BSIZE, fp)) > 0){
      // if flag_n is true print line numbers
      if (flag_n == true) {
        for (int i = 0; i < nsamples_read; i++) {
          fprintf(stdout, "%07d: [%f]\n", i, f_buf[i]);
        } // end for loop
      }//end if
      // no line numbers
      else{
        for (int i = 0; i < nsamples_read; i++) {
          fprintf(stdout, "[%f]\n", f_buf[i]);
        } // end for loop
      }// end else
    } // end while loop
  } // end else

  // close file
  if (is_stdin == false) {
    fclose(fp);
  }

  return 0;
} // end read_signal

//
// end file
