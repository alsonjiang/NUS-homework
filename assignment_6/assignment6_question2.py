############################################
## DO NOT MODIFY THIS PORTION OF CODE!!!! ##
############################################

def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def m_tight_print(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

############################################
########### End of do not modify ###########
############################################

############
##  Task  ##
############

def pd_map(r: int, c: int, sites: list) ->list:
    pass

# m_tight_print(pd_map(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
# m_tight_print(pd_map(10,10,[[2,3],[4,9],[7,2]]))

# m_tight_print(pd_map(60,70,[[10,20],[30,20],[40,50]]))
# ex = pd_map(60,70,[[10,20],[30,20],[40,50]])
    
