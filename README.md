# DCPL
double coding programming language - esoteric programming language.

Data line is line of data that program can use. Indexing of data_line is from 0.
There are 4 markers on the data line: A, B, C and D.
Each of the markers has its own position on the line.
Markers can be moved to the right using>,
left with <, and can be moved to the position indicated by the number on the marker with ^.
After the marker A is moved, the instruction with the number it points to is executed.
Sample A shift: >>; This is the shift of marker A by 2 squares to the right.

At the beginning of the file in which we declare initial values, there must be: limes = n, where n is a positive integer that defines the length of the data line.
The values stored in the data line file begin with the second line and are separated by commas.

Instruction number and what is it doing:
0: Increment B
1: Decrement B
2: B = 0
3: B = C + D
4: B = C-D
5: B = C * D
6: B = C // D
7: B = C% D
8: B = C ** D
9: If B <0: goto C
10: If B <= 0: goto C
11: If B == 0: goto C
12: If B> 0: goto C
13: If B> = 0: goto C
14: If B <C: goto D
15: If B <= C: goto D
16: If B == C: goto D
17: If B> C: goto D
18: If B> = C: goto D
19: Set position A to B
20: Set position B to C
21: Set position C to B
22: Set position D to B
23: Write character B on consoles
24: Write the number B on the consoles
25: Download a series of characters
26: Get the first character in the series of characters into B
27: Get the number from console to B
28: Goto B
29: Set the value of A as the value of B
30: Set the B value as the C value
31: Set the C value as the B value
32: Set the D value as the B value
