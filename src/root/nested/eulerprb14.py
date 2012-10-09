'''
Created on Oct 8, 2012

@author: ed
'''  

if __name__ == '__main__':
    from time import ctime
    
    print "Started at ", ctime()
    big_chain = 0
    
    for i in range(999999,0,-1):
        num = i
        chain = 0
        #print "Current number is %d" % (num)
        while num > 1:
            if divmod(num,2)[1] == 0:
                num = num / 2
                chain += 1
                #print "Chain is now ", chain
            else:
                num = (3 * num) + 1
                chain += 1
                #print "Chain is now ", chain
            #print "Number is ", num
        
        chain += 1
        
        if chain > big_chain:
            big_chain = chain
            big_num = i
            #print "New largest chain ", chain,"for number ",i
            
    print "completed at ", ctime()
    print "The starting number under one million that produces the longest Collatz chain is %d" % (big_num),"with",big_chain,"members in it's chain."