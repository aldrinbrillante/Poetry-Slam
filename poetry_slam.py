# import randint() to use for the function lines_printed_random() 
from random import randint

#----------FUNCTION 1----------#
'''
Create a function called get_file_lines()
It should have 1 parameter called filename, which is a string of the filename.
It should return a list of strings containing the lines of the file.
'''
#define function with parameter filename
def get_file_lines(filename):
    # create variable to open & read file
    file_lines = open(filename, "r").read()
    # return the variable
    return file_lines

#print the function with .txt file as the parameter
print(get_file_lines("poem.txt"))
# print a space to give space between this section and the next
print("\n")


#----------FUNCTION 2----------#
'''
Create a function called lines_printed_backwards()
It should have 1 parameter called 'lines_list,' which is a 
list of strings containing lines of your poem
It should print the lines of the poem in reverse. 
Include the original line number at the beginning of each line
'''
# #define function with parameter lines_list
def lines_printed_backward(lines_list):
    # create variable for the LENGTH of parameter
    num_lines = len(lines_list)
    #print(lines_list)
    lines_list = lines_list[::-1] #reverses the list

    # for loop in range of len(lines_list), which is the variable created above
    for i in range(num_lines):
        # create a short-name variable for the length to be printed and to be subtracted by i. add space to give space b/w number and line text 
        p = str(num_lines - i) + " " + lines_list[i]
        #print variable
        print(p)

#create variable that opens file 
poem = open('./poem.txt' , 'r') 
#call function to read and splitlines() method
lines_printed_backward(poem.read().splitlines()) # pass a list of lines to foo 
#print \n to give space for next part of assignment
print("\n")


#----------FUNCTION 3----------#
'''
Create a function called lines_printed_random():
have 1 parameter called lines_list
It should print the lines of your poem in randomly order.
Repeats are ok, but make sure the number of lines printed is equal to the original lines in the poem
(Line numbers do not need to be printed.) 
Hint: try using a loop and randint() from the random module.
'''
def lines_printed_random(lines_list):
    # create variable for len() of line_list
    line_len = len(lines_list)
    #for loop
    for i in range(line_len):
        # variable random using randint()
        random = lines_list[randint(i, line_len - 1)]
        # print random
        print(random)

poem = open('./poem.txt', 'r')
lines_printed_random(poem.read().splitlines())
print("\n")

#----------FUNCTION 4----------#
'''
Create a function called lines_printed_custom()
minimally have 1 parameter called lines_list
It should print the poem in a unique way, be creative!
Make sure that you carefully comment your custom function so it’s clear what it does.
'''
#created function to sort poem lines in alphabetical order

# define function with parameter lines_list
def lines_printed_custom(lines_list):
    #with exception statement as 'r'
    with open('poem.txt', 'r') as r:
        # for loop with sorted function The sorted() function returns a sorted list of the specified iterable object.
        for line in sorted(r):
            # prints line variable
            print(line, end='')

poem = open('./poem.txt', 'r')
#calls custom function
lines_printed_custom(poem.readlines())
print("\n")