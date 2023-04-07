def isVowel(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    if string in vowel:
        return True
    else:
        return False

def minion(string):
    # Stuart counts the number of word starting with consonants
    # Kevin counts the number of word starting with vowels
    stuart, kevin = 0, 0
    for i in range(len(string)):
        if isVowel(string[i]):
            kevin += len(string[i:])
        else:
            stuart += len(string[i:])
    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")

minion("BANANA")