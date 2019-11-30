Good morning!

This is the first assignment, as discussed in the seminar part today.

The goal of this assignment is to practically implement and to 
test a simple program that will generate a pseudorandom bit 
stream using the ANSI X9.31 generator with the 128-bit version 
of the AES block cipher.

1. Download and compile an implementation of AES. You can choose 
implementation/language on your own, but your implementation must 
be correct with respect to the NIST test vectors 
(http://csrc.nist.gov/archive/aes/rijndael/wsdindex.html). 
One such implementation can be found at 
https://github.com/BrianGladman/AES.

2. Use the AES source code to implement the ANSI X9.31 pseudorandom 
number generator with the 128-bit version of AES. Specification of 
the algorithm can be found in files PV079assignment_1_2018_931rngext.pdf 
and PV079assignment_1_2018_ansi931rng.pdf in the IS.
You don't need to write the program from scratch, you can just 
extend the source code of your AES implementation. However,
you must implement the ANSI X9.31 by your own, not using
an existing implementation of the algorithm. You can only use existing AES
implementation.

3. Use your program to generate binary file F.bin of EXACTLY 10^9 bits of random data.
  	- Create initial seed V from repetitions of your UCO 
	(e.g., 2328862328862328 for UCO=232886). Truncate to cipher 
	block size, if needed. Do NOT treat numbers in UCO as ASCII 
	characters (e.g. 9 will be 0x09 hexadecimal, NOT 0x39).
 	- Create encryption KEY as a reversely ordered seed V 
	(e.g., 8232688232688232 for example V given above). Last 
	byte of the seed V will be the first byte of the key, 
	second last byte of V will be the second byte of the key, etc. 
	- Start with zero date/time vector and update it on each iteration. 
	Date/time vectors should be in the natural order i.e,
	0x0...00, 0x0..01,0...02,...,0x0...0f, 0x0...10,... in hexadecimal.
  
4. Use C library function - rand() seeded with your UCO and generate F2.bin of
  EXACTLY 10^9 bits.  

5. Perform a randomness analysis of the files F.bin, F2.bin using NIST STS. 
  (http://csrc.nist.gov/groups/ST/toolkit/rng/documentation_software.html).
  Each file has to be analysed as 1000 sequences, i.e, each consisting of
  10^6 bits. For the analysis use all tests (very slow Linear Complexity can be omitted)
  with their default settings.
  
6. Create empty file results_XXXXXX.txt for all results!
  
  Compute two hashes of F.bin and F2.bin and write them into results_XXXXXX.txt.
  Also write 2 tables from finalAnalysisReport.txt obtained for F.bin, F2.bin into results_XXXXXX.txt. 
  Describe shortly (in results_XXXXXX.txt) the meaning of Proportion, P-value, and Ci used in the tables. 
  Shortly (max 300 characters) interpret table obtained for F.bin.
  Shortly (max 300 characters) interpret table obtained for F2.bin.
	
  Strictly follow the format of file results_232886.txt computed for UCO 232886. 
 
7. Pack your source files to UCO.zip (not .rar or any other compression!!!). Post UCO.zip in the 
"Solutions to assignment #1" folder in "Homework Vaults" for our course in the IS.

IMPORTANT: 
The structure of UCO.zip has to be:
UCO.zip	
+-- results_XXXXXX.txt
+-- src
|   +-- main
|   ... directories or files used by main

The source code must be well commented!!!
During verification, seed V and KEY will be automatically generated 
from XXXXXX value from submitted files and d/t vectors will be used 
to generate and test exactly the same pseudorandom sequence. 
Correctness of the source code implementation will be checked. 
Note that your seed V and KEY can be 'hard-coded' into your source
code and you don't need to generate them based on supplied the 
file name (we must :)).

TIPS
- if you successfully complete tasks 1-3 you will be awarded 
6 points, for tasks 4-6 you can gain additional 4 points, altogether 
you can gain up to 10 points;
- we strongly recommend you to verify your implementation -- file results_232886.txt
 can be used to check the correctness of your implementation ;)

END

All the best,

Vashek Matyas