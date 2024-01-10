#!/usr/bin/env python3

import bz2
import ssl
import tarfile
from pathlib import Path
import os
from io import BytesIO
import urllib.request
from pathlib import Path
import os
import certifi
import urllib.request

def extract_bz2(archive_path, dest):
    with bz2.open(archive_path, "rb") as f:
        content = f.read()
        with open(dest, "wb") as extractedf:
            extractedf.write(content)

def extract_tar(archive_path, dest, format=""):
    with tarfile.open(archive_path, f'r:{format}') as tar:
        names = tar.getnames()
        assert len(names) == 1, "expected single archived file"
        mfile = tar.extractfile(names[0])
        with open(dest, "wb") as extractedf:
            extractedf.write(mfile.read())

def unzip(archive):
    archive_path = archive.download_path
    dest = archive.extract_dest
    ext = Path(archive_path).suffix
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if ext == '.bz2':
        stem = archive.download_path.stem
        if stem.endswith('.tar'):
            extract_tar(archive_path, dest, "bz2")
        else:
            extract_bz2(archive_path, dest)
    elif ext == '.tar':
        extract_tar(archive_path, dest)

def download_artifact(archive):
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(archive.url, context=context) as response:
        resb = BytesIO(response.read())
        os.makedirs(os.path.dirname(archive.download_path), exist_ok=True)
        with open(archive.download_path, "wb") as f:
            f.write(resb.getbuffer())

class Archive:
    def __init__(self, url, download_path, extract_dest):
        self.url = url
        self.download_path = Path(download_path)
        self.extract_dest = Path(extract_dest)

jpn_sentences = Archive('https://downloads.tatoeba.org/exports/per_language/jpn/jpn_sentences.tsv.bz2',
                        'downloads/jpn_sentences.tsv.bz2',
                        'extracted/jpn_sentences.tsv')
eng_sentences = Archive('https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences.tsv.bz2',
                        'downloads/eng_sentences.tsv.bz2',
                        'extracted/eng_sentences.tsv')
indices = Archive('https://downloads.tatoeba.org/exports/jpn_indices.tar.bz2',
                  'downloads/jpn_indices.tar.bz2',
                  'extracted/jpn_indices.csv')

archives = [jpn_sentences, eng_sentences, indices]

def get_latest(archives):
    for archive in archives:
        download_artifact(archive)
        unzip(archive)

get_latest(archives)