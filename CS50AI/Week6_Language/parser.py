NONTERMINALS = """
S -> NP VP

NP -> N | Det N | Det AP N | NP PP
VP -> V | V NP | VP PP | VP Conj VP

AP -> Adj | Adj AP
PP -> P NP
"""

def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Split into tokens
    tokens = nltk.word_tokenize(sentence)

    # Filter words without alphabet
    filtered = []
    for token in tokens:
        if any(c.isalpha() for c in token):
            filtered.append(token.lower())
    return filtered


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    chunks = []

    # Get all subtrees
    nps = tree.subtrees(filter=lambda t: t.label() == 'NP')
    for np in nps:

        # If only 1 child means itself
        np_childs = np.subtrees(filter=lambda t: t.label() == 'NP')
        length = 0
        for _ in np_childs:
            length += 1
            if length > 1:
                break

        # If no child with NP
        if length == 1:
            chunks.append(np)
    return chunks