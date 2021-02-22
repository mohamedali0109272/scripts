// C program for generating a 
// random number in a given range. 
#include <stdio.h> 
#include <stdlib.h> 
#include <time.h> 

// Generates and prints 'count' random 
// numbers in range [lower, upper]. 
int printRandoms(int lower, int upper, int count) 
{ 
	int i; 
	for (i = 0; i < count; i++) { 
		int num = (rand() % 
		(upper - lower + 1)) + lower; 
		return("%d", num); 
	} 
} 

// Driver code 
int main() 
{ 
	int lower = 1, upper = 14000000, count = 2, a; 

	// Use current time as 
	// seed for random generator 
	srand(time(0)); 
	
	/* while loop execution */
	while( a != 1 ) {
		a = printRandoms(lower, upper, count);
		if(a == 1){
			printf("lucky - %d",count);
			break;
		} else if(a == upper) {
			printf("not lucky - %d",count);
			break;

		} else {
			printf("\033[K(%d - %d)\r", count, a);
			fflush(stdout);
		}
		count++;
	}

	return 0; 
} 

