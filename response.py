import random

name = "Bot"
mood = ["Happy", "Enthusiastic", "Sad"]

responses = {

    "greetings": [
        'hey',
        'hello',
        'greetings',
        'I\'m glad! You are talking to me'
    ],

    "what's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "My name is the {0}".format(name)
    ],

    "are you a robot?": [
        "What do you think?",
        "Maybe yes, maybe no!",
        "Yes, I am a robot with human feelings.",
    ],

    "how are you?": [
        "I am feeling {0}".format(random.choice(mood)),
        "{0}! How about you?".format(random.choice(mood)),
        "I am {0}! How about yourself?".format(random.choice(mood)),
    ],

    "calculate": [
        "Yes I can do add, sub, mul"
    ],

    "addition": [
        "Done with addition, want to calculate something else"
    ],

    "subtraction": [
        "Done with subtraction"
    ],

    "multiplication": [
        "Done with multiplication"
    ],

    "": [
        "Sorry I didn't catch it"
    ],
    
    "default": [
        "Say something which I can understand"
    ]

}