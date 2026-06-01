import random

import random

routines = {
    "stressed": {
        "skincare": ["Clay mask to clear your mind", "Green tea toner and moisturizer", "Pore cleansing strip and serum"],
        "music": ["Lo-fi beats", "Rain sounds", "Soft jazz"],
        "snack": ["Chamomile tea and dark chocolate", "Warm honey lemon water", "Granola and yogurt"],
        "activity": ["Journal your thoughts for 10 minutes", "Do a 5 minute breathing exercise", "Take a slow walk outside"],
        "affirmation": ["You are doing better than you think.", "One step at a time is enough.", "You are allowed to rest."]
    },
    "sad": {
        "skincare": ["Hydrating sheet mask", "Rose water mist and lip balm", "Calming aloe vera gel"],
        "music": ["Soft piano", "Lana Del Rey", "Taylor Swift sad era"],
        "snack": ["Hot chocolate and cookies", "Warm soup", "Ice cream and your favorite snack"],
        "activity": ["Watch your comfort show", "Reread your favorite book", "Write a letter to yourself"],
        "affirmation": ["It's okay to feel everything. This will pass.", "You are loved more than you know.", "Healing is not linear and that is okay."]
    },
    "tired": {
        "skincare": ["Eye patches and moisturizer", "Overnight sleeping mask", "Gentle cleanse and face oil"],
        "music": ["Sleep sounds", "ASMR", "Calm instrumentals"],
        "snack": ["Warm milk and honey", "Banana and peanut butter", "Herbal tea and crackers"],
        "activity": ["Stretch for 5 minutes then rest", "Take a long warm shower", "Lie down and do nothing guilt free"],
        "affirmation": ["Rest is productive. You deserve to recharge.", "Your body is telling you something. Listen.", "Doing less is sometimes doing enough."]
    },
    "happy": {
        "skincare": ["Glow serum and face massage", "Vitamin C serum and sunscreen", "Brightening mask and eye cream"],
        "music": ["Feel good pop", "Your hype playlist", "Dance hits"],
        "snack": ["Fruit platter or smoothie", "Popcorn and lemonade", "Your favorite treat"],
        "activity": ["Dance, call a friend, or do something creative", "Start that project you've been putting off", "Go outside and enjoy the day"],
        "affirmation": ["You deserve every good thing coming your way.", "Your joy is contagious and beautiful.", "Keep going, everything is falling into place."]
    }
}

print("** Welcome to Your Self Care Night Generator **")
print("Let's build your perfect self care routine!")
print("")
print("How are you feeling? (stressed / sad / tired / happy)")
print("")
mood = input("I am feeling: ").lower()

if mood in routines:
    routine = routines[mood]

    skincare = random.choice(routine["skincare"])
    music = random.choice(routine["music"])
    snack = random.choice(routine["snack"])
    activity = random.choice(routine["activity"])
    affirmation = random.choice(routine["affirmation"])

    print("")
    print("~ Your Self Care Night ~")
    print("")
    print("Skincare  : " + skincare)
    print("Music     : " + music)
    print("Snack     : " + snack)
    print("Activity  : " + activity)
    print("")
    print("Tonight's affirmation:")
    print(affirmation)
    print("")

else:
    print("")
    print("Oops! Please type one of these: stressed, sad, tired, happy")