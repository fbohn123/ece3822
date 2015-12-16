// file: main.cc
// description: this is the main program, it prints out the sampls in a raw data file
//

// include header file
#include "hw_06.h"

// structure to handle the long options
static struct option long_options[] = {
  //
  {"numbers", no_argument, 0 ,'n'},
  {"no",      no_argument, 0, 'n'},
  {"help",    no_argument, 0, 'h'},
  {"float",   no_argument, 0, 'f'},
  {"int",     no_argument, 0, 'i'},
  {0,         0,           0,   0}
};

// main program
// arguments: command line arguments
// return: 0 for successful execution
//
int main(int argc, char** argv){
  // declare file name
  char* fname;

  // initialize counter for the number of options
  int count_opt = 0;

  // initialize counter for the number of file
  int count_files = 0;

  // initialize flags
  bool is_stdin;       // flag to check std input
  bool flag_i = true;  // flag for option i (on by default)
  bool flag_f = false; // flag for option f
  bool flag_n = false; // flag for option n

  // declare command line parsing variables
  int opt;
  int option_index = 0;

  // if no files then print the help
  if (argc == 1) {
    help();
    exit(EXIT_FAILURE);
  }

  // parse the command line arguments for the options
  while ((opt = getopt_long(argc, argv, "fihn", long_options, &option_index)) != -1) {
    switch (opt) {
      // interpret the data as 16-bit integers
      case 'i':
        // on by default
        break;

      // interpret the data as 4-byte floating point numbers
      case 'f':
        flag_i = false;
        flag_f = true;
        break;

      // display line numbers
      case 'n':
        flag_n = true;
        break;

      // help function
      case 'h':
      help();
      exit(EXIT_FAILURE);

      // otherwise
      default:
        fprintf(stderr, "Usage: %s [-h -n -f -i] [file...]\n", argv[0]);
        exit(EXIT_FAILURE);
    }
  }// end while loop

  // loop through every command line argument and count the number of options
  // and files
  for (int i = 1; i < argc; i++) {
    // if true then the argument is an option
    if (strncmp(argv[i],"-",1) == 0) {
      // count the number of characters after a dash
      // increment the number of options
      count_opt+=1;
    }
    // otherwise it is a file
    else{
      // increment the number of files
      count_files+=1;
    }
  }// end for loop

  // if there is no files then check stdin
  if (count_files == 0) {
    is_stdin = true;
    fname = NULL;
    // call function read_signal
    read_signal(is_stdin, flag_i, flag_f, flag_n, fname);
  }
  else{
    is_stdin = false;
    // loop over every file name
    for (int j = count_opt + 1; j < argc; j++) {
      fname = argv[j];
      // check if file exist
      if (fopen(fname,"r") != NULL) {
        // call function read_signal
        read_signal(is_stdin, flag_i, flag_f, flag_n, fname);
      } // end if
      // if the file does not exist
      else{
        // display error message
        fprintf(stderr, "%s: No such file or directory\n", argv[j]);
      } // end else
    } // end for
  } // end else

  return 0;
} // end main program

// function: help
// arguments: none
// description: prints out usage information and defines all options.
// return: none
//
void help(){
  printf("Usage: print_signal [-h -n -f -i] [file...]\n");
  printf("Options: \n");
  printf("\t -h --help \t\t Display help message.\n");
  printf("\t -i --int \t\t Interpret data as 16-bit integers (default setting).\n");
  printf("\t -f --float \t\t Interpret data as 32-bit/4-byte floating point values.\n");
  printf("\t -n --no --numbers \t Display line number.\n");
} // end help

//
// end file
