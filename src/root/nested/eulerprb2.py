'''
Created on Oct 3, 2012

@author: ed
'''

if __name__ == '__main__':
    prev_term = 0
    curr_term = 1
    next_term = 1
    even_term_sum = 0
    while (even_term_sum < 4000000):
        print "curr_term = %d, prev_term = %d " % (curr_term, prev_term)
        next_term = curr_term + prev_term
        prev_term = curr_term
        curr_term = next_term
        if (divmod(next_term,2)[1] == 0):
            even_term_sum += next_term
            print "Even term = %d" % (next_term)
    print "Sum of even fibonacci terms = %d" % (even_term_sum)
        