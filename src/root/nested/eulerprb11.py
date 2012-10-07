'''
Created on Oct 5, 2012

@author: ed
'''

def prod(a_lst):
    #print a_lst
    res = 1
    for num in a_lst:
        res = num * res
        
    #print res
    return res

def main():
    from time import ctime
    
    print "Starting at:", ctime()
    big_prod = 0
    chk_lst = []
    row_num = 0
    
    fp = open('eulerprb11.txt', 'r')
    data = [line.strip() for line in fp.readlines()]
    fp.close()
    
    while row_num < 17:
        rowa, rowb, rowc, rowd = [], [], [], []
        for a_str in data[row_num].split():
            if a_str[0] == '0':
                rowa.append(int(a_str[1]))
            else:
                rowa.append(int(a_str))
        for a_str in data[row_num+1].split():
            if a_str[0] == '0':
                rowb.append(int(a_str[1]))
            else:
                rowb.append(int(a_str))
        for a_str in data[row_num+2].split():
            if a_str[0] == '0':
                rowc.append(int(a_str[1]))
            else:
                rowc.append(int(a_str))
        for a_str in data[row_num+3].split():
            if a_str[0] == '0':
                rowd.append(int(a_str[1]))
            else:
                rowd.append(int(a_str))
        
        if row_num < 17:
            for j in range(0,19):       # downward check
                chk_lst = [rowa[j],rowb[j],rowc[j],rowd[j]]
                if prod(chk_lst) > big_prod:
                    big_prod = prod(chk_lst)
                    
        for j in range(0,17):           # rightward check
            if prod(rowa[j:j+4]) > big_prod:
                big_prod = prod(rowa[j:j+4])
                
            if prod(rowb[j:j+4]) > big_prod:
                big_prod = prod(rowb[j:j+4])
                
            if prod(rowc[j:j+4]) > big_prod:
                big_prod = prod(rowc[j:j+4])
                
            if prod(rowd[j:j+4]) > big_prod:
                big_prod = prod(rowd[j:j+4])
                
        if row_num < 17:
            for j in range(0,17):       # right diagonal check
                chk_lst = [rowa[j],rowb[j+1],rowc[j+2],rowd[j+3]]
                if prod(chk_lst) > big_prod:
                    big_prod = prod(chk_lst)
                    
        if row_num < 17:
            for j in range(3,20):       # left diagonal check
                chk_lst = [rowa[j],rowb[j-1],rowc[j-2],rowd[j-3]]
                if prod(chk_lst) > big_prod:
                    big_prod = prod(chk_lst)
        
        row_num += 1
        
    print "Completed at: ", ctime()
    print big_prod

if __name__ == '__main__':
    main()