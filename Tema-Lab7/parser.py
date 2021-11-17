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
    file_name = "Training data/train2.json"
    list_of_texts = json_file_parser(file_name)
    # print(len(list_of_texts), list_of_texts)

    # Get the phrase structure trees
    parser = CoreNLPParser()
    for text in list_of_texts:
        parse = next(parser.raw_parse(text))
        print(parse, "\n\n")
