import os

import numpy as np
import pandas as pd
from project2 import config as cfg
from project2 import z5445967_project2 as pj

tickers = [tic.lower() for tic in list(cfg.TICMAP.keys())]



if __name__ == "__main__":
    # Q1: Which stock in your sample has the highest average daily return for the
    #     year 2020 (ignoring missing values)? The sample should include all tickers
    #     included in the dictionary config.TICMAP. Your answer should include the
    #     ticker for this stock.
    Q1_ANSWER = 'TSLA'

    df = pj.mk_ret_df(pj.mk_prc_df(tickers, prc_col='adj_close'))
    avg_2020 = {}
    for tic in tickers:
        avg_2020[tic] = pj.get_avg(df, tic, 2020)
    max_tic = max(avg_2020, key=avg_2020.get)
    print(f'The answer of Q1 is {max_tic}, with average return in 2020 is {avg_2020[max_tic]}')



    # Q2: What is the annualised return for the EW portfolio of all your stocks in
    # the config.TICMAP dictionary from the beginning of 2010 to the end of 2020?
    Q2_ANSWER = '0.20435428936872047'

    ann_ret = pj.get_ann_ret(pj.get_ew_rets(df, tickers), start='2010', end='2020')
    print(f'The answer of Q2 is {ann_ret}')



    # Q3: What is the annualised daily return for the period from 2010 to 2020 for
    # the stock with the highest average return in 2020 (the one you identified in
    # the first question above)?
    Q3_ANSWER = '0.5516209538619083'

    max_ann = pj.get_ann_ret(df[max_tic], start='2010', end='2020')
    print(f'The answer of Q3 is {max_ann}')



    # Q4: What is the annualised daily ABNORMAL return for the period from 2010 to 2020 for
    # the stock with the highest average return in 2020 (the one you identified in
    # the first question Q1 above)? Abnormal returns are calculated by subtracting
    # the market return ("mkt") from the individual stock return.
    Q4_ANSWER = '0.3770885290285164'

    aret_df = pj.mk_aret_df(df)
    max_a_ann = pj.get_ann_ret(aret_df[max_tic], start='2010', end='2020')
    print(f'The answer of Q4 is {max_a_ann}')

