#KMP Algorithm

def KMPFind(pattern, word):
    P = len(pattern)
    W = len(word)
    #this will define the length of the pattern and the letter
    
    lps = [0]*P
    #LPS stands for the longest prefix that is also a suffix
    #so it is created to hold the longest prefix suffix
    j = 0   #index for pattern[]

    computeLPSArray(pattern, P, lps)
    #preprocess the pattern, means calculating the lps[] array using the fuction created below

    pattern_found = False

    i = 0  #index for word[]
    while i < W:
        if pattern[j] == word[i]:  #if the words are the same then i and j will increment by 1
            j += 1
            i += 1
        else:
            if j != 0:
              j = lps[j - 1]  #to continue finding patterns
            else:
                i += 1 #if there is no matches in the first index then it will compare to the next one after it finds a match
        if j == P:
            print("Same pattern is found at index " + str(i - j))
            j = lps[j - 1]  #to continue finding patterns
            pattern_found = True

    #show message if pattern is not found in word
    if not pattern_found:
        print("Pattern not found in the word.")



#Below is the fuction to compute the LPS array
def computeLPSArray(pattern, P, lps):
    len = 0  #length of the previous longest prefix suffix
    #However it is set to 0 as there is nothing computed yet
    lps[0] = 0
    i = 1

    while i < P:
        #this loop will calculate for i = 1 and P - 1(Reason for P - 1 as index starts from 0)
        if pattern[i] == pattern[len]:
            len += 1   #This is how they check the pattern with each index
            lps[i] = len
            i += 1
        else:
            if len != 0:  #if the current length doesn't match this check the previous index
                len = lps[len - 1]
            else:
                lps[i] = 0  #if everything doesn't match it will go back to the first index and start comparing from the first index and the letter that has mismatched will be 0
                i += 1


word = "APPLSAPPLEAPPLESD"
pattern = "APPLES"
KMPFind(pattern,word)