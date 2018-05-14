import read
import pandas as pd
df=read.load_data()
df['submission_time'] = pd.to_datetime(df.submission_time)
df['submission_hours'] = df['submission_time'].dt.hour
hour_subs = df['submission_hours'].value_counts()
print(hour_subs)