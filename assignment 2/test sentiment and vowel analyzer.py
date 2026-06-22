#Write a function -analyze_text_sentiment(text) that:
#- Counts positive words(good,great, happy, excellent, love, etc) and negative words.
# counts vowels and consonants 
# detects if text has a "vowel runs"(3+ vowels in a row).
# returns a sentiment score and full statistics 

#Create a second function - conpare_texts(text 1, text2) that compares two texts and prints which one is more positive.

#Test with your favorite song lyrics, a motivational quote, and a complaint message.
# Topics:
   
   
   # function to analyze text sentiment
def analyze_text_sentiment(text):
    positive_words = {"good", "fine", "happy", "excellent", "love","amazing","strong", "win"}
    negative_words = {"bad", "sad" "hate","terrible", "pain", "angry", "worst", "fail"}
    words = text.lower().split()
    positive_count = 0
    negative_count = 0
    vowels = 0
    consonants = 0
    vowel_run = False
    vowel_letters = "aeiou"
    current_run = 0

    # counting the positive and negative words:
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    # loop to count vowels, consonants and check vowel runs
    for letter in text.lower():
        if letter.isalpha():
            if letter in vowel_letters:
                vowels += 1
                current_run += 1
                if current_run >= 3:
                    vowel_run = True
            else:
                consonants += 1
                current_run = 0

    # Sentiment score
    score = positive_count - negative_count
    return {"Positive words": positive_count,"Negative words": negative_count,
            "vowels": vowels, "consonants": consonants, "vowel run found": vowel_run,
            "sentiment score": score}

    # Function to compare two texts
def compare_texts(text1, text2):
        result1 = analyze_text_sentiment(text1)
        result2 = analyze_text_sentiment(text2)

        print("\nText 1 Score:", result1["sentiment score"])
        print("text 2 score:", result2["sentiment score"])

        if result1["sentiment score"] > result2["sentiment score"]:
            print("text 1 is more positive")
        elif result2["sentiment score"] > result1["sentiment score"]:
            print("text 2 is more positive")
        else:
            print("Both texts are equally positive")

# Test samples
song_lyrics = "I thought this love would never end, you never told me"
motivational_quote = "A stitch in time saves nine"
complaint = "This is the worst feeling i've had in a very long time"

# analysing each text
print("Song Lyrics Analysis:")
print(analyze_text_sentiment(song_lyrics))

print("\nMotivational Quote Analysis:")
print(analyze_text_sentiment(motivational_quote))

print("\nComplaint Analysis:")
print(analyze_text_sentiment(complaint))

# Compare Texts
compare_texts(song_lyrics, motivational_quote,)
compare_texts(motivational_quote, complaint)
