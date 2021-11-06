# shc
tiny shell transpiler to C in python3

This small tool generates from a specific shell script .shc that contains only comments or executable commands a C code and the executable file.

## shc usage 

python3 shc.py --help

    usage: shc.py [-h] [-V] -f FILE [-o OUTPUT]

    shc is a tiny shell transpiler to C and creates an executable file

    optional arguments:
    -h, --help            show this help message and exit
    -V, --version         Display the version of shc
    -f FILE, --file FILE  shell file .shc containing the commands to execute
    -o OUTPUT, --output OUTPUT
                            outputfile by default it will be the file without .shc

Example : python3 shc.py -f example.shc
    It creates an output C file example.shc.c and the executable file example that will execute the commands defined in the .shc file.

Example : python3 shc.py -f example.shc -o test123
    It creates an output C file example.shc.c and an exe file test123
       
       ./test123
        hello world!
        example.shc  example.shc.c  result.txt  shc.py  test123
        Sat Nov  6 12:49:18 CET 2021