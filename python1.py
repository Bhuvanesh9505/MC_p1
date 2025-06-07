mood_responses = {
    "happy": {
        "emoji": "😊",
        "message": "That's wonderful to hear! Keep shining bright!"
    },
    "sad": {
        "emoji": "😔",
        "message": "It's okay to feel sad sometimes. Remember that even the darkest clouds have a silver lining."
    },
    "angry": {
        "emoji": "😠",
        "message": "It's natural to feel angry. Take a deep breath, and remember that this feeling will pass."
    },
    "excited": {
        "emoji": "🤩",
        "message": "Awesome! Your excitement is contagious. What amazing things are you looking forward to?"
    },
    "calm": {
        "emoji": "😌",
        "message": "A calm mind is a powerful one. Enjoy this peaceful moment."
    },
    "confused": {
        "emoji": "🤔",
        "message": "Feeling a bit puzzled? Sometimes clarity comes after a good ponder. You'll figure it out!"
    }
}
default_response = {
    "emoji": "🙂",
    "message": "I don't quite recognize that mood, but I hope you find a moment of peace and joy today!"
}
user_mood_input = input("How are you feeling today? (e.g., Happy, Sad, Angry, Excited, Calm, Confused): ").lower()
response_data = mood_responses.get(user_mood_input, default_response)
print(f"\n{response_data['emoji']} {response_data['message']}")

print("\n---")
print("This program demonstrates dictionary usage, user input handling, and conditional logic.");