import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Garden path sentences
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nOriginal sentence: {sentence}")
    
    # Tokenization
    print("\nTokenization:")
    for token in doc:
        print(token.text, end=' | ')

    # Named Entity Recognition
    print("\nNamed Entity Recognition:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})", end=' | ')

    # Print explanations for entities
    for ent in doc.ents:
        print(f"\nEntity Explanation for {ent.text}: {spacy.explain(ent.label_)}")

# Look up and print explanations for additional entities if needed
# print(spacy.explain("FAC"))  # Uncomment and replace "FAC" with the actual entity you want to look up

# Comments about two entities looked up
"""
Entity 1:
- What was the entity and its explanation that you looked up?
  Entity: GPE (Geopolitical Entity)
  Explanation: Countries, cities, states.

- Did the entity make sense in terms of the word associated with it?
  Yes, it makes sense. For example, in the sentence "The cotton clothing is made of grows in Mississippi," 'Mississippi' is correctly identified as a geopolitical entity.

Entity 2:
- What was the entity and its explanation that you looked up?
  Entity: ORG (Organization)
  Explanation: Companies, agencies, institutions, etc.

- Did the entity make sense in terms of the word associated with it?
  Yes, it makes sense. For example, in the sentence "Mary gave the child a Band-Aid," 'Band-Aid' is correctly identified as an organization, even though it might be more commonly associated with a product.
"""
