# Solution 1
def anagram(word1, word2):
    if word1 == word2:
        return False
    elif len(word1) != len(word2):
        return False
    else:
        word2 = list(word2)
        for i in word1:
            if i not in word2:
                return False
            else:
                word2.remove(i)
    return True

wrd1 = input("Enter the first word: ")
wrd2 = input("Enter the second word: ")

result = anagram(wrd1, wrd2)

if result:
    print(f"{wrd1} and {wrd2} are anagrams")
else:
    print(f"{wrd1} and {wrd2} are not anagrams")

# Solution 2
def anagram():
    x = input("enter a string")
    y = input("enter another string")
    if sorted(x) == sorted(y):
        print("anagram")
    else:
        print("not anagram")
anagram()

# Solution 3:
def charcters_count(s):
    counts={}
    for ch in s:
        if ch in counts:
            counts[ch]=counts[ch]+1
        else:
            counts[ch] = 1
    return counts

wrd1 = input("Enter the first word: ")
wrd2 = input("Enter the second word: ")
counts1=charcters_count(wrd1)
counts2=charcters_count(wrd2)

if counts1==counts2:
    print('anagrams')
else:
    print('Not anagrams')