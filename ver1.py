qest = input("Good day! would you like to know your recommended exercises?(yes/no) ")

if qest.upper() == "YES":

    print("Please input your vital stastistics in inches.")
    Shoulder = float(input("Shoulder Size: "))
    Bust = float(input("Bust Size: "))
    Waist = float(input("Waist Size: "))
    Hips = float(input("Hips Size: "))

    Shoulderfit = 16
    Bustfit = 37
    Waistfit = 24
    Hipsfit = 37

    #Shoulder
    if (Shoulder < Shoulderfit):
        print('''
Recommended Exercises for Small Shoulder:
    Lateral Raise: 15 reps (3 sets)
    Overhead Press: 15 reps (3 sets)
    Arnold Press: 15 reps (3 sets)
    Rear Delt Raise: 10 reps (3 sets)
              ''')
    elif (Shoulder > Shoulderfit):
        print('''
Recommended Exercises for Big Shoulder:
    Lateral Raise: 25 reps (3 sets)
    Overhead Press: 25 reps (3 sets)
    Arnold Press: 25 reps (3 sets)
    Rear Delt Raise: 15 reps (3 sets)
              ''')
    else:
        print("Your shoulder is fit!")

    if (Bust < Bustfit):
        print('''
Recommended Exercises for Small Bust:
    DB Peck Fly: 15 reps (3 sets)
    Plank Shoulder Tap Rotations: 15 reps (3 sets)
    Tricep Dips: 15 reps  (3 sets)
    DB Bent Over Row: 15 reps (3 sets)
              ''')
    elif (Bust > Bustfit):
        print('''
Recommended Exercises for Big Bust:
    DB Peck Fly: 10 reps (3 sets)
    Plank Shoulder Tap Rotations: 10 reps (3 sets)
    Tricep Dips: 10 reps  (3 sets)
    DB Bent Over Row: 10 reps (3 sets)
              ''')
    else:
        print("Your bust is fit!")


    if (Waist < Waistfit):
        print('''
Recommended Exercises for Small Waist:
    High Knees: 60 sec (3 sets)
    Reverse Lunges: 60 sec per side (3 sets)
    Crunches: 30 reps (3 sets)
    Leg extensions: 30 reps (3 sets)
              ''')
        
    elif (Waist > Waistfit):
        print('''
Recommended Exercises for Big Waist:
    High Knees: 30 sec (3 sets)
    Reverse Lunges: 30 sec per side (3 sets)
    Crunches: 15 reps (3 sets)
    Leg extensions: 15 reps (3 sets)
              ''')
    else:
        print("Your waist is fit!")
    
    if (Hips < Hipsfit):
        print('''
Recommended Exercises for Small Hips:
    Squats: 25 reps (3 sets)
    Lateral Set ups: 25 reps per side (3 sets)
    Donkey Kicks: 25 reps per side (3 sets)
    Fire Hydrants: 25 reps per side (3 sets)
              ''')
    if (Hips > Hipsfit):
        print('''Recommended Exercises for Big Hips:
    Squats: 10 reps (3 sets)
    Lateral Set ups: 10 reps per side (3 sets)
    Donkey Kicks: 15 reps per side (3 sets)
    Fire Hydrants: 15 reps per side (3 sets)
              ''')
              
    else:
        print("Your hips is fit!")

else:
    print("Thank you!")


