# Inna Lin, wl676
# Kristen Engel, ke242

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE

    this_string = is_word(string[i:j])
    if this_string == False:
        return RespaceTableCell(this_string, None)
    else:
        if i == 0:
            previous_end = True
        else:
            previous_end = False
            for ind in range(i):
                if T.get(ind, i).value == True:
                    previous_end = True

        fill_value = this_string and previous_end

        return RespaceTableCell(fill_value, i)


# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    #TODO: YOUR CODE HERE
    cell_order = []

    for i in range(0, N+1):
        for j in range(i, N+1):
            cell_order.append((i,j))
    return cell_order

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    #TODO: YOUR CODE HERE
    new_s = ''

    i = len(s)
    while (i > 0):
        ind = i-1
        next_i = i - 1
        existT = False
        while (ind >= 0):
            if table.get(ind, i).value == True:
                existT = True
                new_s = s[ind : i] + ' ' + new_s
                next_i = ind
                break
            else:
                ind -= 1
        if existT == False:
            return None
        else:
            i = min(i-1, next_i)
    new_s = new_s[:-1]
    return new_s


if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "itwasthebestoftimes"
    wordlist = ["of", "it", "the", "best", "times", "was"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print (respace_from_table(s, D))
