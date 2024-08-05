from convokit import Corpus, download
import pandas as pd

# Load the Friends TV show dataset
corpus = Corpus(filename=download("friends-corpus"))

# Extract dialogues
utterances = list(corpus.iter_utterances())
data = [(utt.speaker.id, utt.text) for utt in utterances if utt.speaker.id and utt.text]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["speaker", "text"])

# Display basic info
print(f"Number of utterances: {len(df)}")
print(df.head())

# Preprocess the dialogues into input-output pairs
def preprocess_data(df):
    # Create pairs of dialogues
    dialogue_pairs = []
    for i in range(len(df) - 1):
        if df.iloc[i]["speaker"] != df.iloc[i + 1]["speaker"]:
            dialogue_pairs.append((df.iloc[i]["text"], df.iloc[i + 1]["text"]))
    return dialogue_pairs

dialogue_pairs = preprocess_data(df)
print(f"Number of dialogue pairs: {len(dialogue_pairs)}")

