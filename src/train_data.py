#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Liguo Chen'
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import cross_val_score


def train_data(x, y):
    clf = MultinomialNB()
    clf.fit(x, y)
    return clf


def test_model(m, x, y):
    f1 = cross_val_score(m, x, y, cv=4, scoring='f1').mean()
    acc = cross_val_score(m, x, y, cv=4, scoring='accuracy').mean()
    recall = cross_val_score(m, x, y, cv=4, scoring='recall').mean()
    print "%s f1:%s" % ("NB", str(f1))
    print "%s acc:%s" % ("NB", str(acc))
    print "%s recall:%s" % ("NB", str(recall))
