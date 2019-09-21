import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Max24680@127.0.0.1:3306/MaxDB')

df = pd.read_sql("select * from twitterscraper_filtered", con=engine)
df1 = df.sort_values(by=['ID'])

def concat(df):
    row = None
    datetime = None
    for r in df.itertuples():
        if(r.text.startswith("...")):
            row += r.text[3:]
        else:
            if row is not None:
                yield datetime, row
            row = r.text
            datetime = r.datetime
    yield datetime, row

out = list(concat(df1))
out_df = pd.DataFrame(columns=['datetime', 'text'], data=out)
out_df.to_sql(name='twitterscraper_merged', con=engine)