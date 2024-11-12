# Task 1: Code Correction
#  You are provided with a Python script that is supposed 
# to help in event planning, but it has errors. Identify and fix them.

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)


attendees = int(input("Enter number of attendees: ")) # <--- int needed to be added in order to 
# convert a string (question) into an integer (# of attendees)

venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to 
# recommend additional things like "audio system" or "projector" based 
# on the number of attendees.



attendees = int(input("Enter number of attendees: ")) 

venue = "large hall" if attendees > 100 else "conference room"
print(venue)


audio_by_attendance = str(input("Will you need music?"))

if attendees < 100 and audio_by_attendance == "yes":
    print("We can provide a speaker to accomodate.")
elif attendees > 100 and audio_by_attendance == "yes":
    print("We can provide a robust audio system to accomodate.")
else:
    print("No audio, no problem!")


entertainment_by_attendance = str(input("Will you need visual assistance?"))

if entertainment_by_attendance == "Yes" and attendees > 100:
    print("We can provide a live speaker or entertainer.")
elif entertainment_by_attendance == "Yes" and attendees < 100:
    print("We have a projector available if needed.")
else:
    print("No visual assistance needed, no problem!")


# Task 3: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers"
#  if yes, otherwise recommend "Gourmet Meals Caterers".

vegetarian_food = input("Would you like vegetarian food to accomodate?")
if "yes":
    print("We recommend Veggie Delight Caterers!")
else:
    print("We recommend Gourmet Meals Caterers!")