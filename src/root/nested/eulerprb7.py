'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    primes = 6
    num = 14
    while True:
        prime_found = True
        for i in range(2,num,1):
            quo,mod = divmod(num,i)
            if mod == 0:
                prime_found = False
                break
        
        if prime_found:
            primes += 1
            if divmod(primes,1000)[1] == 0:
                print "We found a prime: %d . It is the %d prime." % (num, primes)
            if primes == 10001:
                break
        num += 1
        
    print "The 10,001 prime is: %d" % (num)