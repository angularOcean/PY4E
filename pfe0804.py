print("Chapter 8: Exercise 4: Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.")
prompt = input("Please provide text file name:", )
shake = open(prompt)
shakelist = [ ]
for line in shake:
    words = line.split()
    for word in words:
        if word in shakelist:
            continue
        else:
            shakelist.append(word)
shakelist.sort()
print("The list of words in the text is:", shakelist)
        
    
    
        

