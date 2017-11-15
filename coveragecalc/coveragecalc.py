#!/usr/bin/env python3
# -*- coding: UTF8 -*-
from . fields import BINS, OUTPUTS
import pandas as pd
import warnings
warnings.filterwarnings('ignore')  # kind of bad


def vc_df(df, col):    
    """Given a df and col return a df of value counts with 
    the columns count and percentage"""
    percen = '{:.2%}'.format

    total_len = len(df)
    t = pd.DataFrame(df[col].value_counts(dropna=False))
    t.columns = ['count']
    t['percentage'] = (t['count'] / total_len).map(percen)
    t['name'] = col
    return t.sort_values(by='count', ascending=False)

def bin_col(df, col, bin_dict):
    """Returns a binned version of a Series for a given df and col"""
    labels = bin_dict['labels']
    bins = bin_dict['bins']
    if labels:
        return pd.cut(df[col], bins=bins, labels=labels, include_lowest=True, right=False)
    return pd.cut(df[col], bins=bins, include_lowest=True, right=False)

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
            
    writer.save()
