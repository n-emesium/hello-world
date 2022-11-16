# Create two counter variables
# And initialize them with zero
line_count = 0
word_count = 0
 
# Open the given sample text file using open() function
file = open("C:path//sample_file.txt", "r", encoding='utf-8')
 
# Perform all the operations using the sample text file
# If it is opened successfully
if file != None:
    # Iterate over the opened file
    # To the number of lines and words in it
    for line in file:
        # Increment the line counter variable
        line_count = line_count + 1
        # Find the number of words in each line
        words = len(line.split())
        # Add the number of words in each line
        # To the word counter variable
        word_count = word_count + words 
else:
    print("OSError: File cannot be opend!!")
 
# Close the above opened text file using close() function
file.close()
 
# Print the final results using the final values 
# Of the line_count and word_count variables
print(f"\nTotal number of lines in the given file: {line_count}")
print(f"\nTotal number of words in the given file: {word_count}")