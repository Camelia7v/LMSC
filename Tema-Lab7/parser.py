import os
import json
from nltk.parse.corenlp import CoreNLPServer
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
    # print(len(list_of_texts))

    # The server needs to know the location of the following files:
    #   - stanford-corenlp-X.X.X.jar
    #   - stanford-corenlp-X.X.X-models.jar
    STANFORD = os.path.join("stanford-corenlp-4.3.1")

    # Create the server
    server = CoreNLPServer(
        os.path.join(STANFORD, "stanford-corenlp-4.3.1.jar"),
        os.path.join(STANFORD, "stanford-corenlp-4.3.1-models.jar"),
    )

    # Start the server in the background
    server.start()
    print("The server started in the background...")
    print("Wait for the phrase structure tree(s)...")

    for text in list_of_texts:
        parser = CoreNLPParser()
        parse = next(parser.raw_parse(text))
        print(parse, "\n\n")

    # Stop the CoreNLP server
    server.stop()
