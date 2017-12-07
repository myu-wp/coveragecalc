#!/usr/bin/env python3
# -*- coding: UTF8 -*-
from . fields import BINS, CATEGORIES, OUTPUTS
import pandas as pd
from pandas.api.types import CategoricalDtype
import warnings
warnings.filterwarnings('ignore')  # kind of bad


def vc_df(df, col):    
    """Given a df and col return a df of value counts with 
    the columns count and percentage"""
    percen = '{:.2%}'.format

    total_len = len(df)
    t = pd.DataFrame(df[col].value_counts(dropna=False, sort=False))
    t.columns = ['count']
    t['percentage'] = (t['count'] / total_len).map(percen)
    t['name'] = col
    return t

def bin_col(df, col, bin_dict):
    """Returns a binned version of a Series for a given df and col"""
    labels = bin_dict['labels']
    bins = bin_dict['bins']
    if labels:
        return pd.cut(df[col], bins=bins, labels=labels, include_lowest=True, right=False)
    return pd.cut(df[col], bins=bins, include_lowest=True, right=False)

def to_category(df, c, cat_list, thresh=0.5):
    """Given a df and col name, return Series (col) as a categorical dtype if
    a certain portion of values are unique out of the whole Series, else return
    Series unchanged. Defaults to 50% threshold."""
    unique_vals = len(df[c].unique())
    total_vals = len(df)
    cat_type = CategoricalDtype(cat_list, ordered=True)
    if unique_vals / total_vals < thresh:
        return df[c].astype(cat_type)
    return df[c]

def main(args):
    """Export coverage calc xlsx document"""
    df = pd.read_csv(args.infile) if args.infile.endswith('csv') else pd.read_excel(args.infile)
    df.columns = map(str.lower, df.columns)

    # bin cols
    for col in BINS:
        try:
            new_col = col + ' binned'
            df[new_col] = bin_col(df, col, BINS[col])
        except KeyError:
            print(f'{col} not found...skipping.')
            pass

    # convert objs to (ordered) categorical types
    for k, v in CATEGORIES.items():
        try:
            df[k] = to_category(df, k, v)
        except KeyError:
            print(f'{k} not found...skipping.')
            pass

    # export to xlsx
    writer = pd.ExcelWriter(args.outfile, engine='openpyxl')
    
    count = 0
    for o in OUTPUTS:
        try:
            t = vc_df(df, o)
            t.to_excel(writer, sheet_name='coverage', startrow=count, na_rep='NULL')
            count += len(t) + 2
        except KeyError:
            print(f'{o} not found...skipping.')
            pass
    writer.active = 0
    writer.save()
    writer.close()