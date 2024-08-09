class Node:
    def __init__(self,left,right,val) -> None:
        self.left = left
        self.right = right
        self.val = val

def splitArr(ar,startIdx,endIndex):
    # If there is nothing left to split, create a leaf with curr idx val
    if startIdx==endIndex:
        return Node(None,None,ar[startIdx])
    # mid is the middle index of the split array
    mid = startIdx + (endIndex - startIdx)//2

    left = splitArr(ar, startIdx, mid)
    right = splitArr(ar, mid+1, endIndex)
    # For each arr split, make a node  with sum of starting vals and ending vals 
    return Node(left,right,left.val + right.val)

def setArray(ar):    
    global root
    global arr_len
    arr_len=len(ar)
    root = splitArr(ar,0,len(ar)-1)

def rs( r , currStart, currEnd, startIdx, endIdx):
    # No overlap in curr range and the one we are searching
    if endIdx<currStart or startIdx>currEnd: 
        return 0
    
    # Found an overlap in curr range and the one we are searching
    if startIdx<=currStart and endIdx>=currEnd:
        return r.val
    
    mid = currStart + (currEnd-currStart)//2
    
    # Go over left and right nodes and sum the found vals
    return rs(r.left , currStart, mid, startIdx, endIdx) + rs(r.right , mid+1, currEnd, startIdx, endIdx)

def rangeSum(L,R):
    return rs(root,0,arr_len-1,L,R)




