import re
# let's choose a file
print('What filename to analyze?')
print('(1) - regex_sum_42.txt - sample file')
print('(2) - regex_sum_1593843.txt - control file')
print('(3) - other file')
ch_num = input('Please, your choice (1-3):')
# Check our choise 1, 2 or 3
if re.search('^[1-3]$', ch_num) is None:
    print('Please, choose only digits: 1, 2 or 3')
    quit()
# try to open our file
if int(ch_num) == 1:
    try: fh = open('regex_sum_42.txt')
    except:
        print('regex_sum_42.txt is absent!')
        quit()
elif int(ch_num) == 2:
    try: fh = open('regex_sum_1593843.txt')
    except:
        print('regex_sum_1593843.txt is absent!')
        quit()
else:
    other_file = input('Input your filename:')
    try: fh = open(other_file)
    except:
        print('Your file is absent!')
        quit()
# read and analize our file
s = list()
s1 = list()
# take every line from file
for line in fh:
    fl = line.strip()
# take only digits from every line
    nums = re.findall('[0-9]+',fl)
    if not nums:
        continue
# convert all strings to integer and append in huge list
    for number in nums:
        n = int(number)
        s1.append(n)
print('The sum of the all numbers in file is: ', sum(s1))
