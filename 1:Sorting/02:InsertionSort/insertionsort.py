```
    DSA sorting algorithms: Selction sort
    Author: Danish Xavier
    email: danishxr@gmail.com
    Twitter: @SillyTechy


```


a = [1,2,3,5,5,6,4,7]

i = 0 

while i < len(a)-1:

    # Traverse the array to compare the values with the inital value
    if a[i] > a[i+1]:
    
        p = i
        
        while p >= 0:
            
            # Traverse to the left to insert the element in the right position
            if a[p] > a[p+1]:

                # swap logic
                temp = a[p+1]
                a[p+1] = a[p]
                a[p] = temp
            
            # condtion to exit
            if p == 0:
    
                break
    
            else:
    
                p = p - 1

    i = i + 1

print(a)

