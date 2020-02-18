# to comment any line keyboard shortcut ctrl+k+c

# Declearing string in a variable
WorkStr = "Hello Work"

# Checking length of the string using len() function
stringlength = len(WorkStr)

print(stringlength)

#checkinh is there any word = "work" in the string

cond = ("Work" in WorkStr)

print(cond)


# getting index of the particular word

indexofw = WorkStr.index("Work")

print(indexofw)

# We need to get first 5 charecter of the string
Char5s = WorkStr[:5]
print("First Five charecter of the string:",Char5s)

# We need to get first 5 charecter of the string
Char5e = WorkStr[-5:]
print("Last Five charecter of the string:",Char5e)

# Creating a new string variable
newString = "D:/Python/Tutorial/String.py"

# spliting string into list of substring using seperator
stringlist = newString.split("/")
print(stringlist)

# Accesing any of the splitted part of the splitted list
print("File Name:",stringlist[-1]) # -1 index is used to look at last item of the list

# join function used to join a list of string into a single string using a separator
# if separator kept blank the string will be joined without any separator
# in this example we will use / as separator to join the string list
# We have to select the list excluding the last item

newList = stringlist[:-1]
separator = "/"
newjoinedstring = separator.join(newList)

print("Folder Path:",newjoinedstring)


# startswith() this function checks if the string starts with the mentioned string and returns true or false.

Chkstrt = WorkStr.startswith("Hello")

print(WorkStr,"is Starts with Hello : ",Chkstrt)
Chkstrt = newString.startswith("Hello")
print(newString," is Starts with Hello : ",Chkstrt)

# endswith() this function checks if the string ends with the mentioned string and returns true or false.

Chkend = WorkStr.endswith("py")

print(WorkStr,"is Ends with py : ",Chkend)
Chkend = newString.endswith("py")
print(newString," is Ends with py : ",Chkend)