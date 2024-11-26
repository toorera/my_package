def top_n(items, n):
    """ This function returns top n items in an array in descending order

    Args: 
        items (array): list or array-like object
        n (int): number of items to return

    return:
        array: top n items in descending order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
            [8,7,4]


    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                
    top_n = items[-n:]
    
    return top_n[::-1]