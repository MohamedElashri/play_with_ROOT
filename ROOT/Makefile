CC=g++

CFLAGS=-c -g -Wall `root-config --cflags`

LDFLAGS=`root-config --glibs`

all: write_ROOT read_ROOT fill_histogram

write_ROOT: write_ROOT.cc
	$(CC) $(CFLAGS) -o write_ROOT.o write_ROOT.cc
	$(CC) $(LDFLAGS) -o write_ROOT write_ROOT.o 

read_ROOT: read_ROOT.cc
	$(CC) $(CFLAGS) -o read_ROOT.o read_ROOT.cc
	$(CC) $(LDFLAGS) -o read_ROOT read_ROOT.o 

fill_histogram: fill_histogram.cc
	$(CC) $(CFLAGS) -o fill_histogram.o fill_histogram.cc
	$(CC) $(LDFLAGS) -o fill_histogram fill_histogram.o
clean:
	rm -f ./*~ ./*.o ./write_ROOT
	rm -rf ./*~ ./*.o ./read_ROOT
	rm -rf ./*~ ./*.o ./fill_histogram
