#!//usr/local/bin/python3
import nltk as nl
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import argparse
from nltk.corpus import stopwords
def parse_args():
        parser=argparse.ArgumentParser( description ='supply string to be lemmatized')
        parser.add_argument('--string',required=True)
        return parser.parse_args()

def lemma(string):
 lemmatizer = WordNetLemmatizer()
 words=nl.word_tokenize(string)
 i=0
 tokens=[]
 stop_words = set(stopwords.words('english'))
 for j in words:
 	if j not in stop_words:
 		tokens.append('post~'+lemmatizer.lemmatize(j))
 		i=i+1
 		if i>4: break
 return tokens


def main():
        args = parse_args()
        lemma(args.string)


if __name__ == "__main__":
        main()
