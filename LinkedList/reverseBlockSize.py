def solve(A,k):
    this_node = A.root()
    cnt = 0
    start_node,prev_node = None,None
    while this_node:
        if cnt == k:
            start_node.next() = this_node.next()
            start_node = this_node.next()
            # prev_node = 
            this_node = this_node.next()
        else:

            

