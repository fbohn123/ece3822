# file: GNUMakefile
#

# define a target for the application
#
all: hw_03.exe

#define a target to link the application
#
hw_03.exe : f_01.o f_00.o
	g++ -O2 f_00.o f_01.o -o hw_03.exe

#define a target to compile the application
#
f_01.o: f_01.cc
	g++ -O2 -c f_01.cc -o f_01.o

f_00.o: f_00.cc
	g++ -O2 -c f_00.cc -o f_00.o

# define a target to clean the directory
#
clean:
	rm -f f_00.o f_01.o
	rm -f hw_03.exe

#
# end of file
