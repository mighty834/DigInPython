# Write function for two strings merging in this way:
# take first letter from string with lower length,
# then take first letter from another string,
# then second from first string again etc.
# Finally concatenate remains letters from greater
# string to end of result string.

def strMerge(str1, str2):
    str_result = ""
    min_length = min(len(str1), len(str2))

    greater_str = ""
    if (len(str1) > len(str2)):
        greater_str = str1
    else:
        greater_str = str2

    for i in range(0, min_length):
        str_result += str1[i]
        str_result += str2[i]

    str_result += greater_str[min_length:]

    return str_result

str1 = "abcd"
str2 = "efghijkl"
print(strMerge(str1, str2)) # Must be "aebfcgdhijkl"

