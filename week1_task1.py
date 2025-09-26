# Function to split a string into different "tokens" or letters in a list - 
# used to count the instances of letters in the word
def splitword(word):
    a = [char for char in word]
    return a

# Function to find the average of a list of numbers
# The function takes a list as input
# Should be done to improve code is to make it verify that the input data is a int or float -
# As a string would cause issues
def findavg(numbers):
    avg = 0
    total = 0
    for i in numbers:
        total = total + i
    avg = total / len(numbers)
    return avg

# Function to find the median of a list of numbers
# The function checks if the amount of numbers is even or uneven, as the way to pick the median differs based on this.
def findmedian(numbers):
    median = 0
    tot_num_entries = len(numbers)
    is_even = tot_num_entries % 2
    sort_numbers = sorted(numbers)
    if is_even == 1:
        rounded_mid = round(tot_num_entries/2)
        median = sort_numbers[rounded_mid]
        return median
    else:
        x1 = round(tot_num_entries/2)
        x2 = round((tot_num_entries/2)+1)
        truex1 = sort_numbers[x1]
        truex2 = sort_numbers[x2]
        median = (truex1+truex2)/2
        return median

# Openening the Namelist file
# For every line of text I split the information, based on a common delimiter, in this case ','
# To handle case sensitivity, I turn all letters to lower
# Then I sort the list
# First on alphabethical order, then by the length of the names
with open("Navneliste.txt","r") as file:
    lines = file.readlines()
    print(type(lines))
    list_of_names = []
    for line in lines:
        x = line.split(',')
        for i in x:
            #print(i)
            list_of_names.append(i.lower())
    print(len(list_of_names))
    for i in range(10):
        print(list_of_names[i-1])
    sorted_alphabetic_list = sorted(list_of_names)
    print('sorted')
    for i in range(10):
        print(sorted_alphabetic_list[i])
    sorted_len_list = sorted(list_of_names, key=len)
    for i in range(10):
        print(sorted_len_list[i])

# First I create a string that include all letters in the english alphabeth
# Then I split the string into a list
# Afterwards this list is used to generate a list of dictionaries that have letter and count for later purposes

alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
list_of_letters = alphabet.split(',')

list_to_count = []
for i in list_of_letters:
    list_to_count.append({'Letter': i, 'Count': 0})

print(list_to_count)

# Now I create a list to store all letters in every name so that I can iterate through all letters in the text.
# I use the splitword function I defined earlier to do this to get all of these individual "tokens" in the text.
count_list = []
for i in list_of_names:
    wordsplitted = splitword(i)
    for v in wordsplitted:
        count_list.append(v)
        
print(len(count_list))
print(count_list)

# I make a list to store my results in
# iterate through the alphabet and my list of letters in a nested loop
# Making sure to reset the count on every instance of new letter in the alphabet

new_counted_list = []
count = 0
for i in list_of_letters:
    if count != 0:
        count = 0
    for v in count_list:
        if v == i:
            count+=1
    new_counted_list.append({'Letter': i, 'Count': count})

print(new_counted_list)

#Importing the matplotlib library to use for visialization of the results
# I make a list of x values, in this case this is the alphabet and a list of y values
# - in this case it is the amount of instances of letters in the words
# I then iterate through the list of dictionaries to get the values

import matplotlib.pyplot as plt

list_of_x = []
list_of_y = []
for i in new_counted_list:
    for key, value in i.items():
        if key == 'Letter':
            list_of_x.append(value)
        else:
            list_of_y.append(value)

print(list_of_x)
print(list_of_y)

# In this section I plot the results into a barplot

fig, ax = plt.subplots()
ax.bar(list_of_x, list_of_y, width=1, edgecolor='white', linewidth=0.9)

plt.show()

# I import the wordcloud library to generate a wordcloud image

from wordcloud import WordCloud
from os import path

bil =""
for i in list_of_names:
    bil = bil + " " + i

wordcloud = WordCloud().generate(bil)

# I show the wordcloud image

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.show()

# I change the maximum fontsize to make some words more or less prominent

wordcloud = WordCloud(max_font_size=40).generate(bil)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# In this section I generate a list of the different lengths and one of every lenght in the data

list_of_lengths = []
list_of_xlengths = []

for i in list_of_names:
    if len(i) not in list_of_xlengths:
        list_of_xlengths.append(len(i))
    list_of_lengths.append(len(i))

sorted_list_of_xlengths = sorted(list_of_xlengths)
print(sorted_list_of_xlengths)
len(list_of_lengths)

# In this part I use the findavg function to find the average name length
# Potential improvement - would be to round the value as no name is of a not int length

avg_len_name = findavg(list_of_lengths)
print(avg_len_name)

# In this part I generate a count of the total number of each name length to use for plotting later

list_of_counts_lengths = []
count = 0
for i in sorted_list_of_xlengths:
    if count != 0:
        count = 0
    for v in list_of_lengths:
        if v == i:
            count+=1
    list_of_counts_lengths.append(count)


# Here the count of each name length is plotted

fig, ax = plt.subplots()
ax.bar(sorted_list_of_xlengths, list_of_counts_lengths, width=1, edgecolor='white', linewidth=0.9)

plt.show()

#Here the findmedian function is used to find the median

median = findmedian(list_of_lengths)
print(median)

# Here I removes any duplicate name in the data, so that no name is present twice
# I then check if any values have been removed - 

new_list_of_names = []
for i in list_of_names:
    if i not in new_list_of_names:
        #print(f'The name: {i} is not in the list - appending')
        new_list_of_names.append(i)
    else:
        print("DUPLICATE!")
tjek = len(new_list_of_names)
if len(list_of_names) == len(new_list_of_names):
    print(f'There appears to be no duplicates in the data \n The length of true data is: {len(list_of_names)} \n The length of checked data is: {len(new_list_of_names)}')
print(tjek)

