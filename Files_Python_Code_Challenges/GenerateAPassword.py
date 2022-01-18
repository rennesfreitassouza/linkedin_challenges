import secrets
import string


# https://www.linkedin.com/learning/python-code-challenges/generate-a-password
def randomWord(myDict, numberOfDices=5):
    myKey = str()
    while(numberOfDices > 0):
        myKey += secrets.choice(string.digits)  # 1:7])
        numberOfDices -= 1
    try:
        return myDict[myKey]
    except KeyError as k:
        print(f'{str(k)}', end=' ')
        return randomWord(myDict)


def t(numberOfWords):
    with open("diceware.wordlist.asc") as fp:
        myDict = dict()
        for line in fp.readlines():
            numberAndWord = line.split('\t')
            myDict[numberAndWord[0]] = numberAndWord[1][:-1]

        myListOfWords = list()
        [myListOfWords.append(randomWord(myDict))
         for i in range(numberOfWords)]

        myDiceWare = ' '.join(myListOfWords)
        return myDiceWare


def main(numberOfWords=1):
    passphrase = t(numberOfWords)
    print(passphrase)


if __name__ == '__main__':
    main()
