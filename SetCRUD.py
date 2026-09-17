# Adding an Element:
set_1 = {1,3,6,"12"}
set_1.add("Swapnil")
print(set_1)

# removing an element
set_1.remove("12")

# replacing an element
# first we remove the element and then we add it 

set_1.discard(6)

# remove vs discard 
# remove(): Removes the element, but raises a KeyError if it isn't present.
# Discard(): Removes the element if it exists. If it doesn't exist, nothing happens.