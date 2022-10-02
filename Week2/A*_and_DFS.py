
def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    fron=[]
    lent=len(cost)
    fron.append(start_point)
    vis=[]
    costt=0
    vis.append(start_point)
    while(vis):
        tot=[]
        costfu=[]
        new=[]
        z=vis.pop()
        for j in range(lent):
            if(cost[z][j]>0):
                new.append(j)
        for j in new:
            costfu.append(costt+cost[z][j])
            why=costt+cost[z][j]
            tot.append(heuristic[j]+why)
        if(costfu and tot):
            heyyyyyy=check_equal(tot)
            if (heyyyyyy==0):
                costt=min(costfu)
                minio=min(tot)
                ind=tot.index(minio)
            else:
                ind=heyyyyyy
            
            fron.append(new[ind])
            vis.append(new[ind])
    path=fron
    return path
def check_equal(arr):
    lent=len(arr)
    sum=0
    for i in range(lent-1):
        if(arr[i]==arr[i+1]):
            sum=sum+1
    if(sum==lent-1):
        return sum
    else:
        return 0

def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    path = []
    fron=[]
    visi=[]
    lent=len(cost)
    fron.append(start_point)

    while(fron):
        z=fron.pop()
        visi.append(z)
        for i in range(lent):
            if (cost[z][i]>0 and not i in visi):
                fron.append(i)
                break
    path=visi
    return path
