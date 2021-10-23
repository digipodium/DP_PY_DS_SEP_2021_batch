def avg(number=[]):
    if number:
        return sum(number)/len(number)


# print( avg(12,34,56,123,45,23) )
# print( avg() )
# print( avg(1,2) )
# print( avg(1,2,3,4) )
# print( avg(1,2,123,132,13,123,12,31,23,123,12,3) )


def stats(*val, action='max'):
    '''
    function for doing stats, like min, max, sum, avg, count,etc
    '''
    if val:
        if action =='max':
            return max(val)
        elif action =='min':
            return min(val)
        elif action =='sum':
            return sum(val)
        elif action =='avg':
            return avg(val)
        elif action =='count':
            return len(val)
        elif action == 'all':
            return max(val), min(val), sum(val), avg(val), len(val)

print("calling stats")
print(stats(1,23,12,31,23,13,123,1,31,231,21,2))
print(stats(1,2,2,3,3,2,1,2,3,3,action='count'))
print(stats(1,2,1,2,3,3,action='all'))
print(stats(1,2,3,action='avg'))