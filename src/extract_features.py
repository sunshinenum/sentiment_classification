#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Liguo Chen'
import math
import sys
sys.path.append("..")
from conf.conf import *
import numpy as np
import time


def extract_features(reviews):
    """
    extract features from reviews.
    :param reviews:[[positive reviews], [negative reviews]]
    :return:[[positive reviews features], [negative reviews features]]
    """
    # score = (count1 + count2) / (count1 * count2 + 1.0) * log(count1 + count2)
    # {word:score, ..}
    scores = dict()
    # [{word:count, ..}, {word:count, ..}]
    counts = []
    # [[words], [words]]
    words = []
    # [{}, {}]
    words_bag = []
    # [[[words], ..], [[words], ..]]
    struct_words = []
    start = time.time()
    for reviews_tmp in reviews:
        words_tmp = []
        words_bag_tmp = set()
        structured_words_tmp = []
        for review in reviews_tmp:
            words_in_one_review = review.split(" ")
            structured_words_tmp.append(words_in_one_review)
            words_bag_tmp = words_bag_tmp | set(words_in_one_review)
            words_tmp += words_in_one_review
        words.append(words_tmp)
        words_bag.append(words_bag_tmp)
        struct_words.append(structured_words_tmp)
    print "split words cost:%.2fs" % (time.time() - start)
    start = time.time()
    # get counts
    for words_tmp in words:
        counts_tmp = dict()
        get = counts_tmp.get
        for word in words_tmp:
            counts_tmp[word] = get(word, 0) + 1
        counts.append(counts_tmp)
    write_out(counts[0])
    words_all = words_bag[0] | words_bag[1]
    print "count words cost:%.2fs" % (time.time() - start)
    start = time.time()
    for word in words_all:
        # count1, count2
        count12 = [0, 0]
        for index, counts_tmp in enumerate(counts):
            if word in counts_tmp:
                count12[index] = counts_tmp[word]
        # score
        score = get_score(count12)
        scores[word] = score
    scores = sorted(scores.iteritems(), key=lambda d: d[1], reverse=True)[:k_features]
    # write_out(dict(scores))
    print "caculate score cost:%.2fs" % (time.time() - start)
    start = time.time()
    # generate vectors
    # [[[], ..], [[], ..]]
    vectors = []
    for structured_words_tmp in struct_words:
        vectors_tmp = []
        for review_words in structured_words_tmp:
            vector = gen_vector(review_words, dict(scores))
            vectors_tmp.append(vector)
        vectors.append(vectors_tmp)
    print "generate vectors cost:%.2fs" % (time.time() - start)
    return vectors


def get_score(count12):
    score = sum(count12) * 1.0 / (count12[0] * count12[1] + 1.0) * \
           math.log(count12[0] + count12[1])
    return score


def gen_vector(words, scores):
    vector = []
    for word, score in scores.items():
        if word in words:
            vector.append(score)
        else:
            vector.append(0.0)
    return vector


def transform_data(matrix):
    x = matrix[0] + matrix[1]
    y = [0.0] * len(matrix[0]) + [1.0] * len(matrix[0])
    x = np.array(x)
    return x, y


def extract_tfidf_features(reviews):
    all_reviews = reviews[0] + reviews[1]
    from sklearn.feature_extraction.text import *
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(all_reviews)
    tfidf_transformer = TfidfTransformer(use_idf=k_button['tf-idf'])
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    return X_train_tfidf


def write_out(features_dict):
    os.chdir(k_tmp_path)
    f = open("word_bag.txt", "w")
    for word, score in features_dict.items():
        f.write("%s,%s\n" % (word.encode('utf8'), str(score).encode('utf8')))
    f.close()
