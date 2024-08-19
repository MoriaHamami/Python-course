

def dnc(baseFunc, combineFunc):

    def divide_until_apply(arr):

        if len(arr) == 1:
            # If there is one cell, apply base func on it
            return baseFunc(arr[0])
        
        # Divide array to two and for each part, 
        # keep on dividing until reaching one cell
        start = divide_until_apply(arr[(len(arr) // 2):]) 
        end = divide_until_apply(arr[:(len(arr) // 2)])
        
        # After applying base func, on return of recursion, 
        # apply combine_func on each 2 parts of arr
        return combineFunc(end, start)
    
    return divide_until_apply


def maxAreaHist(hist):

    def calc_max_area(hist, start, end):
        # If there is one cell, return val
        if start == end:
            return hist[start]
        
        # Find the minimum height in the sub-array
        curr_min_height = min(hist[start:end+1])
        
        # Calculate area based on the minimum height
        curr_max_area = curr_min_height * (end - start + 1)
        
        # Find index of curr minimum height   
        mid = hist.index(curr_min_height, start, end + 1)
        # Recursively calculate the maximum area on both sides of the sub-array   
        start_max_area = calc_max_area(hist, start, mid - 1) if mid > start else 0
        end_max_area = calc_max_area(hist, mid + 1, end) if mid < end else 0
        
        # Return the maximum area among the middle, start, and end sub-arrays
        return max(curr_max_area, start_max_area, end_max_area)
    
    return calc_max_area(hist, 0, len(hist) - 1)
