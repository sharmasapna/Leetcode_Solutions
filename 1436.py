#1436
cclass Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        """
        list_s = [] # list with source
        list_d = [] # list with destination
        for val in paths:
            list_s.append(val[0])
            list_d.append(val[1])
        for val in list_d:
            if val not in list_s: # checking if the destination is available in source
                return val
        """
        # we can use zip and set to make it run faster
        a =list(zip(*paths)) # creates a list of tuples of the two indices as follows
        # original list : [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        # after using zip: a is [(u'London', u'New York', u'Lima'), (u'New York', u'Lima', u'Sao Paulo')]
        return (set(a[1])-set(a[0])).pop() # The difference of the two unique lists are returned
