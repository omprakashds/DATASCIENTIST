#creating a mindlab game
def mindlab():
  Noun = input("Enter a noun: ")
  Verb = input("Enter a verb: ")
  Adjective = input("Enter an adjective: ")
  Adverb = input("Enter an adverb: ")
  return f"Do you {Verb} your {Adverb} {Adjective} {Noun}? That's hilarious!
result = mindlab()
print(result)