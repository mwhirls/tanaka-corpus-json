#!/usr/bin/env python3

import csv
from enum import Enum

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

JPN_SENTENCES_PATH = 'extracted/jpn_sentences.tsv'
ENG_SENTENCES_PATH = 'extracted/eng_sentences.tsv'
INDICES_PATH = 'extracted/jpn_indices.csv'

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

jpn_sentences = load_sentences(JPN_SENTENCES_PATH)
eng_sentences = load_sentences(ENG_SENTENCES_PATH)
indices = load_indices(INDICES_PATH)