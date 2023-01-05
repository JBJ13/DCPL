# DCPL
Double coding programming language - esoteric programming language.
This programming language was created so that its code could be easily edited by itself, so each instruction was given its own number.
Program written in Python 3.10

Data line is line of data that program can use. Indexing of data_line is from 0.
There are 4 markers on the data line: A, B, C and D.
Each of the markers has its own position on the line.
Markers can be moved to the right using>,
left with <, and can be moved to the position indicated by the number on the marker with ^.
After the marker A is moved, the instruction with the number it points to is executed.
Sample A shift: >>; This is the shift of marker A by 2 squares to the right.

At the beginning of the file in which we declare initial values, there must be: limes = n, where n is a positive integer that defines the length of the data line.
The values stored in the data line file begin with the second line and are separated by commas.

Instruction number and what is it doing:<br>
0: Increment B<br>
1: Decrement B<br>
2: B = 0<br>
3: B = C + D<br>
4: B = C-D<br>
5: B = C * D<br>
6: B = C // D<br>
7: B = C% D<br>
8: B = C ** D<br>
9: If B <0: goto C<br>
10: If B <= 0: goto C<br>
11: If B == 0: goto C<br>
12: If B> 0: goto C<br>
13: If B> = 0: goto C<br>
14: If B <C: goto D<br>
15: If B <= C: goto D<br>
16: If B == C: goto D<br>
17: If B> C: goto D<br>
18: If B> = C: goto D<br>
19: Set position A to B<br>
20: Set position B to C<br>
21: Set position C to B<br>
22: Set position D to B<br>
23: Write character B on consoles<br>
24: Write the number B on the consoles<br>
25: Download a series of characters<br>
26: Get the first character in the series of characters into B<br>
27: Get the number from console to B<br>
28: Goto B<br>
29: Set the value of A as the value of B<br>
30: Set the B value as the C value<br>
31: Set the C value as the B value<br>
32: Set the D value as the B value<br>

There is Hello World program. To use it: as a data_line you neet to write: data.txt, and as a file: program.txt
