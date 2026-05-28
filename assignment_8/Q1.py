#Q 1) Convert a series of date-strings to a timeseries?

import pandas as pd

date_strings = pd.Series(['2026-01-01', '2026-02-01', '2026-03-01'])

ts=pd.to_datetime(date_strings)
print(ts)