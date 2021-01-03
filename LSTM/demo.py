import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///Futures.db')
frame = pd.read_sql('RB9999.XSGE', engine)
print(frame)
