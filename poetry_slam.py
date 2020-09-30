# Create a function called get_file_lines()
# It should have 1 parameter called filename, which is a string of the filename.
# It should return a list of strings containing the lines of the file.
def get_file_lines(filename):
    file_lines = open(filename, "r").read()
    return file_lines

print(get_file_lines("poem.txt"))
print("\n")



# Create a function called lines_printed_backwards()
# It should have 1 parameter called 'lines_list,' which is a 
# list of strings containing lines of your poem

# It should print the lines of the poem in reverse. 
# Include the original line number at the beginning of each line

def lines_printed_backwards(line_list):
    for line in reversed(list(open("poem.txt"))):
        print(line.rstrip())
    return line
print(lines_printed_backwards("poem.txt"))


