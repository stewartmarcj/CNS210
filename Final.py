import argparse
import os

#Commission scale for gross profit is 25%

def profit(p): 
   return (p * .25) 
      
#Commission scale for spiffs is 100%
def spiffs(s):
   return (s * 1)

#Commission scale for warranty is 20%

def warranty(w):
   return (w * .2)

#Commission scale for bedding is 1%

def bedding(b):
   return (b * .01)




def main():
    
    parser_formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser( description = 'Commission Calculator' ,formatter_class=parser_formatter)

    parser.add_argument('--profit', required=True, action='store',dest='profit', type=int, help='Gross profit for the period')
   
    parser.add_argument('--spiffs', required=True, action='store',dest='spiffs', default=True, type=int, help='Total spiffs earned for the period')

    parser.add_argument('--warranty', required=True, action='store',dest='warranty', default=True, type=int, help='Total warranty dollars for the period')

    parser.add_argument('--bedding', required=True, action='store',dest='bedding', default=True, type=int, help='Total dollars of bedding & mattresses sold during for the period')

    args = parser.parse_args()
   
    total = profit(args.profit) + spiffs(args.spiffs) + warranty(args.warranty) + bedding(args.bedding)

    print(total)
    
    
    

if __name__ == '__main__':
    main()


