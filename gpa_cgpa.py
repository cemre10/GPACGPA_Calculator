import time

print("Welcome to GPA / CGPA Calculator! ")

def startGame():

  def gpaCalculator():
    list1 = []

    lessonNumber = int(input("How Many Lessons Do You Have?: "))
    for ch in range(0,lessonNumber):
      lessonName = input("Enter Your "+str(ch+1)+". lesson name: ")
      list1.append(lessonName)

    totalGpa = calculator(list1,False)

    print("Your GPA is: ", format(totalGpa,'.2f'))

  def cgpaCalculator():
    list5 = []
    list4 = []
    semesterNumber1 = int(input("Which semester do you in (Ex:5)?: "))
    totalCredit = 0
    totalCredit1 = 0

    if semesterNumber1 != 1:
      for ac in range(0,semesterNumber1-1):
        semesterGpa1,semesterCredit = input("Enter Your "+str(ac+1)+". semester GPA and Total Credit number: ").split()
        totalCredit = totalCredit + float(semesterCredit)
        list4.append(float(semesterCredit)*float(semesterGpa1))
    else:
      gpaCalculator()
      return

    print("Lets Calculate your "+str(semesterNumber1)+". Semester GPA to Find CGPA")

    lessonNumber1 = int(input("How Many Lessons Do You Have in your "+str(ac+2)+". Semester?: "))
    for ad in range(0,lessonNumber1):
      lessonName1 = input("Enter Your "+str(ad+1)+". lesson name: ")
      list5.append(lessonName1)
  
    totalGpa1,totalCredit1 = calculator(list5,True)

    total1 = 0
    for ah in range(0,len(list4)):
      total1 = total1 + list4[ah]
  
    total2 = total1 + totalGpa1*totalCredit1

    totalCgpa1 = total2 / (totalCredit+totalCredit1)

    print("Your "+str(semesterNumber1)+". Semester GPA is: ", format(totalGpa1,'.2f'))
    print("Your CGPA is: ", format(totalCgpa1,'.2f'))
  
  choice = input("\nType 1 for GPA, 0 for CGPA: ")
  while (choice != '1' and choice != '0' or choice.isdigit() == False):
    print("\nPlease enter 1 or 0")
    choice = input("\nType 1 for GPA,Type 0 for GPA/CGPA: ")

  else:
    if choice == '1':
      gpaCalculator()
      calculateAgain()
    elif choice == '0':
      cgpaCalculator()
      calculateAgain()

def calculateAgain():
    choice1 = input("\nDo you want to Calculate Again (Yes/No)?: ")
    choice1 = choice1.upper()
    if choice1 == "YES":
        startGame()
    else:
        print("\nGood Bye!")

def calculator(list,boolean):
  artan = 0
  list1 = []
  list2 = []

  for lh in range(0,len(list)):
    i,j = input("Enter Your "+str(list[artan])+" Lesson's Letter Grade and Credit(Leave Blank between them): ").split()
    
    j = int(j)
    i = i.upper()
    if i == "A":
        i = j*4
    elif i == "A-":
      i = j*(3.7)
    elif i=="B+":
      i = j*(3.3) 
    elif i == "B":
      i = j*(3.0)
    elif i == "B-":
      i = j*(2.70)
    elif i == "C+":
      i = j*(2.30)
    elif i == "C":
      i = j*(2.0)
    elif i == "C-":
      i = j*(1.7)
    elif i == "D":
      i = j*(1.0)
    else:
      i = 0
    list1.append(i)
    list2.append(j)
    artan = artan + 1
  
  total1 = 0
  total2 = 0

  for dh in range(0,len(list1)):
    total1 = total1 + list1[dh]

  for fh in range(0,len(list2)):
    total2 = total2 + list2[fh]

  totalGpa = total1/total2

  if boolean==False:
    return totalGpa
  else:
    return totalGpa,total2

startGame()

time.sleep(3) 