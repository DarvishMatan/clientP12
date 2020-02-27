import shelve

shelf = shelve.open("vars/vars.txt")  # directory for text file to save the vars
shelf['activation'] = 1  # set the 'activation' field to 1
print(shelf['activation'])  # get the 'activation field and print it
