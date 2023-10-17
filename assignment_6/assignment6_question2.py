import pprint
import matplotlib.pyplot as plt
############################################
## DO NOT MODIFY THIS PORTION OF CODE!!!! ##
############################################

#creates a r x c zero matrix
def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]
#print(create_zero_matrix(3,3)) 

#given a matrix, turn into a string, print out (tight print)
def m_tight_print(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)
#m_tight_print(create_zero_matrix(3,3))
#000
#000
#000

############################################
########### End of do not modify ###########
############################################

############
##  Task  ##
############

#euclidean distance = ((x1-x2)**2 + (y1-y2)**2)*0.5
def euclidean_distance(i: int, j: int, point_2: list) -> float:
    return ((i - point_2[0])**2 + (j - point_2[1])**2)**0.5


def pd_map(r: int, c: int, sites: list) ->list:
    homes = create_zero_matrix(r, c) #creates a r x c zero matrix
    for i in range(r):
        for j in range(c):
            #for every coordinate point, check euclidean distance to every pizza hut in sites
            distances = [euclidean_distance(i, j, site) for site in sites] #list of distances to all piza huts from one house
            nearest = min(distances) #get nearest pizza hut distance
            if distances.count(nearest) > 1: #more than one nearest pizza hut
                homes[i][j] = 'X'
            else:
                homes[i][j] = distances.index(nearest) #save the closest pizza hut number to the coordinate   
    return homes

m_tight_print(pd_map(10, 10, [[2, 2], [6, 6]]))
#m_tight_print(pd_map(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
# m_tight_print(pd_map(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
# m_tight_print(pd_map(10,10,[[2,3],[4,9],[7,2]]))
#m_tight_print(pd_map(60,70,[[10,20],[30,20],[40,50]]))
# ex = pd_map(60,70,[[10,20],[30,20],[40,50]])
#print(pd_map(60,70,[[10,20],[30,20],[40,50]]))
    
################
##  OPTIONAL  ##
################
def visualize_colored_map(matrix):
    # Define a color mapping (you can extend or change this)
    color_map = {
        0: 'white',
        1: 'red',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'purple',
        6: 'orange',
        'X': 'black'  # 'X' or any other special characters you used
    }

    # Replace integers with their respective colors
    colored_matrix = [[color_map[val] for val in row] for row in matrix]

    # Visualize using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(colored_matrix, aspect='auto')
    ax.axis('off')  # Hide the axis
    plt.show()

matrix = pd_map(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]])
#visualize_colored_map(matrix)

    

