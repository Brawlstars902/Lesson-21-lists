def match_words(words):
   cntr=0
   lst=[]
   for word in words:
      if len(word)>1 and word[0]==word[-1]:
         cntr+=1
         lst.append(word)
   print('\nThe words that have the first and last letters the same of the list, ',words,',are: ',lst)
   return cntr

count=match_words(['drd','fbi','madam','adam','the','that'])
print('\nThe number of words the have the first and last letters as the same letter is',count,)

