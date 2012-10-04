'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    sum_of_sqr = 0
    sum_of_nums = 0
    for num in range(1,101,1):
        sum_of_sqr += pow(num,2)
        sum_of_nums += num
        
    sqr_sum = pow(sum_of_nums,2)
    diff = abs((sqr_sum - sum_of_sqr))
    print "The difference between the sum of squares and the square of the sum for the first 100 natural numbers is: %d" % (diff)