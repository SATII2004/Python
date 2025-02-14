import random

# Dictionary to store mood-based song recommendations
songs = {
    "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Uptown Funk - Mark Ronson ft. Bruno Mars"],
    "sad": ["Someone Like You - Adele", "Let Her Go - Passenger", "Fix You - Coldplay"],
    "energetic": ["Eye of the Tiger - Survivor", "Stronger - Kanye West", "Titanium - David Guetta ft. Sia"],
    "relaxed": ["Weightless - Marconi Union", "Sunflower - Post Malone", "Better Together - Jack Johnson"]
}

# Get user input
mood = input("How are you feeling today? (happy, sad, energetic, relaxed): ").strip().lower()

# Suggest a song based on mood
if mood in songs:
    recommended_song = random.choice(songs[mood])
    print(f"You should listen to: {recommended_song} 🎵")
else:
    print("Sorry, I don't have recommendations for that mood. Try happy, sad, energetic, or relaxed!")
