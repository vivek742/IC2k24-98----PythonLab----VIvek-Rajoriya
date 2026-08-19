# Python Programming Lab

19 AUG 2026
This repository contains the Python programs for the lab assignment. The programs use simple Python concepts such as functions, loops, nested loops, recursion, arithmetic operations, and basic input validation.

## Files

1. `01_armstrong.py` - Armstrong Number
2. `02_prime.py` - Prime Number
3. `03_perfect.py` - Perfect Number
4. `04_palindrome.py` - Palindrome
5. `05_fibonacci.py` - Fibonacci Series
6. `06_pattern.py` - Pattern Printing
7. `07_menu_driven.py` - Menu-Driven Application
8. `08_number_guessing.py` - Number Guessing Game

---

# 1. Armstrong Number

### Aim
To check whether a number is an Armstrong number and print all Armstrong numbers in a given range.

### Logic
The program finds the number of digits and adds each digit raised to that power. The same function is used to check every number in the given range.

### Sample Input / Output

```text
Enter a number: 153
153 is an Armstrong number.
Enter range start: 100
Enter range end: 1000
Armstrong numbers in the range:
153 370 371 407
```

---

# 2. Prime Number

### Aim
To check whether a number is prime and print all prime numbers up to a given limit.

### Logic
The program checks whether the number is divisible by any number between 2 and the number minus 1. The same prime-checking function is used for all numbers up to the limit.

### Sample Input / Output

```text
Enter a number: 29
29 is a prime number.
Enter the limit: 30
Prime numbers up to 30:
2 3 5 7 11 13 17 19 23 29
```

---

# 3. Perfect Number

### Aim
To check whether a number is a perfect number and print all perfect numbers up to a given limit.

### Logic
The program finds all proper divisors of a number and adds them. If their sum is equal to the original number, the number is perfect.

### Sample Input / Output

```text
Enter a positive number: 28
28 is a perfect number.
Enter the limit: 100
Perfect numbers up to 100:
6 28
```

---

# 4. Palindrome

### Aim
To check whether a number and a string are palindromes.

### Logic
The number is reversed using arithmetic operations such as `%` and `//`, without converting it to a string. For a string, the characters are reversed and compared with the original string.

### Sample Input / Output

```text
Enter a number: 1221
1221 is a palindrome.
Enter a string: madam
String is a palindrome.
```

---

# 5. Fibonacci Series

### Aim
To print the first n terms of the Fibonacci series using a loop and recursion and count the recursive function calls.

### Logic
The loop version keeps two variables for the previous two terms. The recursive version calculates each term using the previous two terms and counts every recursive call.

### Sample Input / Output

```text
Enter number of terms: 10
Fibonacci using loop:
0 1 1 2 3 5 8 13 21 34

Fibonacci using recursion:
0 1 1 2 3 5 8 13 21 34

Number of recursive function calls: 177
```

---

# 6. Pattern Printing

### Aim
To print a right-angled triangle, a number pattern, and a centered pyramid using nested loops.

### Logic
Nested loops are used to control the number of stars, numbers, and spaces in every row. The number of elements changes according to the current row.

### Sample Input / Output

```text
Enter number of rows: 4

1. Right-Angled Triangle
* 
* * 
* * * 
* * * *

2. Number Pattern
1
1 2
1 2 3
1 2 3 4

3. Centered Pyramid
      * 
    * * * 
  * * * * * 
* * * * * * *
```

---

# 7. Menu-Driven Application

### Aim
To combine Programs 1 to 6 into one menu-driven application.

### Logic
The program displays a menu and asks the user to select an operation. The selected function is executed and the menu is displayed again until the user selects Exit. Invalid menu choices are handled using a simple `else` condition.

### Sample Input / Output

```text
========== MENU ==========
1. Armstrong Number
2. Prime Number
3. Perfect Number
4. Palindrome
5. Fibonacci Series
6. Pattern Printing
7. Exit
==========================
Enter your choice: 2
Enter a number: 17
17 is a prime number.
```

---

# 8. Number Guessing Game

### Aim
To create a game where the computer generates a random number from 1 to 100 and the user gets a maximum of 7 attempts to guess it.

### Logic
The program generates a random number and compares each user guess with it. It tells the user whether the guess is too high or too low and stops when the number is guessed or all attempts are used.

### Sample Input / Output

```text
Guess the number between 1 and 100.
You have 7 attempts.
Enter your guess: 50
Too low!
Enter your guess: 75
Too high!
Enter your guess: 63
Correct!
Number of attempts: 3
```

#9 All the Other Pattern Programs Sample Output
*  *  *  *  
*  *  *  *  
*  *  *  *  
*  *  *  *  

*
**
***
****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*

**********
*********
********
*******
******
*****
****
***
**
*


              * 
            * * * 
          * * * * * 
        * * * * * * * 
      * * * * * * * * * 
    * * * * * * * * * * * 
  * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 

********************
*********  *********
********    ********
*******      *******
******        ******
*****          *****
****            ****
***              ***
**                **
*                  *
**                **
***              ***
****            ****
*****          *****
******        ******
*******      *******
********    ********
*********  *********
********************

********************
*********  *********
********    ********
*******      *******
******        ******
*****          *****
****            ****
***              ***
**                **
*                  *

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 


# Author

**Vivek Rajoriya**

BCA - International Institute of Professional Studies, DAVV
