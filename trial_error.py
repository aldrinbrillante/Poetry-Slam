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

# def lines_printed_backwards(line_list):
#     #add_num = print(len(line_list))
#     #n = add_num
#     #for loop
#         # The reversed() function returns the reversed iterator of the given sequence.
#         # The list() constructor returns a list in Python.
#         # The open() function opens a file, and returns it as a file object.

#     for line in reversed(list(open("poem.txt"))):
#         print(line.rstrip())
#     # return temp variable line
#     return line

# # call function lines_printed_backwards
# lines_printed_backwards("poem.txt")


# -------------------CO WORK CODE-----------------------------#

def lines_printed_backward(line_list):
    num_lines = len(line_list)
    #print(line_list)
    line_list = line_list[::-1] #reverses the list

    # 1 to num_lines
    for i in range(len(line_list)):
        #print (num_lines - i)
        #print(line_list[i])
        v = str(num_lines - i) + " " + line_list[i]
        print(v)

f = open('./poem.txt' , 'r') #opens the file
#foo([1, 2, 3, 4]) 
lines_printed_backward(f.read().splitlines()) # pass a list of lines to foo 