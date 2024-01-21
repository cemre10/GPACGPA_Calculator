import time


print("Welcome to GPA / CGPA Calculator! ")

def startGame():

  def gpaCalculator():
  
    list3 = []
    list2 = []
    list1 = []

    lessonNumber = int(input("How Many Lessons Do You Have?: "))
    for ch in range(0,lessonNumber):
      lessonName = input("Enter Your "+str(ch+1)+". lesson name: ")
      list3.append(lessonName)

    artan = 0

    for lh in range(0,len(list3)):
      i,j = input("Enter Your "+str(list3[artan])+" Lesson's Letter Grade and Credit(Leave Blank between them): ").split()
      
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


    totalGpa = total1 / total2

    print("Your GPA is: ", format(totalGpa,'.2f'))

  def cgpaCalculator():
    list7 = []
    list6 = []
    list5 = []
    list4 = []
    semesterNumber1 = int(input("Which semester do you in (Ex:5)?: "))
    totalCredit = 0
    totalCredit1 = 0
    for ac in range(0,semesterNumber1-1):
      semesterName1,semesterCredit = input("Enter Your "+str(ac+1)+". semester GPA and Total Credit number: ").split()
      totalCredit = totalCredit + float(semesterCredit)
      list4.append(float(semesterCredit)*float(semesterName1))

    print("Lets Calculate your "+str(semesterNumber1)+". Semester GPA to Find CGPA")

    lessonNumber1 = int(input("How Many Lessons Do You Have in your "+str(ac+2)+". Semester?: "))
    for ad in range(0,lessonNumber1):
      lessonName1 = input("Enter Your "+str(ad+1)+". lesson name: ")
      list5.append(lessonName1)
  
    artan1 = 0

    for ae in range(0,len(list5)):
      m,n = input("Enter Your "+str(list5[artan1])+" Lesson's Letter Grade and Credit(Leave Blank between them): ").split()
      
      totalCredit1 = float(n) + totalCredit1
      n = int(n)
      m = m.upper()
      if m == "A":
          m = n*4
      elif m == "A-":
        m = n*(3.7)
      elif m=="B+":
        m = n*(3.3) 
      elif m == "B":
        m = n*(3.0)
      elif m == "B-":
        m = n*(2.70)
      elif m == "C+":
        m = n*(2.30)
      elif m == "C":
        m = n*(2.0)
      elif m == "C-":
        m = n*(1.7)
      elif m == "D":
        m = n*(1.0)
      else:
        m = 0
      list6.append(m)
      list7.append(n)
      artan1 = artan1 + 1
  
    total3 = 0
    total4 = 0

    for af in range(0,len(list6)):
      total3 = total3 + list6[af]

    for ag in range(0,len(list7)):
      total4 = total4 + list7[ag]

    totalGpa1 = total3 / total4
    

    total5 = 0

    for ah in range(0,len(list4)):
      total5 = total5 + list4[ah]
  
    total6 = total5 + totalGpa1*totalCredit1
    print(total5,totalCredit1,total6)
    

    totalCgpa1 = total6 / (totalCredit+totalCredit1)

    print("Your "+str(semesterNumber1)+". Semester GPA is: ", format(totalGpa1,'.2f'))
    print("Your CGPA is: ", format(totalCgpa1,'.2f'))
  
  choice = input("\nType 1 for GPA,Type 0 for GPA-CGPA: ")

  

  while choice.isdigit() == False:
    print("\nPlease enter 1 or 0")
    choice = input("\nType 1 for GPA,Type 0 for GPA/CGPA: ")

  while (choice != '1' and choice != '0'):
    print("\nPlease enter 1 or 0")
    choice = input("\nType 1 for GPA,Type 0 for GPA/CGPA: ")

  else:
    if choice == '1':
      gpaCalculator()
      playAgain()
    elif choice == '0':
      cgpaCalculator()
      playAgain()
    else:
      print("ERROR404")




def playAgain():
    choice1 = input("\nDo you want to Calculate Again (Yes/No)?: ")
    choice1 = choice1.upper()
    if choice1 == "YES":
        startGame()
    else:
        print("\nGood Bye!")

startGame()

time.sleep(3) 