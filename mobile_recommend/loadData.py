#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import datetime

def load_data():
    start = datetime.datetime.now()
    print 'loading data...'
    path = '/local/Tianchi/data/fresh_comp_offline/tianchi_fresh_comp_train_user.csv'
    df = pd.read_csv(path)
    end = datetime.datetime.now()
    print 'loading finished, cost', (end - start).seconds, 'seconds'
    return df

# 统计分析
def statistic():
    df = load_data()
    print 'users', len(df.drop_duplicates('user_id'))
    print 'items', len(df.drop_duplicates('item_id'))
    print 'behavior type', len(df.drop_duplicates('behavior_type'))
    print 'item category', len(df.drop_duplicates('item_category'))
    print 'time', len(df.drop_duplicates('time'))



if __name__ == '__main__':
    statistic()