
import pandas as pd
import os
import datetime as dt

def modification_date(filename):
    t = os.path.getmtime(filename)
    file_time = dt.datetime.fromtimestamp(os.path.getmtime(filename))
    file_time = file_time.strftime("%D")
    dt_t = dt.datetime.strftime(dt.datetime.fromtimestamp(t).date(), "%Y-%m-%d")
    
    return dt_t

def move_tickets(frames):
    
    ticket = []
    
    for frame in frames:
        for i in frame.ticket_number:
            ticket.append(i)
    
    return ticket


def date_diff(df):
    df['from_announce'] = (df.as_of_date - df.announce_date).dt.days
    df['from_issuance'] = (df.as_of_date - df.issue_date).dt.days

    return df



def filter_time_delta(df,col):
    return df[df1[col] <=  np.timedelta64(dt.timedelta(days = 0))]


def gen_frame(file):
    
    df = pd.read_csv(file, sep='\t', skiprows=2)
    #fill nans on not field with blank space
    df[['Long Note 1','Long Note 2','Long Note 3','Long Note 4' ]] = df[['Long Note 1','Long Note 2','Long Note 3', 'Long Note 4' ]].fillna('')
    #join notes fields to one
    df['long notes'] = df['Long Note 1'].astype(str) +" " + df['Long Note 2'].astype(str) +" "+ df['Long Note 3'].astype(str) + df['Long Note 4'].astype(str)
    #fix spaces to _
    df.columns = [i.lower().replace(' ', '_').replace('(', '').replace(')', '') for i in df.columns]
    
    date_cols = ['as_of_date', 'issue_date', 'announce_date', 'settlement_date']
    
    for i in date_cols:
        df[i] = pd.to_datetime(df.loc[:,(i)], errors='coerce')
    
    
    df = date_diff(df)
    
    return df



def remove_books(df):
        df = df[((df.master_account != 'TRADER')&(df.counterparty != 'TESTHOLD') &
         (df.master_account != 'TEST')& (df.trader_name != 'DBDESK') &            #DBDESK = dublin
         (df.master_account != '70112883')&      #70112883 = fed rserver
         (~df.trader_name.str.startswith(('CFE', 'HK')))                               #cfe = cfe europe
        )].reset_index(drop=True)
        
        return df

def write_excel(out_name, frames):
       
    with pd.ExcelWriter(out_name) as writer:
        dealOver.to_excel(writer, sheet_name='over deal books', index=False)
        agcyOver.to_excel(writer, sheet_name='over agcy over', index=False)
        dfOver_rRobin.to_excel(writer, sheet_name='over rount robin', index=False)
        df_Over_exchange.to_excel(writer, sheet_name='over pool exchanges', index=False)
        df_newPool_Over.to_excel(writer, sheet_name='over mbs pools', index=False)
        
        dealUnder.to_excel(writer, sheet_name='under deal books', index=False)
        agcyUnder.to_excel(writer, sheet_name='unver agcy', index=False)
        df_newPool_Under.to_excel(writer, sheet_name='under mbs pools', index=False)
        df_Under_exchange.to_excel(writer, sheet_name='under pool exchanges', index=False)




if __name__ == "__main__":

    pass
