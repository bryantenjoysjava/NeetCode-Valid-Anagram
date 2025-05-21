#My Thought Process:
I tried to find the most efficient solution and immediately thought of using a dictionary when given an anagram problem comparing two strings. My algorithim involves adding
the characters of string 't' as the keys in the dictionary and the occurences of each character in string 't' as the values. I then took the characters of string 's' and compared 
them to the keys in the dictionary, if they matched, I subtracted the value of that key by each occurence. I then looked at all the values of each key in the dictionary and
checked if they were all zero. If they were, then the two words are anagrams, if not, then they aren't.
