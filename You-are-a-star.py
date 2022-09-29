import os
#os.system('cls')

import random

adjectives = {'a': ["Ambitious", "Amazing", "Awesome"], 
              'b': ["Bright", "Brilliant", "Best"], 
              'c': ["Charming", "Curious", "Courageous", "Compassionate", "Clever"], 
              'd': ["Diligent", "Determined", "Devoted"], 
              'e': ["Enthusiastic", "Excellent", "Extraordinary", "Empathatic"], 
              'f': ["Fantastic", "Fun", "Funny", "Flexible"], 
              'g': ["Generous", "Great", "Genius", "Gorgeous"], 
              'h': ["Happy", "Hillarious", "Honest"], 
              'i': ["Inventive", "Intelligent", "Innovative"], 
              'j': ["Jolly", "Joyful", "Jovial"], 
              'k': ["Kind", "Keen", "Knowlegeable"], 
              'l': ["Likable", "Lovable", "Lively"], 
              'm': ["Merry", "Magnificent", "Marvelous"], 
              'n': ["Nice", "Noble", "Nimble"], 
              'o': ["Observant", "Open", "Ornate"], 
              'p': ["Passionate", "Positive", "Perfect", "Posh", "Pretty"], 
              'q': ["Quick", "Quiet", "Quirky"], 
              'r': ["Reliable", "Rightful", "Resourceful", "Responsible"], 
              's': ["Super", "Supportive", "Sincere"], 
              't': ["Trustable", "Truthful", "Topper"], 
              'u': ["Unparalleled", "Useful", "Upstanding", "Upright"], 
              'v': ["Viligant", "Valuable", "Vivid"], 
              "w": ["Wonderful", "Wise", "Wholehearted"], 
              'x': ["X-factor", "Xanthic", "Xenial"], 
              'y': ["Youthful", "Young", "Yare", "Yern"], 
              'z': ["Zestful", "Zealous", "Zappy"]}
              
string = input()
string = string.lower()
for i in range(len(string)):
  words = adjectives[string[i]]
  word = random.choice(words)
  print(word[0], word[1:])