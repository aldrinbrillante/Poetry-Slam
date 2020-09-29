# Create a function called get_file_lines()
# It should have 1 parameter called filename, which is a string of the filename.
# It should return a list of strings containing the lines of the file.

def get_file_lines(filename):
    # create variable for open/read file_lines
    file_lines = open(filename, "r").read()
    return file_lines
print(get_file_lines("poem.txt", "\n")

# Create a function called lines_printed_backwards()
# It should have 1 parameter called 'lines_list,' which is a 
# list of strings containing lines of your poem

# It should print the lines of the poem in reverse. 
# Include the original line number at the beginning of each line

def line_printed_backwards(line_list):
    poem_dict_lines = open(line_list, "r").readLines()
    reverse = ''
    num_count = len(line_list)
    for line in reversed(list(open("poem.txt"))):
        num_count = num_count - 1
        print(line.rstrip())
    return reverse
    



# def lines_printed_backwards(line_list):
#     poem_dict_lines = open(line_list, "r").readlines()
#     reverse = ''
#     num_count = len(line_list)
#     for line in reversed(list(open("poem.txt"))):
#         num_count = num_count - 1
#         print(line.rstrip()) 
#     return reverse

print(lines_printed_backwards("poem.txt"))


