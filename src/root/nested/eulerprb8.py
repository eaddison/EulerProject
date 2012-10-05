'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    big5 = 0
    prod = 1
    str_dat = ""
    fp = open('eulerprb8.txt','r')
    data = [line.strip() for line in fp.readlines()]
    fp.close()
    
    for astring in data:
        str_dat = str_dat + astring
    
    for num_str in str_dat[0:5]:
        prod *= int(num_str)
    big5 = prod
        
    for i in range(5,995,1):
        prod = 1
        for num_str in str_dat[i-4:i+1]:
            prod *= int(num_str)
        if prod > big5:
            big5 = prod
    print "The biggest consecutive 5 number product is: %d" % (big5)