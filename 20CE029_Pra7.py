# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Pra7/blob/main/20CE029_Pra7.py


# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 

# Input: 
# 6 
# gaga 
# abcde 
# rotor 
# xyzxy 
# abbaab 
# ababc 

# Output: 
# YES 
# NO 
# YES 
# YES 
# NO 
# NO


n = int(input())

for i in range(n):
    word = input()
    length = len(word)
    if length % 2 == 0:
        if sorted(word[:length//2]) == sorted(word[length//2:]):
            print("YES")
        else:
            print("NO")
    else:
        if sorted(word[:length//2]) == sorted(word[length//2+1:]):
            print("YES")
        else:
            print("NO")
