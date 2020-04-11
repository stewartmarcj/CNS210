# Fibonacci Assignment 1
# Function for nth Fibonacci number 
#

import argparse
import os 



def Fibonacci(n): 
   if n<0: 
      print("Incorrect input") 
# First Fibonacci number is 0 
   elif n==0: 
      return 0
# Second Fibonacci number is 1 
   elif n==1 or n==2: 
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2) 




def main():
    
    parser_formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser( description = 'Fibonacci Sequence' ,formatter_class=parser_formatter)

    parser.add_argument('--filename', required=True, action='store',dest='fib', help='fibonacci sequence output file')
   
    parser.add_argument('--number', required=True, action='store',dest='num', default=True, help='user selected number of the fibonacci sequence')
    args = parser.parse_args()
    output = Fibonacci(int(args.num))
   
    f = open("fib.txt", "w")
    f.close()

    f = open("fib.txt", "r")
    print(f.read())
   

