#! /home/chen/anaconda2/envs/tensor/bin/python
# -*- coding:utf-8 -*-
import jieba
import sys
sys.path.append("..")
from conf.conf import *
import os
__author__ = 'Liguo Chen'


def segment_reviews():
    """
    segment reviews and return reviews list.
    :return:[[],[]]
    """
    # read data
    os.chdir(book_data_path)
    folders = os.listdir(".")
    tagged_reviews = []
    for folder in folders:
        os.chdir(folder)
        os.system("enca -L zh_CN -x UTF8 *")
        reviews_tmp = []
        review_files = os.listdir(".")
        for file_name in review_files:
            f = open(file_name, "r")
            review = f.read()
            # segmentation if text is chinese
            if k_is_chinese:
                seg_list = jieba.cut(review, cut_all=False)
                review = " ".join(seg_list)
            reviews_tmp.append(review)
            f.close()
        os.chdir("..")
        tagged_reviews.append(reviews_tmp)
    return tagged_reviews
