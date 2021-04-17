'''
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''
def permutate(array):
    ans = []
    for i in range(len(array)):
        ans.append(array[i:] + array[:i])
    return ans

def ask_array():
    n = int(input('combien de nombres?\n'))
    array = []
    for i in range(n):
        array.append(input('element:'))
    return array

print(permutate(ask_array()))

