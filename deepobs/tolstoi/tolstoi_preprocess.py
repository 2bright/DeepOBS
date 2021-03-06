# -*- coding: utf-8 -*-
"""This is a scipt to pre-process a plain *.txt file for character-level
language modelling. It splits the the text into a train and test portion (the
size of which is determined by the --test_size argument), creates a look-up
table for the (character-level) vocabulary, and saves the 1D array of character
ids in train.npy and and test.npy files. The vocabular is also saved in a
pkl file.

The text file is assumed to be called input.txt and to reside in a folder given
by the --data_dir argument."""

import codecs
import os
import collections
from six.moves import cPickle
import numpy as np


def preprocess(file_path="", save_path="", encoding="utf-8", num_examples=0, test_size=0.2):
    # Paths for the input and output files
    input_file = os.path.join(file_path, "input.txt")
    vocab_file = os.path.join(file_path, "vocab.pkl")
    train_file = os.path.join(file_path, "train.npy")
    test_file = os.path.join(file_path, "test.npy")

    # Make sure input file exists and the npy and pkl files don't
    assert os.path.exists(input_file)
    if os.path.exists(vocab_file):
        raise ValueError("Found existing vocabulary file")
    if os.path.exists(train_file) or os.path.exists(test_file):
        raise ValueError("Found existing array file")

    # Parse text and create vocavbulary
    with codecs.open(input_file, "r", encoding=encoding) as f:
        data = f.read()
    counter = collections.Counter(data)
    count_pairs = sorted(counter.items(), key=lambda x: -x[1])
    chars, _ = zip(*count_pairs)
    print "Vocab size", len(chars)
    print type(chars)
    vocab = dict(zip(chars, range(len(chars))))

    # Save vocabulary file
    with open(vocab_file, 'wb') as f:
        cPickle.dump(chars, f)

    # Create array of chharacter ids
    array = np.array(list(map(vocab.get, data)))

    # Split in train and test and save to .npy files
    train_size = int(np.ceil((1.0 - test_size) * np.size(array)))
    train = array[0:train_size]
    test = array[train_size:]
    np.save(train_file, train)
    np.save(test_file, test)
