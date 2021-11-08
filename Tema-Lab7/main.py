import nltk


print("Phrase structure tree(s) for 'I saw the lady on the hill'")

groucho_grammar1 = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'I'
VP -> VP PP
VP -> VBD NP
VBD -> 'saw'
NP -> NP PP
NP -> DT NN
DT -> 'the'
NN -> 'lady'
NN -> 'hill'
PP -> P NP
P -> 'on'
""")

sent1 = ['I', 'saw', 'the', 'lady', 'on', 'the', 'hill']
parser = nltk.ChartParser(groucho_grammar1)
for tree in parser.parse(sent1):
    print(tree)


print("\n\n Phrase structure tree(s) for 'We ate octopus and shells for dinner'")

groucho_grammar2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'We'
VP -> VP NP
VP -> VBD NP
VBD -> 'ate'
NP -> NP CONJ NP
NP -> N
N -> 'octopus' | 'shells'
CONJ -> 'and'
NP -> DT NN
DT -> 'for'
NN -> 'dinner'
""")

sent2 = ['We', 'ate', 'octopus', 'and', 'shells', 'for', 'dinner']
parser = nltk.ChartParser(groucho_grammar2)
for tree in parser.parse(sent2):
    print(tree)


print("\n\n Phrase structure tree(s) for 'Anna and Peter saw us'")

groucho_grammar3 = nltk.CFG.fromstring("""
S -> NP VP
NP -> NP CONJ NP
NP -> N
N -> 'Anna' | 'Peter'
CONJ -> 'and'
VP -> V P
V -> 'saw'
P -> 'us'
""")

sent3 = ['Anna', 'and', 'Peter', 'saw', 'us']
parser = nltk.ChartParser(groucho_grammar3)
for tree in parser.parse(sent3):
    print(tree)
