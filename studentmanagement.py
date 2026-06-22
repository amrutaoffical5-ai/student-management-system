student = []

while True:
  print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
  print("1. ADD STUDENT IN SYSTEM")
  print("2. VIEW STUDENT IN SYSTEM")
  print("3. SEARCH STUDENT IN SYSTEM")
  print("4. DELETE STUDENT FROM SYSTEM")
  print("5. EXIT")

  try:
    choice = int(input("ENTER CHOICE: "))
  except ValueError:
    print("INVALID INPUT! PLEASE ENTER A NUMBER")
    continue

  if choice == 1:
    name = input("ENTER NAME OF STUDENT: ")
    student.append(name)
    print("STUDENT ADDED")

  elif choice == 2:
    print("\nStudent List:")
    for s in student:
      print(s)

  elif choice == 3:
    search_name = input("ENTER NAME TO SEARCH: ")
    if search_name in student:
      print("STUDENT FOUND")
    else:
      print("STUDENT NOT FOUND")

  elif choice == 4:
    name = input("ENTER NAME OF STUDENT TO DELETE: ")
    if name in student:
      student.remove(name)
      print("STUDENT NAME DELETED SUCCESSFULLY")
    else:
      print("STUDENT NAME NOT FOUND IN SYSTEM")

  elif choice == 5:
    print("GOODBYE ThankYOU!")
    break

  else:
    print("INVALID CHOICE! PLEASE TRY AGAIN")

