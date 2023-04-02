"""
    DSA sorting algorithms: Selction sort
    Author: Danish Xavier
    email: danishxr@gmail.com
    Twitter: @SillyTechy


"""

# Seclection sort algorithm

a = [1, 2, 8, 5, 6, 4, 3, 7]

i = 0

while i < len(a)-1:

    # store position of the smallest number index
    k = i

    j = i+1

    while j < len(a):

        # find the position of the smallest element
        if a[k] > a[j]:
            k = j

        j = j+1

    # Swap with the smallest element
    temp = a[i]
    a[i] = a[k]
    a[k] = temp


    i = i + 1

print(a)