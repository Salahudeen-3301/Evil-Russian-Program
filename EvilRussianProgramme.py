print(
    "The evil Russian program was invented to increase the amount of pushups  you can do by up to 170%, it involves doing the maximum amount of pushups until exhaustion, and doing a perecentage of that amount everyday for two weeks with  various time intervals in between."
)

print(
    "\n WARNING:You will need to pause all upper body workouts until the end of a fortnite. You should stop an hour before sleeping to sleep comfortably. "
)

print("\nWeek one/day 1 Max pushup test")
x = int(input("Enter Max pushups: "))

print("\nDay one:", round(x * 0.3, 0), "pushups every 60 mins")
print("Day two:", round(x * 0.5, 0), "pushups every 60 mins")
print("Day three:", round(x * 0.6, 0), "pushups every 45 mins")
print("Day four:", round(x * 0.25, 0), "pushups every 60 mins")
print("Day five:", round(x * 0.45, 0), "pushups every 30 mins")
print("Day six:", round(x * 0.40, 0), "pushups every 60 mins")
print("Day seven:", round(x * 0.20, 0), "pushups every 90 mins")

print("\nWeek two/day 8 Max pushup test")
y = int(input("Enter Max pushups: "))

print("\nDay eight:", round(y * 0.35, 0), "pushups every 45 mins")
print("Day nine:", round(y * 0.55, 0), "pushups every 20 mins")
print("Day ten:", round(y * 0.30, 0), "pushups every 15 mins")
print("Day eleven:", round(y * 0.65, 0), "pushups every 60 mins")
print("Day twelve:", round(y * 0.35, 0), "pushups every 45 mins")
print("Day thirteen:", round(y * 0.45, 0), "pushups every 60 mins")
print("Day fourteen:", round(y * 0.25, 0), "pushups every 120 mins")

print(
    "\n\nGood job! you have completed the two week program, What is your new Max pushup limit?"
)
newmax = int(input("Enter Max pushups: "))

change = newmax - x
percentage = change / x * 100
if percentage >= 170:
    print("Congatulations you have improved by", round(percentage, 2), "%")
else:
    print("Keep pushing!")
