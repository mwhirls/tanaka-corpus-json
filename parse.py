#!/usr/bin/env python3

import csv
from enum import Enum
import json
import os
import re
import constants

OUTPUT_PATH = 'dist/jpn_eng_examples.json'

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

class Word:
    def __init__(self, headword, reading, sense, surface_form, checked):
        self.headword = headword
        self.reading = reading
        self.sense = sense
        self.surface_form = surface_form
        self.checked = checked

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

def parse_word(word):
    # format "headword()[sense]": https://dict.longdo.com/about/hintcontents/tanakacorpus.html
    pattern = "^(?P<headword>[^()[\]{}]+)(?:\((?P<reading>.+)\))?(?:\[(?P<sense>.+)\])?(?:{(?P<surface_form>.+)})?(?P<checked>~)?$"
    match = re.match(pattern, word)
    assert match, "headword not found"
    return match.groupdict()

def parse_words(index):
    word_strs = index.text.split()
    return [parse_word(w) for w in word_strs]

def to_json_entry(sentence, eng_sentences_dict, indices_dict):
    try:
        index = indices_dict[sentence.id]
        translation = eng_sentences_dict[index.trans_id]
        words = parse_words(index)
        return dict(id=sentence.id, text=sentence.text, translation=translation.text, words=words)
    except KeyError:
        return None

def to_json(jpn_sentences_dict, eng_sentences_dict, indices_dict):
    entries = [to_json_entry(v, eng_sentences_dict, indices_dict) for v in jpn_sentences_dict.values()]
    return [x for x in entries if x is not None]

def write_file(json_data, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

jpn_sentences_dict = load_sentence_dict(constants.JPN_SENTENCES_PATH)
eng_sentences_dict = load_sentence_dict(constants.ENG_SENTENCES_PATH)
indices_dict = load_indices_dict(constants.INDICES_PATH)
examples_json = to_json(jpn_sentences_dict, eng_sentences_dict, indices_dict)
write_file(examples_json, OUTPUT_PATH)