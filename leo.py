import spacy

# Load SpaCy's small English model
nlp = spacy.load('en_core_web_sm')

# A simple dictionary mapping keywords to legal sections
legal_sections = {
    'theft': 'Section 378 IPC - Theft',
    'assault': 'Section 351 IPC - Assault',
    'murder': 'Section 302 IPC - Murder',
    'kill': 'Section 302 IPC - kill',
    'cheating': 'Section 415 IPC - Cheating',
    'fraud': 'Section 420 IPC - Fraud',
}

def extract_keywords(complaint):
    # Process the complaint with SpaCy
    doc = nlp(complaint)
    
    # Extract the relevant legal keywords (nouns and verbs)
    keywords = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'VERB']]
    
    # Match the extracted keywords to legal sections
    matched_sections = []
    for word in keywords:
        if word in legal_sections:
            matched_sections.append(legal_sections[word])
    
    return matched_sections

# Get complaint input from the user
complaint = input("Please enter your complaint: ")

# Extract relevant sections from the complaint
sections = extract_keywords(complaint)

if sections:
    print("Relevant Legal Sections:", sections)
else:
    print("No matching legal sections found.")
