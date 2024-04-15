from _run import _deal_over, _deal_all, _deal_under, _ageny_under, _agency_over, _over_rRobin, _new_pool_over, _new_pool_under, _over_exchange,_under_exchange, GNPL_Manual 
from _run import _remaining, _ageny_under, GNPL_Manual, _reported#, start_date, end_date,
import pandas as pd
from _run import frames, gen_data_frame
from over_report.table_functions import gen_frame
import os

def test(f):
    base = frames(f)


    print(base.df)

def calc_start(df):
    df = df
    start_date = df.as_of_date.to_list()[-1].strftime('%m.%d.%y')
    return start_date

def calc_end(df):
    df = df
    end_date = df.as_of_date.to_list()[-1].strftime('%m.%d.%y')
    return end_date


def write_excel(df_path):

    base = frames(df_path)
    print(base.df_under())

    start_date = calc_start(base.df)
    end_date = calc_end(base.df)



    df_deal_all = _deal_all(base)

    df_deal_over = _deal_over(base)
    df_agency_over = _agency_over(base)
    df_over_rRobin = _over_rRobin(base)
    

    with open("log.txt", "a") as f:
        f.write(start_date+ "\n")
        agy = df_agency_over.to_string()
        f.write(agy+"\n \n")

    df_over_exchange = _over_exchange(base)
    df_new_pool_over = _new_pool_over(base)
    df_deal_under = _deal_under(base)
    df_agency_under = _ageny_under(base)
    df_new_pool_under = _new_pool_under(base)
    df_under_exchange = _under_exchange(base)

    _frames = [df_over_exchange,df_under_exchange ,df_new_pool_over, df_new_pool_under,df_over_rRobin, df_agency_under, df_agency_over, df_deal_all]


    remaining = _remaining(base, _frames)
    gnpl_flips = GNPL_Manual(df_path)
    reported = _reported(_frames,base)
    
    print('start under', start_date)
    
    #df_agency_over.to_excel("C:\\users\\kmk\\desktop\\reports\\test.xlsx")

    try:
        with pd.ExcelWriter(start_date+'-'+end_date+'.xlsx') as writer:
            df_deal_over.to_excel(writer, sheet_name='over deal books', index=False)
            df_agency_over.to_excel(writer, sheet_name='over agcy over', index=False)
            df_over_rRobin.to_excel(writer, sheet_name='over rount robin', index=False)
            df_over_exchange.to_excel(writer, sheet_name='over pool exchanges', index=False)
            df_new_pool_over.to_excel(writer, sheet_name='over mbs pools', index=False)
            
            df_deal_under.to_excel(writer, sheet_name='under deal books', index=False)
            df_agency_under.to_excel(writer, sheet_name='under agcy', index=False)
            df_new_pool_under.to_excel(writer, sheet_name='under mbs pools', index=False)
            df_under_exchange.to_excel(writer, sheet_name='under pool exchanges', index=False)
            remaining.to_excel(writer, sheet_name='under remaining', index=False)
            gnpl_flips.to_excel(writer, sheet_name='GNPL Manuals', index=False)
            
            reported.to_excel(writer, sheet_name='reported trade')

    except Exception as e:
        with open("log.txt", "a") as f:
            f.write(str(e) + "\n")
            f.write('end \n')


if __name__ != '__main__':
    
    pass