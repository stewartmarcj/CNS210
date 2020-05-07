import argparse
import os

#Commission scale for gross profit is 25%

def profit(p): 
   if p<=0: 
      print('Incorrect input') 
   else:
      return p / 4 
   elif n==0: 
      
#Commission scale for spiffs is 100%

#Commission scale for warranty is 20%

def warranty(w):
   if w<=0:
      print('Incorrect input')
   else:
      return w / 5 

#Commission scale for bedding is 1%

def bedding(b):
   if b<=0:
      print('Incorrect input')
   else:
      return b / 1

def total:(t)
   total = p + s + w + b

def main():
    
    parser_formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser( description = 'Commission Calculator' ,formatter_class=parser_formatter)

    parser.add_argument('--profit', required=True, action='store',dest='profit', help='Gross profit for the period')
   
    parser.add_argument('--spiffs', required=True, action='store',dest='spiffs', default=True, help='Total spiffs earned for the period')

     parser.add_argument('--warranty', required=True, action='store',dest='warranty', default=True, help='Total warranty dollars for the period')

      parser.add_argument('--bedding', required=True, action='store',dest='bedding', default=True, help='Total dollars of bedding & mattresses sold during for the period')

    args = parser.parse_args()
    output = Fibonacci(int(args.num))
   
    f = open(args.fib, "w")
    f.write(str(output))

    f = open(args.fib, "r")
    print(f.read())
    print(args.fib)

if __name__ == '__main__':
    main()
