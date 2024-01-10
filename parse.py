#!/usr/bin/env python3

import csv
from enum import Enum
import json

JPN_SENTENCES_PATH = 'extracted/jpn_sentences.tsv'
ENG_SENTENCES_PATH = 'extracted/eng_sentences.tsv'
INDICES_PATH = 'extracted/jpn_indices.csv'

class SentenceField(str, Enum):
    ID = 'id'
    LANG = 'lang'
    TEXT = 'text'

class IndexField(str, Enum):
    SENTENCE_ID = 'id'
    TRANSLATION_ID = 'trans_id'
    TEXT = 'text'

class Sentence:
    def __init__(self, id, text):
        self.id = id
        self.text = text

class Index:
    def __init__(self, id, trans_id, text):
        self.id = id
        self.trans_id = trans_id
        self.text = text

def load_sentences(tsv_path):
    with open(tsv_path, "r", encoding="utf-8") as tsvf:
        reader = csv.DictReader(tsvf, fieldnames=[SentenceField.ID, SentenceField.LANG, SentenceField.TEXT], delimiter="\t")
        sentences = map(lambda row: Sentence(row[SentenceField.ID], row[SentenceField.TEXT]), reader)
        return list(sentences)
    
def load_indices(tsv_path):
    with open(tsv_path, "r", encoding="utf-8") as tsvf:
        reader = csv.DictReader(tsvf, fieldnames=[IndexField.SENTENCE_ID, IndexField.TRANSLATION_ID, IndexField.TEXT], delimiter="\t")
        indices = map(lambda row: Index(row[IndexField.SENTENCE_ID], row[IndexField.TRANSLATION_ID], row[IndexField.TEXT]), reader)
        return list(indices)
    
def to_dict(sentences):
    tuples = map(lambda s: (s.id, s), sentences)
    return dict(list(tuples))

def load_sentence_dict(path):
    sentences = load_sentences(path)
    return to_dict(sentences)

def load_indices_dict(path):
    indices = load_indices(path)
    return to_dict(indices)

def to_json_entry(sentence, eng_sentences_dict, indices_dict):
    try:
        index = indices_dict[sentence.id]
        translation = eng_sentences_dict[index.trans_id]
        return dict(id=sentence.id, transId=translation.id, text=sentence.text, translationText=translation.text)
    except KeyError:
        return None

def to_json(jpn_sentences_dict, eng_sentences_dict, indices_dict):
    entries = [to_json_entry(v, eng_sentences_dict, indices_dict) for v in jpn_sentences_dict.values()]
    return [x for x in entries if x is not None]

jpn_sentences_dict = load_sentence_dict(JPN_SENTENCES_PATH)
eng_sentences_dict = load_sentence_dict(ENG_SENTENCES_PATH)
indices_dict = load_indices_dict(INDICES_PATH)
examples_json = to_json(jpn_sentences_dict, eng_sentences_dict, indices_dict)
print(json.dumps(examples_json))