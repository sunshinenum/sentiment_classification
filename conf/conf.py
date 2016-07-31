#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Liguo Chen'
import os


root = os.getcwd().replace(os.getcwd().split("/")[-1], "")
print root
# book_data_path = "%sdata/Dangdang_Book_4000" % root
# book_data_path = "%sdata/txt_sentoken" % root
# book_data_path = "%sdata/Jingdong_NB_4000" % root
book_data_path = "%sdata/Ctrip_htl_ba_4000" % root
k_tmp_path = "%stmp" % root
k_features = 12500
k_is_chinese = True
k_button = {'tf': True, 'tf-idf': False, 'self_def': False}
