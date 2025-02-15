import random
words = [
    'apple', 'house', 'dance', 'light', 'table', 'water', 'chair', 'block', 'stone', 'cloud',
    'bread', 'watch', 'plant', 'round', 'green', 'heart', 'sleep', 'quick', 'peace', 'dream',
    'funny', 'music', 'sharp', 'money', 'fruit', 'grass', 'lucky', 'blank', 'road', 'coin',
    'train', 'brush', 'clown', 'bird', 'scale', 'stick', 'fight', 'shout', 'smell', 'twirl',
    'cake', 'pearl', 'stone', 'glove', 'plaza', 'tiger', 'grape', 'mango', 'rainy', 'clear',
    'piano', 'light', 'smile', 'shine', 'smell', 'tease', 'pluck', 'shock', 'plant', 'truck',
    'glove', 'blaze', 'vocal', 'spine', 'spark', 'score', 'horse', 'drown', 'press', 'slide',
    'clash', 'bride', 'brake', 'bloom', 'flame', 'drive', 'wrist', 'sweep', 'flock', 'swirl',
    'watch', 'group', 'claim', 'fence', 'charm', 'swoop', 'bloom', 'swing', 'loose', 'pluck',
    'grasp', 'whisk', 'storm', 'thump', 'glove', 'shoes', 'brush', 'stone', 'loose', 'swear',
    'reach', 'paint', 'leafy', 'tough', 'jolly', 'quiet', 'hello', 'laugh', 'straw', 'freed',
    'laser', 'flute', 'grove', 'sight', 'pouch', 'alert', 'vocal', 'mood', 'crawl', 'cloud',
    'dove', 'chime', 'cover', 'globe', 'ocean', 'flick', 'cliff', 'glint', 'track', 'shift',
    'roast', 'vowel', 'punch', 'laugh', 'pout', 'clean', 'jumpy', 'peach', 'shift', 'stone',
    'chunk', 'froze', 'fruit', 'blaze', 'plaza', 'loud', 'frost', 'stamp', 'crisp', 'grasp',
    'loop', 'style', 'dare', 'quick', 'blink', 'blind', 'loud', 'grip', 'sore', 'shock',
    'brace', 'pearl', 'swipe', 'heart', 'flush', 'clamp', 'chalk', 'roast', 'flame', 'swoop',
    'cliff', 'flip', 'trip', 'brand', 'light', 'sweep', 'mark', 'charm', 'blend', 'punch',
    'touch', 'blend', 'stamp', 'shout', 'wrist', 'tease', 'score', 'empty', 'shine', 'stack',
    'flock', 'brace', 'crown', 'shift', 'chose', 'loud', 'grate', 'night', 'plant', 'sound',
    'spoke', 'spin', 'flop', 'snap', 'noble', 'shard', 'empty', 'track', 'blaze', 'print',
    'clear', 'flick', 'whale', 'poise', 'sweep', 'wrist', 'screw', 'glide', 'grove', 'bliss',
    'grip', 'pouch', 'whisk', 'peach', 'twist', 'blunt', 'brisk', 'tune', 'gloom', 'pouch',
    'race', 'flap', 'blast', 'grin', 'swoop', 'brash', 'blaze', 'brunt', 'shade', 'sore',
    'flash', 'light', 'crown', 'round', 'moat', 'tide', 'voice', 'plan', 'crush', 'stamp',
    'grace', 'steel', 'grip', 'vocal', 'sweat', 'dare', 'flash', 'clam', 'star', 'alert',
    'touch', 'leaf', 'spike', 'bride', 'golf', 'load', 'race', 'quiz', 'flip', 'bird', 'back',
    'study', 'flute', 'grasp', 'stare', 'ride', 'step', 'blunt', 'boot', 'bore', 'block', 'grip'
]
# Randomly choose a word
word = random.choice(words)
word = "grasp"
# Initialize the guessed word display
guessed_word = ['_'] * len(word)
# Set the number of attempts
attempts = 5

# Fun intro message
print("🎉 Welcome to Wordle! 🎉")
print("Guess the 5-letter word! 🌟")
print("You have 5 attempts to guess it right... no pressure! 😜")

# Main game loop
while attempts > 0:
    # Ask for a guess
    print(f"\nAttempts left: {attempts}")
    print(f"Current guess: {' '.join(guessed_word)}")
    print("Enter a 5-letter word: ", end="")
    guess = input().lower()

    # Check if the guess is correct
    if guess == word:
        print("🎉 Amazing! You got it! 🎉")
        print("You're a Wordle wizard! 🧙‍♂️✨")
        break
    else:
        # Check each letter of the guess
        for i in range(len(guess)):
            if word[i] in guess:
                guessed_word[i] = word[i]  # Correct letter, correct position!
        
        # Fun hint: Show the guessed word with revealed letters
        print("Hmm... not quite! But you're getting closer! 😅")
        print(f"Current word: {' '.join(guessed_word)}")
        
    # Reduce attempts after each guess
    attempts -= 1

# End of the game - reveal the word
if attempts == 0 and ''.join(guessed_word) != word:
    print(f"\nOops! You're out of attempts. The word was: {word}")
    print("Better luck next time! You can do it! 😎")
