# string = input()
# even_string = ''
# odd_string = ''
# for index in range(len(string)):
#     if index % 2 != 0:
#         odd_string = odd_string + string[index]
#     else:
#         even_string = even_string + string[index]
#
# print(odd_string + " " + even_string)
# # modified_string = string.split()
# # for s in modified_string:
# #     c_even = s[0::2]
# #     c_odd = s[1::2]
# #     stdout = c_odd + " " + c_even
# #     print(stdout)
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
