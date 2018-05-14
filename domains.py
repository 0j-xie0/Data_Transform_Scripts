import read
df = read.load_data()
df['url'].dropna(inplace=True)

def rm_sub(fld):
    s = str(fld).split('.')
    l = len(s)
    return s[l-2] + '.' + s[l-1]

df['url'] = df['url'].apply(rm_sub)
domains = df['url'].value_counts()

for name, row in domains.items():
    print("{}:{}".format(name, row))