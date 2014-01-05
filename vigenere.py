import string
import operator

WORDLIST_FILENAME = "words.txt"

##words.txt and load_words() code from MIT's OCW ...
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    ## inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    ## line: string
    line = inFile.readline()
    ## wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

WORDS = load_words()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

MOST_COMMON_ENG = "etnorias"

##Length of key used to encrypt ciphertext. Determines the interval length.
KEY_LENGTH = 3

CIPHERTEXT = "ctmyrdoibsresrrrijyrebyldiymlccyqxsrrmlqfsdxfowfktcyjrriqzsmx"

NUM_STR_TO_PRNT = 5

##TEST_DICT = {}#{5:[("domino", "Franciscan monks")], 3:[("gary", "Elephantitis is bad.")], 17:[("grant", "Ropes are sometimes slippery."), ("branch", "Anti-matter does not matter"), ("skills", "unknown palindrome")]} ## //DEBUGGING ONLY

##Build and return list of frequencies of letters on each interval.
def count_letters(ciphertext):
    
    ##Build list in which to store the frequencies of ciphertext letters.
    frequencies = [[0] * 26]
    for i in range(KEY_LENGTH - 1):
        frequencies.append([0] * 26)

    ##Count the frequency of appearance of each letter on each interval.
    for i in range(0, len(ciphertext)):
        frequencies[i % KEY_LENGTH][ALPHABET.index(ciphertext[i])] += 1

    return frequencies

##Build a dictionary of letters as keys and frequencies as values
##for each interval. Build a list of (letter, frequency) tuples sorted
##in descending order by frequency. Print letter frequencies. Return a string
##of the most common letter on each frequency in order.
def most_freq_letters(frequencies, printYN = False):

    mostComL = str()
    
    for i in range(0, len(frequencies)):
        frequencies[i] = dict(zip(ALPHABET, frequencies[i]))
        print "\nInterval ", i + 1, " letter frequencies:\n"
        frequencies[i] = sorted(frequencies[i].items(), None, key=operator.itemgetter(1), reverse=True)

        mostComL += ord(frequencies[i][0][0])
        
        if printYN:
            for j in frequencies[i]:
                print j[0], " = ", j[1]

    return mostComL
        

##Returns a string of the most common letter on each interval of the ciphertext.
def get_letter_freqs(ciphertext):

    return most_freq_letters(count_letters(ciphertext))

    ##For each most commonly occuring letter on each interval (in the string mostComL), assign it
    ##to each of the most commonly used English letters. For each
    ##permutation with repetition of the possible values for each letter,
    ##check that string for words in WORDS. Print only the strings with the top
    ##NUM_STR_TO_PRNT numbers of words. The human can do the rest.

    ##1 - For each KEY_LENGTH length permutation with repetition using the
    ##    alphabet MOST_COMMON_ENG, 
    ##       Meaning, for each number 0 through len(MOST_COMMON_ENG)**KEY_LENGTH,
    ##       convert that number to a tuple of base len(MOST_COMMON_ENG) numbers.
    ##       Call the tuple permutation.
    ##2 - For i in len(mostComL), calculate the shift amount needed to transform
    ##    the ciphertext letter ord(mostComL[i]) into the plaintext letter permutation[i]. Store the result
    ##    in a tuple called shifts. Create a string made of these shifts and call it keyword.
    ##3 - For i in len(ciphertext), temp += ord[ciphertext[i]] - shift amount of
    ##    (shifts index i % KEY_LENGTH).
    ##4 - For word in WORDS, if word in temp, increment wordcount by 1.
    ##5 - If wordcount > 0, append tuple of temp and keyword to list in dict
    ##    wordcountDict at key wordcount.
    ##6 - sortedWordcounts = sorted(wordCountDict, None, None, reverse=True)
    ##7 - for i in range(0, NUM_STR_TO_PRNT), try print "keyword is ", sortedWordcounts[i][0],
    ##    " for:\n", sortedWordcounts[i][1], "\n"
    ##    except (IndexError)
    ##       print "Only ", i, " results.\n"

##DEBUGGED
##Prints NUM_STR_TO_PRNT guesses in descending order.
def disp_best_guesses(bestGuesses):

    ##Creates a sorted list of tuples in form (<int>, <list> <tuple>, <tuple>, ... </list>)
    sortedGuesses = sorted(bestGuesses.items(), None, key=operator.itemgetter(0), reverse=True)

    for i in range(0, NUM_STR_TO_PRNT):
        
        try:

            keyTextList = sortedGuesses[i][1]
            
            print "\n\n======================================="
            print "Number of words: ", sortedGuesses[i][0]

            for keyTextPair in keyTextList:

                print "\n\nKey: ", keyTextPair[0]
                print "----------------------------------------"
                print "Plaintext: ", keyTextPair[1]
                
        except (IndexError):

            if (i == 0):
                print "No results."

            else:
                print "\n\n!!!"
                print "Only ", i, " results."
            
            break

##Puts the keywords that produce a plaintext containing more than one wordlist word
##into a dict.
def get_key_counts(most_common_ltrs):

    wordcountDict = dict()

    for permutation in range(0, len(MOST_COMMON_ENG) ** KEY_LENGTH):

        permutation = baseX_digs(base10Perm, len(MOST_COMMON_ENG))

        shifts = get_shifts(permutation, most_common_ltrs)

        keyword = make_keyword(shifts)

        check_guess(keyword, wordcountDict)

        ##print wordcountDict ##DEBUGGING ONLY

        

    return None ## PLACEHOLDER -- REMOVE

##Returns a list of base10 numbers that represent the place values of base10Num in base x.
##Can be used to easily treat a base10 number as if it were a base x number.
def baseX_digs(num, base, exp = 0):

    assert base > 0, "Base cannot be 0 or negative."
    
    if (num * (base ** exp) < base) and exp == 0:
        
        return [num]

    elif exp == 0:

        ##Find most significant digit.
        while num / (base ** exp) >= base:
            exp += 1

    return [num / base ** exp] + (baseX_digs(num % base ** exp, base, exp - 1))

##Returns a tuple of the shifts needed to encrypt plaintext into ciphertext.
def get_shifts(plaintext, ciphertext):

    return None

def make_keyword(shifts):

    return None

def decrypt(keyword, ciphertext = CIPHERTEXT):

    return None

##Checks how many wordlist words a keyword's plaintext has, then adds that to
##the dict of keywords if the number is at least 1.
def check_guess(keyword, keywordDict):

    plaintextGuess = decrypt(keyword)

    guessNumWords = count_words(plaintextGuess)

    if  guessNumWords > 0:

        if not keywordDict.has_key(guessNumWords):

            keywordDict[guessNumWords] = list()

        keywordDict[guessNumWords].append((keyword, plaintextGuess))

    return None
        
def count_words(text):

    return None
