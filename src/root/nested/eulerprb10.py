'''
Created on Oct 5, 2012

@author: ed
'''
from time import ctime
    
def main():
    print"Starting up...", ctime()
    sum_primes = 2
    max_prime = 2000000
    num = 3
    
    while num < max_prime:
        prime_found = True
        for i in range(2,int(num**0.5) + 1,1):
            mod = divmod(num,i)[1]
            if mod == 0:
                prime_found = False
                break
        
        if prime_found:
            #print "Prime found %d" % (num)
            sum_primes += num
            
        num += 2
    
    print "Finished at ", ctime()
    print "The sum of primes under 2 million is: %d" % (sum_primes)

if __name__ == '__main__':
    main()