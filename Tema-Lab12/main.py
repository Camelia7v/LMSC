import spacy
from spacy import displacy
import os.path
from pathlib import Path
from nltk.parse.stanford import StanfordDependencyParser
import stanza
from graphviz import Source
# stanza.download('en')


sentences = ['I saw the lady on the hill.', 'We ate octopus and shells for dinner.', 'Anna and Peter saw us.']


"""
Method 1: Using spaCy
"""

print('Method 1: Using spaCy\n')

# Load the language model
nlp = spacy.load("en_core_web_sm")

count = 1
for sentence in sentences:
    # nlp function returns an object with individual token information, linguistic features and relationships
    doc = nlp(sentence)

    print("{:<15} | {:<8} | {:<15} | {:<20}".format('Token', 'Relation', 'Head', 'Children'))
    print("-" * 70)

    for token in doc:
        # Print the token, dependency nature, head and all dependents of the token
        print("{:<15} | {:<8} | {:<15} | {:<20}"
              .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])))

    # Use displayCy to visualize the dependency
    svg = spacy.displacy.render(doc, style="dep")
    output_path = Path(os.path.join("./", f"sentence{count}.svg"))
    output_path.open('w', encoding='utf-8').write(svg)
    count += 1

    print('\n')


"""
Method 2: Using NLTK with Stanford CoreNLP
"""

print('\nMethod 2: Using NLTK with Stanford CoreNLP\n')

# Path to CoreNLP jar unzipped
jar_path = './stanford-corenlp-4.3.1/stanford-corenlp-4.3.1.jar'

# Path to CoreNLP model jar
models_jar_path = './stanford-corenlp-4.3.1/stanford-corenlp-4.3.1-models.jar'

# Initialize StanfordDependency Parser from the path
parser = StanfordDependencyParser(path_to_jar=jar_path, path_to_models_jar=models_jar_path)

count = 1
for sentence in sentences:
    # Parse the sentence
    result = parser.raw_parse(sentence)
    dependency = result.__next__()

    print("{:<15} | {:<10} | {:<10} | {:<15} | {:<10}".format('Head', 'Head POS', 'Relation', 'Dependent', 'Dependent '
                                                                                                           'POS'))
    print("-" * 75)

    # Use dependency.triples() to extract the dependency triples in the form
    # ((head word, head POS), relation, (dependent word, dependent POS))
    for dep in list(dependency.triples()):
        print("{:<15} | {:<10} | {:<10} | {:<15} | {:<10}"
              .format(str(dep[0][0]), str(dep[0][1]), str(dep[1]), str(dep[2][0]), str(dep[2][1])))

    dot_def = dependency.to_dot()
    # source = Source(dot_def, filename=f"dependency_graph{count}", format="svg")
    # source.view()
    output_path = Path(os.path.join("./", f"dependency_graph{count}.txt"))
    output_path.open('w', encoding='utf-8').write(dot_def)
    count += 1

    print('\n')


"""
Method 3: Using Stanza
"""

print('\nMethod 3: Using Stanza\n')

nlp = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma,depparse')

for sentence in sentences:
    doc = nlp(sentence)

    # Print the dependencies of the first sentence in the doc object
    # Format: Token, Index of head, Nature of dependency
    # Index starts from 1, 0 is reserved for ROOT
    doc.sentences[0].print_dependencies()

    print("{:<15} | {:<10} | {:<15} ".format('Token', 'Relation', 'Head'))
    print("-" * 50)

    # Convert sentence object to dictionary
    sent_dict = doc.sentences[0].to_dict()

    # Iterate to print the token, relation and head
    for word in sent_dict:
        print("{:<15} | {:<10} | {:<15} "
              .format(str(word['text']), str(word['deprel']),
                      str(sent_dict[word['head'] - 1]['text'] if word['head'] > 0 else 'ROOT')))

    print('\n')
