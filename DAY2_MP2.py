wordlist = []
while True:
    words = input("Enter a word:   ")
    wordlist.append(words)

    retry = input("Do you want to add more words? Y/N?:    ")
    if retry.upper()=="N":
        break

total = len(wordlist)
print("Total words entered: ", total)
print("List of all words in the list:   ")
for all_words in wordlist:
    print(all_words)
