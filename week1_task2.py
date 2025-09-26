# Here I create a function to split the strings of system messages into a list of individual words
# A line / string is given as input
# Then I check if any of my case words - ERROR or WARNING is in the list
# I then return an appropriate value

def tokenise(line):
    #Tokenise line
    words = line.split(' ')
    if "ERROR" in words:
        return "ERROR"
    elif "WARNING" in words:
        return "WARNING"
    else:
        return "OK"

# Here I create a function to handle the messages
# The input is: a specific line/string, the message given by the tokenise function and the -
# filepath of the file thats being analysed
# I use the datetime library to create a timestamp on the textfile, so that it would be implementable -
# in a continous environment where these logs are generated regularily

import datetime

current_day = datetime.date.today()
current_day = str(current_day)

def handle_message(line,message,filepath):
    if message == "ERROR":
        with open("ERROR_log_"+current_day+"_"+filepath+".txt","a") as file:
            file.write(line)
    if message == "WARNING":
        with open("WARNING_log_"+current_day+"_"+filepath+".txt","a") as file:
            file.write(line)

# Here I create a function to open the file and write the error-/warning_logs
# It calls the tokenise function to get a message

def handle_file(filepath):
    with open(filepath,"r") as file:
        lines = file.readlines()
        for line in lines:
            message = tokenise(line)
            if message == "ERROR" or message == "WARNING":
                handle_message(line, message,filepath)
                print("Handled the "+ message + " Message")
            else:
                print("System line not an error or warning")

# Here I run the code
# I take a users input - which hopefully is a viable filepath :)
# Then I apply the input into the handle_file function

x = input("Insert you file path here")

print(x)

handle_file(x)

# Here I print the warning_log file I just generated to check if I actually succeded in generating it

with open("WARNING_log_"+current_day+"_"+x+".txt","r") as file:
    for lines in file:
        print(lines)

# Here I print the error_log file I just generated to check if I actually succeded in generating it

with open("ERROR_log_"+current_day+"_"+x+".txt","r") as file:
    for lines in file:
        print(lines)
