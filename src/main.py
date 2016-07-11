#! /home/chen/anaconda2/envs/tensor/bin/python
# -*- coding:utf-8 -*-
__author__ = 'Liguo Chen'
from preprocessing import *
from extract_features import *
from train_data import *
import time


def main():
    start = time.time()
    reviews = segment_reviews()
    print "total time cost:%.2fs, preprocess finished." % \
          (time.time() - start)
    if k_button['self_def']:
        # [[[vector], ..], []]
        matrix = extract_features(reviews)
        print "total time cost:%.2fs, extract features finished." % \
              (time.time() - start)
        x, y = transform_data(matrix)
        model = train_data(x, y)
        test_model(model, x, y)
    else:
        # tf-idf feature
        x = extract_tfidf_features(reviews)
        y = [0.0] * (x.shape[0] / 2) + [1.0] * (x.shape[0] / 2)
        model = train_data(x, y)
        test_model(model, x, y)


if __name__ == '__main__':
    main()
