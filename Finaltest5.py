import argparse
import os

#Commission scale for gross profit is 25%

def profit(p): 
   a = p * .25 
      
#Commission scale for spiffs is 100%
def spiffs(s):
   b = s * 1

#Commission scale for warranty is 20%

def warranty(w):
   c = w * .2 

#Commission scale for bedding is 1%

def bedding(b):
   d = b * .01

def total(t):
   t = a + b + c+ d

print(total)

def main():
    
    parser_formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser( description = 'Commission Calculator' ,formatter_class=parser_formatter)

    parser.add_argument('--profit', required=True, action='store',dest='profit', help='Gross profit for the period')
   
    parser.add_argument('--spiffs', required=True, action='store',dest='spiffs', default=True, help='Total spiffs earned for the period')

    parser.add_argument('--warranty', required=True, action='store',dest='warranty', default=True, help='Total warranty dollars for the period')

    parser.add_argument('--bedding', required=True, action='store',dest='bedding', default=True, help='Total dollars of bedding & mattresses sold during for the period')

    args = parser.parse_args()
    output = total
    

if __name__ == '__main__':
    main()


