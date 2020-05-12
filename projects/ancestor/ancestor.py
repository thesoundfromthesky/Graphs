from math import inf

#(parent, child)
def earliest_ancestor(ancestors, starting_node):
    
    #{child: parent}
    a = {}
    for i in ancestors:
        c = i[1]
        p = i[0]
        if c not in a:   
            a[c]=[p]
        else:
            a[c].append(p)

    if starting_node not in a:
        return -1
    
    #{vertex:[weight, prev_child]}
    l= {starting_node: [0, None] }
    s = []

    s.append(starting_node)

    while len(s):
        v = s.pop()

        if v not in a:
            continue

        for nxt in a[v]:
            s.append(nxt)
            
            if nxt not in l:
                 l[nxt]=[inf, None]
            
            d = l[v][0] + 1

            d_s = l[nxt][0]
            if d < d_s:
                l[nxt]=[d, v]
    
    r=[]
     #{vertex:[weight, prev_child]}
    for i, v in l.items():
        if not len(r):
            r.append([v[0],i])
        else:
            if r[0][0] == v[0]:
                r.append([v[0], i])
            elif r[0][0] < v[0]:
                r =[[v[0],i]]


    e_a=None
    for i in r:
        a=i[1]
        if not e_a:
            e_a = a
        elif e_a > a:
            e_a = a
            
    return e_a

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 3)