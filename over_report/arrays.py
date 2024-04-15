

class frame_lists:
    
    
    #Data frame columns
    columns= ['as_of_date', 'ticket_number', 'security_description', 'trader_name',
       'buy/sell', 'trade_feed_trade_amount', 'trade_price','settlement_date',
       'tblt_ticket_type', '144a_eligible_indicator', 'security_type', 'transaction_type',
       'mortgage_pool_type','is_trace', 'reg_confirm', 'issuer',
       'cusip_number', 'counterparty', 'firm_account_long_name','master_account',
       'master_account_long_name', 'issue_date', 'announce_date',
       'round_robin_to_be_announced', 'trader_department_description', 'sales_description',
       'long_notes', 'from_announce', 'from_issuance']
    
    trade_support_manual = ["GNPL", "FDUS"]

    agcy_gse_account = [
        '10040988', #fhlb reston
        '94054400', #freddie
        '70136726', #farmer mac
        '94054400', # freddie
        '70386347', #ffcb funding
        ]
    
    
    agcy_book = ['AGYN', 'AGYM','AGWI'] # books for agency report
    
    dealbooks = [
        'RMBSCOMM', 'ABSCOMM', 'ABSDEAL',
        'RMBSDEAL', 'CORPDEAL', 'CORPSYND',
        'PTHRCOMM', 'SBA2']    
    commbooks = ['RMBSCOMM', 'ABSCOMM','CORPDEAL', 'CORPSYND', 'PTHRCOMM', 'SBA2']
    dealbook = ['ABSDEAL', 'RMBSDEAL']

    """
    pool creations issuers
    94105806 = FNMA MEGA
    94185600 = fnma mega
    94188703 = fhlmc giant/super
    70001690 = fhlmc giant
    70014329 = fhlmc supers
    20000196 = Bridge
    94000908 = cant fitz mbscc dealer - moving firm 31/33/37
    20000197 = exchanges bny
    70386347 = farm credit
    10040988 = fhlb reston
    94110806 = gnma plat
    TESTHOLD = TEST ACCOUNT
    70000951 = US BANK GNMA CMO DEAL 
    94001104 = CANTOR FITZGERALD & CO MBSCC DEALER CFCA
    941009060 = mega dupe check with trader


    """
    pools = [
        '94105806', #fnma mega
        '94188703', #fhlmc giant super
        '70001690', #fhlmc giant super
        '70014329', #FREDDIES SUPERS ACCOUNT
        '20000196', #CF&CO CONVERSIONS
        '94000908', #CANTOR FITZGERALD & CO MBS
        '20000197', #CFCO FED/BONY EXCHANGES
        '70386347', #FEDERAL FARM CREDIT BANK - 
        '10040988', #FHLB, RSTON VA
        '94110806', #GNMA PLATINUM ACCOUNT
        'TESTHOLD', #test
        '70000951', #US BANK NA GNMA CMO DEALS BECKER/WICKENS
        '94185600', #FNMA MEGA
        '94001104', #CANTOR FITZGERALD & CO MBSCC DEALER CFCA
        '941009060' #FANNIE MAE
    ]

    """
    exchanges
    #70479295 = wells
    #70014993 = us bank exchanged daly/depalma
    #70011657 = us bank exchanges kaufmann gnma cmo
    #20000197 = CFCO FED/BNY EXCHANGES
    #70013087 = CITIBANK NA
    """
    exchnge_account = [
        '70479295',#    #70479295 = wells
        '70014993',#    0014993 = us bank exchanged daly/depalma
        '70011657',#    70011657 = us bank exchanges kaufmann gnma cmo
        '20000197',#    20000197 = CFCO FED/BNY EXCHANGES
        '50026152',#    US BANK LAS VEGAS	USBANKLV
        '70011657',#     us bank exchanges kaufmann gnma cmo
        '70013087',  #70013087 = CITIBANK NA
        

    ]



if __name__ == "__main__":

    main()

