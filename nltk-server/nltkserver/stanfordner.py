from nltk.tag.stanford import StanfordNERTagger
from helpers import ret_success
from helpers import ret_failure
from os.path import exists


def tagger(data):
    print(exists('./Skola/exjobb/nltk-server/nltk-data/StanfordNER/english.all.3class.distsim.crf.ser.gz'))
    try:
        st = StanfordNERTagger('./Skola/exjobb/nltk-server/nltk-data/StanfordNER/english.all.3class.distsim.crf.ser.gz',
                               './Skola/exjobb/nltk-server/nltk-data/StanfordNER/stanford-ner.jar')
    except:
        return ret_failure(705)
    try:
        tag = st.tag(data.split())
    except:
        return ret_failure(702)
    return ret_success(tag)
