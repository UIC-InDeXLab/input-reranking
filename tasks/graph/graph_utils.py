def get_degree(edge_list, vertex):
    return len([e for e in edge_list if vertex in e])

def shiftLbyn(arr, n=0):
    return arr[n::] + arr[:n:]

def shiftRbyn(arr, n=0):
    return arr[n:len(arr):] + arr[0:n:]