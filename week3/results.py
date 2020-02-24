# Student Marks Administration
# Pete Dwyer 01/11/17
# Saul Johnson 20/06/2019

from datafile import data

# Initialise variables.

# Define functions.
def show_raw_data(dat):
   for ind in range(0, len(data), 2):
       print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4)) 

# Main body of program.
show_raw_data(data)



