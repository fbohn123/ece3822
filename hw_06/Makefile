# file: GNUMakefile
#

# define a target for the application
#
all: print_signals

#define a target to link the application
#
print_signals : read_signal.o main.o
	g++ -O2 $^ -o $@

#define a target to compile the application
#
read_signal.o: read_signal.cc
	g++ -O2 -c $^ -o $@

main.o: main.cc
	g++ -O2 -c $^ -o $@

# define a target to clean the directory
#
clean:
	rm -f main.o read_signal.o
	rm -f print_signals
#
# end of file
