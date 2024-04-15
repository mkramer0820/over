import pandas as pd
import numpy as np
import os
import glob as glob
import datetime as dt
import time
from over_report.arrays import frame_lists as l
from over_report.table_functions import date_diff, filter_time_delta, gen_frame, move_tickets, remove_books


pd.options.display.max_columns = 35


def modification_date(filename):
    t = os.path.getmtime(filename)
    file_time = dt.datetime.fromtimestamp(os.path.getmtime(filename))
    file_time = file_time.strftime("%D")
    dt_t = dt.datetime.strftime(dt.datetime.fromtimestamp(t).date(), "%Y-%m-%d")
    
    return dt_t


def gen_data_frame(file):
    
    if type(file) is list:
        print(file)
        file = file[0]
    
    if type(file) is str:
        file = file
    
    df = gen_frame(file)
    df = remove_books(df)
    df = df[l.columns]
    
    master_act_filter = ['TRADER', 'TESTHOLD', '70112883']
    trd_book_filter = ('CFE', 'HK', 'DBDESK')
    df = df[((df.counterparty !='TESTHOLD')& 
            (~df.master_account.astype(str).isin(master_act_filter))
            &(~df.trader_name.str.startswith(trd_book_filter)))]

    df=df.reset_index(drop=True)
    df = df[df.is_trace =='Y'].reset_index(drop=True)
    
    return df



class frames(object):
    
    def __init__(self, df):
    
        self.df = gen_data_frame(df)

    
    def df_under(self):
        dfUnder = self.df[(self.df.reg_confirm == 'DONOTSEND') |
                          (self.df.reg_confirm.isna()) |
                          (self.df.reg_confirm == '0')
                         ].reset_index(drop=True)
        return dfUnder
    
    def df_over(self):
        dfOver = self.df[self.df.reg_confirm != 'DONOTSEND'].reset_index(drop=True)
        return dfOver


"""
checks for trades that have a regconfirm and also in a commission type book that should not be reported:
        'RMBSCOMM', 'ABSCOMM', 'CORPDEAL', 'CORPSYND', 'PTHRCOMM', 'SBA2'
then short by security descript and counter party
"""
#print('filtering reports with reg confirm #s and in a commission books these should not be reported %s' % (l.commbooks)) 
def _deal_over(base):
    df_over = base.df_over()
    df_deal_over = df_over[df_over.trader_name.isin(l.commbooks)].sort_values(
        by=['security_description', 'counterparty']).reset_index(drop=True)
    print(df_deal_over)
    return df_deal_over


"""
checks for trades that have a regconfirm and also in a commission type book that should not be reported:
        'RMBSCOMM', 'ABSCOMM', 'CORPDEAL', 'CORPSYND', 'PTHRCOMM', 'SBA2'
then short by security descript and counter party
"""
#print('filtering reports with reg confirm #s and in a dealbooks %s' % (l.dealbooks)) 
def _deal_all(base):

    df_deal_all = base.df[base.df.trader_name.isin(
        l.dealbooks)].sort_values(
        by=['security_description', 'counterparty']).reset_index(drop=True)
    return df_deal_all


def _deal_under(base):
    df_under = base.df_under()
    df_deal_under = df_under[df_under.trader_name.isin(l.dealbook)]

    df_deal_under = df_deal_under.sort_values(by=['security_description', 'counterparty']).reset_index(drop=True)
    return df_deal_under


def _ageny_under(base):
    df_under = base.df_under()

    df_agency_under = df_under[(df_under.trader_name.isin(l.agcy_book)) & 
                        (~df_under.counterparty.isin(l.agcy_gse_account))]#&(df_under['from_announce'] <= 0)]

    #print('use from announce to determine if new issuance')
    df_agency_under = df_agency_under.sort_values(by=['from_announce', 'master_account']).reset_index(drop=True)

    return df_agency_under


# In[21]:

def _agency_over(base):
    df_over = base.df_over()

    df_agency_over = df_over[df_over.trader_name.isin(l.agcy_book)]

    #filters trades done with customer
    df_agency_over = df_agency_over[~df_agency_over.master_account.str.startswith('5')]
    df_agency_over = df_agency_over.sort_values(by=['from_announce', 'master_account']).reset_index(drop=True)
    return df_agency_over



def _over_rRobin(base):
    df_over_rRobin = base.df[base.df.round_robin_to_be_announced == 'Y']
    return df_over_rRobin

def _new_pool_over(base):
    df_over = base.df_over()

    df_new_pool_over = df_over[(df_over.counterparty.isin(l.pools)) & (~df_over.trader_name.str.startswith('AGY', na=False))]
    df_new_pool_over['notes'] = df_new_pool_over['master_account_long_name']
    #print(l.pools)
    df_new_pool_over = df_new_pool_over.sort_values(by=['master_account_long_name','from_issuance']).reset_index(drop=True)

    return df_new_pool_over

# In[11]:
def _new_pool_under(base):
    df_under = base.df_under()

    df_new_pool_under = df_under[(df_under.counterparty.isin(l.pools)) & (~df_under.trader_name.str.startswith('AGY', na=False))]
    df_new_pool_under['notes'] = df_new_pool_under['master_account_long_name']
    df_new_pool_under = df_new_pool_under.sort_values(by=['master_account_long_name','from_issuance']).reset_index(drop=True)

    return df_new_pool_under


# In[19]:
def _over_exchange(base):
    df_over = base.df_over()
    df_over_exchange = df_over[df_over.counterparty.isin(l.exchnge_account)]

    return df_over_exchange

def _under_exchange(base):
    df_under = base.df_under()

    df_under_exchange = df_under[df_under.counterparty.isin(l.exchnge_account)]

    return df_under_exchange

def _remaining(base, frames):
    t = move_tickets(frames)
    
    remaining = base.df_under()[~base.df_under().ticket_number.isin(t)]
    return remaining

def _reported(frames, base):
    t = move_tickets(frames)
    reported = base.df[~base.df.ticket_number.isin(t)]
    return reported

# In[24]:
def GNPL_Manual(path):

    df = gen_data_frame(path)
    manual_report_books = l.trade_support_manual
    dfManual = df[(df.trader_name.isin(manual_report_books)) & (df.security_description.str.startswith((".", "STRU")))]
    dfManual[dfManual.settlement_date >= pd.Timestamp('today')]
    return dfManual


def write_excel(out_name):
       
    with pd.ExcelWriter(out_name) as writer:
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
        


if __name__ != '__main__':
    
    pass