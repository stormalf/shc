#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
a tiny shell compiler written in python.
it generates a c code, compiles it using gcc.
For now, in this first try, it compiles only if the source contains only executable commands.
It's possible to generate directly assembly language without generating C code. Perhaps in a future version.
'''


import sys
import os 
import argparse

__version__ = "1.0.0"


EXT = ".shc"
header= "#include <stdio.h>\n \
#include <stdlib.h>	//to use system()\n \
#include <string.h> //to use strcpy()\n \
\n \
int main() \n \
{ \n \
	char cmd[500];\n \
    char *command = cmd;\n \
    int error = 0;"

footer = "return 0; \n \
} \n"    

def shcVersion():
    return f"shc version : {__version__}"

def shc(parms):
    if parms.file == "":
        print("Error : no input file")
        return
    if parms.file[-4:] != EXT:
        print("Error : file must be a .shc file")
        return
    if parms.output == "":
        parms.output = args.file.split(".")[0]
    output = parms.file + ".c"
    exename = parms.output
    of = open(output, "w")
    of.write(header)
    with open(parms.file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            else:
                of.write("strcpy(command, \"" + line.strip().replace('"','\\"') + "\");\n")
                of.write("error = system(command);\n")
                of.write("if (error != 0) { \n")
                of.write("printf(\"Error: %d, %s\", error, command);\n")
                of.write("exit(1);\n")
                of.write("}\n")
    of.write(footer)
    of.close()
    os.system("gcc -Og " + output + " -o " + exename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="shc is a tiny shell transpiler to C and creates an executable file")
    parser.add_argument('-V', '--version', help='Display the version of shc', action='version', version=shcVersion())
    parser.add_argument('-f', '--file', help='shell file .shc containing the commands to execute', required=True)
    parser.add_argument('-o', '--output', help='outputfile by default it will be the file without .shc', default="", required=False)  
    args = parser.parse_args()
    shc(args)
