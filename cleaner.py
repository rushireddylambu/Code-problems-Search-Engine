import re #by importing re we can use all these open file things from regular expression
# required for pattern matching

arr=[]  #array to store lines of the file

#open the file 
with open('leetcode.txt','r') as file:  # read each line one by one        
    for line in file:  #processing the line from the file
        arr.append(line) #performing append on every line to add them to array



def remove_elements_with_this_pattern(array,pattern):
    new_array=[]
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed:"+element)
    return new_array

arr=remove_elements_with_this_pattern(arr,"/solution")
print(len(arr))
arr=list(set(arr))

with open('leecode_problems.txt','a') as f: 
   
    for j in arr:     #iterate over each link in your final list
        
        f.write(j) #write each link to the file followed by new line