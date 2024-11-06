import copy
import random

import nltk
import pandas as pd
from deep_translator import GoogleTranslator
from nltk.corpus import wordnet

# Download NLTK data if not already available
# nltk.download("wordnet")
# nltk.download("omw-1.4")

# Load the original dataset
dataset_path = "./input/deceptive-opinion-spam-corpus/deceptive-opinion.csv"
dataset = pd.read_csv(dataset_path)


# Function to replace words with synonyms
def synonym_replacement(text, num_replacements=1):
    words = text.split()
    new_text = copy.deepcopy(words)
    replacements = 0
    for i in range(len(words)):
        synonyms = wordnet.synsets(words[i])
        if synonyms:
            synonym = synonyms[0].lemmas()[0].name()
            if synonym != words[i]:  # Ensure the synonym is different
                new_text[i] = synonym
                replacements += 1
            if replacements >= num_replacements:
                break
    return " ".join(new_text)


# Function to apply back translation
def back_translation(text, source_lang="en", intermediate_lang="fr"):
    try:
        translated = GoogleTranslator(
            source=source_lang, target=intermediate_lang
        ).translate(text)
        back_translated = GoogleTranslator(
            source=intermediate_lang, target=source_lang
        ).translate(translated)
        return back_translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return the original if there's an error


# Apply augmentations
augmented_texts = []
for index, row in dataset.iterrows():
    original_text = row["text"]

    # Apply Synonym Replacement
    synonym_text = synonym_replacement(original_text)
    augmented_texts.append({**row, "text": synonym_text})

    # Apply Back Translation
    back_translated_text = back_translation(original_text)
    augmented_texts.append({**row, "text": back_translated_text})

# Create a DataFrame from the augmented data
augmented_df = pd.DataFrame(augmented_texts)

# Save the augmented dataset
output_path = "./input/deceptive-opinion-spam-corpus/deceptive-opinion-augmented.csv"
augmented_df.to_csv(output_path, index=False)

print(f"Augmented dataset saved to {output_path}")
