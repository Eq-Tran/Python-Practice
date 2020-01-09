# Write a function that takes a list and returns a new list with the same elements of the 
# first list without any duplicates
#
# Python Practice 14
#
# BONUS: instead of using set use a loop



d = [1,2,3,4,5,6,5,6,7,8,9,0]

def duplicates(d):

    a = [i for i in set(d)]
    return(a)




# WITH loop


# NOT FINISHED
def duplicates_with_loop(d):

    a = []
    for i in d: # loop through every index in d
        if i not in a: # if index is not in d
            a.append(i) # append those indexes to a
    return(a)

print (duplicates_with_loop(d))
print (duplicates(d))       