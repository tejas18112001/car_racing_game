
print("##***********************Quiz********************##")
print("welcome")
print("---------------------------------------------------------------------")
students_name=input("Enter your name:")
input("Enter your register no.:")
input("Enter your roll no :")
input("Your class and division:")
print("Hello {}, welcome to quiz, best of luck, perform good" .format(students_name))
print("Lets start to solve")
print("----------------------------------------------------------------------")
from quize import instructions
print(instructions)

print("-----------------------------------------------------------------------")
from quize import que_dict

import time

time.sleep(3)


print("\n Ready")
time.sleep(1)
print("\n 3")
time.sleep(1)
print(" \n 2")
time.sleep(1)

print(" \n 1")
time.sleep(1)
print("\n Go")
start=time.time()
print("------------------------------------------------------------------------")

#duration=time.time()-start

score=0
for key in que_dict:

      print(key)

      ans=input("Enter the option:")


      if ans==que_dict[key]:
          score+=1
      else:
          score-=1
print("-------------------------------------------------------------------------------------")
print("Your final score is:" ,score)
print("your duration is",time.time()-start,"sec") # this calculate time duration of students
print("-------------------------------------------------------------------------------------")


print("--------------------------:Thanks:-----------------------------")

import numpy as np
import matplotlib.pyplot as plt

s=[1,2,3,4]
t=[5,6,7]
plt.pyplot(s,t)

plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('student performance')
#plt.legend(['Sine', 'Cosine'])
plt.show()