#!/usr/bin/env python3


print("Here are the results from your last workout")
print("--------------------")

f = open("latest.txt", "r")
print(f.read())



class Workout(object):
    def __init__(self, exercise, weight, reps):
        self.exercise = exercise
        self.d = {}
        self.weight = weight
        self.reps = reps
    def __str__(self):
        r = []
        r.append(f'Exercise: {self.exercise}')
        r.append(f'Weight: {self.weight} KG')
        r.append(f'Reps: {self.reps}')
        return '\n'.join(r)
f = open("latest.txt", "w")
a = []
q = input("Add an exercise? (Y/N) ")
while q != "N":
   if q == "Y":
      ex = input("Exercise: ")
      f.write(ex + '\n')
      wght = input("Weight: ")
      f.write(wght + " KG" +'\n')
      rps = input("Reps: ")
      f.write(rps + " reps" + '\n' + '\n')
      a.append(Workout(ex, wght, rps))
      q = input("Add an exercise? (Y/N) ")
f.close()
print("Workout results" + "\n" + "-------------")
for e in a:
    print(e)
