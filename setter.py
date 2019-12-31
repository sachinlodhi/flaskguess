def let_set(word,space,letter):
   for i in range(len(word)):
      if letter == word[i]:
         space[i] = letter
   print(space)
   return space