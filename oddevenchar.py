'''printing out even and odd characters from the string with each input  '''
n = int(input())
# s = string.split()
for j in range(n):

    string = input()
    # s = string.split()
    odd_ = ''
    even_ = ''

    for index in range(len(string)):
        if index % 2 != 0:
            odd_ += string[index]
        else:
            even_ += string[index]
    stdout = even_  + " " + odd_
    print(stdout)
