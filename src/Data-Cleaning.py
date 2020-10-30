# Read raw data collected from web scraping 
df = pd.read_csv('pokemon.csv', index_col = None)

# Drop na rows (galarian form pokemon/ new release)
df = df.dropna(how = "any")

def min(df, col_list):
    '''
    A function returns pokemon with the lowest stat for every stat category
    ++++++
    Parameter:

    df (object): a dataframe of all pokemon   
    col_list (list): a list of all the stat 

    ++++++
    Output

        txt : (str) 
    '''
    txt = ''
    col_list = list(df.columns)
    for col in col_list:
        val = df[col].min()
        name = df[df[col] == val]['NAME'].values[0]
        txt += "{0}{1} has the lowest {2} of {3}.{4}".format("\n",name, col, str(val),"\n")
       
    return txt

print(min(df, col_list)) # Print out the result here 


def max(df, col_list):
    '''
    A function that returns pokemon with the highest stat for every stat category
    ++++++
    Parameter:

    df (object): a dataframe of all pokemon   
    col_list (list): a list of all the stat 

    ++++++
    Output :  
        
         txt (str) 
    '''
    txt = ''
    for col in col_list:
        val = df[col].max()
        name = df[df[col] == val]['NAME'].values[0]
        txt += "{0}{1} has the highest {2} of {3}.{4}".format("\n",name, col, str(val),"\n")
       
    return txt

print(max(df, col_list)) # Print out the result here 

def drop_mega(df):
    '''
    A function that drops out Pokemon with name containing a word "Mega " 

    '''
    mega = df[df['NAME'].str.contains('Mega ')]
    idx = mega.index
    df = df[~df.index.isin(idx)]
    return df 

def split_df(main_df):
    '''
    A function that splits the dataframe in half based on a pokemon named Arceus
    Arceus is the last pokemon in generation IV 
    +++++
    Output :

        df1 (object) : Dataframe with pokemon from Gen I - IV
        df2 (object) : Dataframe with pokemon from Gen V - VIII

    '''
    row_num = main_df[main_df['NAME'] == 'Arceus'].index.values
    # Reconfirm 
    # main_df.loc[540]
    df1 = main_df[:int(row_num)]
    df2 = main_df[(int(row_num) + 1):]
    return df1, df2 

def galarian_moving(df1, df2):
    '''
    A function that moves Galarian Pokemon from the first df to the bottom of the second df
    Galarian pokemon were not introduced until Gen VII but they share the same ID with the original form. 
    Therefore, moving them to the later gen group would give us a more accurate view on the stat distribution. 
    '''
    galarian = df1[df1['NAME'].str.contains('Galarian ')]
    galarian_idx = galarian.index
    df1 = df1[~df1.index.isin(galarian_idx)]
    df2 = pd.concat([df2,galarian])
    return df1, df2