'''
Created on Oct 8, 2012

@author: ed
'''

if __name__ == '__main__':
    from time import ctime
    
    big_num = 0L
    print "Starting at ", ctime()
    fp = open('eulerprb13.txt','r')
    data = [long(line.strip()) for line in fp.readlines()]
    fp.close()
    
    for num in data:
        big_num += num
        
    str_num = str(big_num)
    
    print "Completed at ", ctime()
    print "The sum = %d and the first ten digits of the sum are: %s" % (big_num,str_num[0:10])