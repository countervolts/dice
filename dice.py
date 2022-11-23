import random
odds = 0 
evens = 0 
total = 0

def dice_rolls (trials) :
  global odds
  global evens
  global total
  for i in range(trials) :
    roll = random.randint (1,6) #Roll
    if roll % 2 == 0:
      evens += 1
    else:
      odds+= 1
    total += 1
  print ('Odds: '+ str(odds))
  print ('Evens: '+ str(evens))
  
dice_rolls (100)
prob_even = (evens/total)*100

print(prob_even)
