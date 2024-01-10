#!/usr/bin/env python3

import csv
from enum import Enum

class SentenceField(str, Enum):
    ID = 'id'
    LANG = 'lang'
    TEXT = 'text'

class Sentence:
    def __init__(self, id, text):
        self.id = id
        self.text = text

JPN_SENTENCES_PATH = 'extracted/jpn_sentences.tsv'
ENG_SENTENCES_PATH = 'extracted/eng_sentences.tsv'

def load_sentences(tsv_path):
    with open(tsv_path, "r", encoding="utf-8") as tsvf:
        reader = csv.DictReader(tsvf, fieldnames=[SentenceField.ID, SentenceField.LANG, SentenceField.TEXT], delimiter="\t")
        sentences = map(lambda row: Sentence(row[SentenceField.ID], row[SentenceField.TEXT]), reader)
        return list(sentences)

jpn_sentences = load_sentences(JPN_SENTENCES_PATH)
eng_sentences = load_sentences(ENG_SENTENCES_PATH)