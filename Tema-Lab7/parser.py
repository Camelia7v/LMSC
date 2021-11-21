import json
from nltk.parse.corenlp import CoreNLPParser


def json_file_parser(file):
    with open(file) as f:
        load_file = json.load(f)
    texts_from_file = []
    for dic in load_file:
        # print(dic)
        texts_from_file.append(dic["text"])
    return texts_from_file


if __name__ == "__main__":
    # Parse a json file and extract the texts from it
    file_name = "Training data/train1.json"
    list_of_texts = json_file_parser(file_name)
    # print(len(list_of_texts), list_of_texts)

    # Start the server in the background first
    # Run the server (from the Terminal) using all jars in the CoreNLP home directory ("stanford-corenlp-4.3.1")
    # with the command below:
    # java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 50000

    # Get the phrase structure trees and write them in a file
    parser = CoreNLPParser(url='http://localhost:9000')
    f = open("phrase_structure_trees.txt", "w")
    for text in list_of_texts:
        parse = next(parser.raw_parse(text))
        f.write(str(parse) + "\n\n\n")
        # print(parse, "\n\n")
