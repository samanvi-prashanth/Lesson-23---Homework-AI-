# NOTE SORTER
# ---------- SETUP (given to you) ----------
BOXES = {
    "Sports": "the team won the football match and the crowd cheered the goal "
              "she runs fast in the race and wins the gold medal for the team",
    "Food": "we cook pasta with tomato sauce and the soup is hot "
            "he bakes bread and the cake tastes sweet with cream",
    "Music": "the band plays a loud song and the singer sings with the guitar "
             "she learns the piano and sings a song in the choir",
}

TEST_NOTES = [
    ("the goal won the match", "Sports"),
    ("he bakes the cake and the bread", "Food"),
    ("the singer plays the guitar", "Music"),
    ("pasta with sweet cream", "Food"),
    ("the band wins the match", "Music"),
    ("", "unknown"),
]

THRESHOLD = 0.2

# ---------- PART 1: count the words ----------
def word_counts(text):
    counts = {}
    # YOUR CODE HERE
    # For each word of text.split(), add 1 to counts[word].
    # A word you have not seen yet starts at 0: use counts.get(word, 0).
    for word in text.split() :
        counts[word] = counts.get(word, 0) + 1
    return counts

PROFILES = {box: word_counts(text) for box, text in BOXES.items()}
print("PART 1: Word counts")
print(PROFILES["Food"].get("the", 0), PROFILES["Food"].get("goal", 0))

# ---------- PART 2: compare two word counts ----------
def cosine(a, b):
    # YOUR CODE HERE
    # dot: for each word in a, add a[word] * b.get(word, 0)
    # size_a: the sum of count * count for every count in a, then ** 0.5. Do the same for size_b.
    # If either size is 0, return 0.0. Otherwise return dot / (size_a * size_b).
    dot = 0
    for word in a :
        dot = dot + a[word] * b.get(word, 0)
    size_a = sum(count * count for count in a.values())**0.5
    size_b = sum(count * count for count in b.values())**0.5
    return 0.0 if size_a == 0 or size_b == 0 else dot / (size_a * size_b)

print("\nPART 2: Cosine")
print(round(cosine(word_counts("the team"), PROFILES["Sports"]), 2))

# ---------- PART 3: find the best box ----------
def classify(note):
    # YOUR CODE HERE
    # Count the words of the note. Compare them with every box in PROFILES using cosine.
    # Keep the box with the highest score.
    # If the best score is below THRESHOLD, return "unknown". Otherwise return the box.
    mystery = word_counts(note)
    best_box = "unknown"
    best_score = 0
    for box, profile in PROFILES.items() :
        score = cosine(mystery, profile)
        if score > best_score :
            best_box = box
            best_score = score
    return "unknown" if best_score < THRESHOLD else best_box

print("\nPART 3: Classify")
print(classify("the goal won the match"), "|", classify("zzz"))

# ---------- PART 4: check every test note ----------
print("\nPART 4: Test all notes")
mistakes = 0
# YOUR CODE HERE
# For each (note, wanted) pair: get the answer from classify, add 1 to mistakes
# if it is not the wanted one, and print the answer and the note on one line.
# After the loop, print: Mistakes: <number> out of <total>
for note, wanted in TEST_NOTES :
    answer = classify(note)
    if answer != wanted :
        mistakes += 1
    print(answer,"-",repr(note))
print(f"Mistakes : {mistakes} out of {len(TEST_NOTES)}")