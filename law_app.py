from flask import Flask, request, render_template
import spacy
import os  # Import os module

app = Flask(__name__)  

nlp = spacy.load('en_core_web_sm')

legal_sections = {
    'missing': 'Section 359 IPC - Kidnapping',
    'theft': 'Section 378 IPC - ',
    'assault': 'Section 351 IPC - Assault',
    'fraud': 'Section 420 IPC - Fraud',
    'theft': 'Section 378 IPC - Theft',
    'steal': 'Section 378 IPC - Theft',
    'robbery': 'Section 378 IPC - Theft',
    'larceny': 'Section 378 IPC - Theft',
    'shoplifting': 'Section 378 IPC - Theft',
    'assault': 'Section 351 IPC - Assault',
    'attack': 'Section 351 IPC - Assault',
    'hit': 'Section 351 IPC - Assault',
    'battery': 'Section 351 IPC - Assault',
    'violence': 'Section 351 IPC - Assault',
    'murder': 'Section 302 IPC - Murder',
    'kill': 'Section 302 IPC - Murder',
    'homicide': 'Section 302 IPC - Murder',
    'manslaughter': 'Section 304 IPC - Manslaughter',
    'cheating': 'Section 415 IPC - Cheating',
    'deceit': 'Section 415 IPC - Cheating',
    'fraud': 'Section 420 IPC - Fraud',
    'scam': 'Section 420 IPC - Fraud',
    'deception': 'Section 420 IPC - Fraud',
    'embezzlement': 'Section 405 IPC - Criminal Breach of Trust',
    'forgery': 'Section 463 IPC - Forgery',
    'identity theft': 'Section 66C IT Act - Identity Theft',
    'bribery': 'Section 7 PCA - Bribery',
    'extortion': 'Section 383 IPC - Extortion',
    'harassment': 'Section 509 IPC - Word, gesture or act intended to insult the modesty of a woman',
    'kidnapping': 'Section 359 IPC - Kidnapping',
    'abduction': 'Section 362 IPC - Abduction',
    'stalking': 'Section 354D IPC - Stalking',
    'criminal trespass': 'Section 441 IPC - Criminal Trespass',
    'insider trading': 'Securities and Exchange Board of India Act - Insider Trading',
    'malpractice': 'Section 304A IPC - Causing death by negligence',
    'misrepresentation': 'Section 18 of the Indian Contract Act - Misrepresentation',
    'false information': 'Section 177 IPC - False Information',
    'defamation': 'Section 499 IPC - Defamation',
    'public nuisance': 'Section 268 IPC - Public Nuisance',
    'trespass': 'Section 441 IPC - Criminal Trespass',
    'cybercrime': 'IT Act - Cybercrime',
    'domestic violence': 'Protection of Women from Domestic Violence Act',
    'sex trafficking': 'Section 370 IPC - Trafficking of Persons',
    'child exploitation': 'Section 373 IPC - Buying Minor for Prostitution',
    'obscenity': 'Section 292 IPC - Obscenity',
    'hate speech': 'Section 153A IPC - Promoting Enmity between Different Groups',
    'terrorism': 'Unlawful Activities (Prevention) Act - Terrorism',
    'money laundering': 'Prevention of Money Laundering Act - Money Laundering',
    'corporate fraud': 'Companies Act - Corporate Fraud',
    'negligence': 'Section 304A IPC - Causing death by negligence',
    'wrongful confinement': 'Section 340 IPC - Wrongful Confinement',
    'child abuse': 'Juvenile Justice Act - Child Abuse',
    'drug trafficking': 'Narcotic Drugs and Psychotropic Substances Act - Drug Trafficking',
    'environmental crime': 'Environment Protection Act - Environmental Crime',
    'manslaughter': 'Section 304 IPC - Manslaughter',
    'cheating': 'Section 415 IPC - Cheating',
    'deceit': 'Section 415 IPC - Cheating',
    'scam': 'Section 420 IPC - Fraud',
    'deception': 'Section 420 IPC - Fraud',
    'embezzlement': 'Section 405 IPC - Criminal Breach of Trust',
    'forgery': 'Section 463 IPC - Forgery',
    'identity theft': 'Section 66C IT Act - Identity Theft',
    'bribery': 'Section 7 PCA - Prevention of Corruption Act',
    'extortion': 'Section 383 IPC - Extortion',
    'harassment': 'Section 509 IPC - Insulting the Modesty of a Woman',
    'kidnapping': 'Section 359 IPC - Kidnapping',
    'abduction': 'Section 362 IPC - Abduction',
    'stalking': 'Section 354D IPC - Stalking',
    'criminal trespass': 'Section 441 IPC - Criminal Trespass',
    'insider trading': 'Securities and Exchange Board of India Act - Insider Trading',
    'malpractice': 'Section 304A IPC - Causing Death by Negligence',
    'misrepresentation': 'Section 18 of the Indian Contract Act - Misrepresentation',
    'false information': 'Section 177 IPC - False Information',
    'defamation': 'Section 499 IPC - Defamation',
    'public nuisance': 'Section 268 IPC - Public Nuisance',
    'trespass': 'Section 441 IPC - Criminal Trespass',
    'cybercrime': 'IT Act - Cybercrime',
    'domestic violence': 'Protection of Women from Domestic Violence Act',
    'sex trafficking': 'Section 370 IPC - Trafficking of Persons',
    'child exploitation': 'Section 373 IPC - Buying a Minor for Prostitution',
    'obscenity': 'Section 292 IPC - Obscenity',
    'hate speech': 'Section 153A IPC - Promoting Enmity between Different Groups',
    'terrorism': 'Unlawful Activities (Prevention) Act - Terrorism',
    'money laundering': 'Prevention of Money Laundering Act - Money Laundering',
    'corporate fraud': 'Companies Act - Corporate Fraud',
    'negligence': 'Section 304A IPC - Causing Death by Negligence',
    'wrongful confinement': 'Section 340 IPC - Wrongful Confinement',
    'child abuse': 'Juvenile Justice (Care and Protection of Children) Act - Child Abuse',
    'drug trafficking': 'Narcotic Drugs and Psychotropic Substances Act - Drug Trafficking',
    'environmental crime': 'Environment Protection Act - Environmental Crime',
}

def extract_keywords(complaint):
    doc = nlp(complaint)
    keywords = [token.text.lower() for token in doc if token.pos_ in ['NOUN', 'VERB']]
    matched_sections = [legal_sections.get(word) for word in keywords if word in legal_sections]
    return matched_sections

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        complaint = request.form["complaint"]
        sections = extract_keywords(complaint)
        return render_template("index.html", sections=sections, complaint=complaint)
    return render_template("index.html", sections=[], complaint="")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)), debug=True)

