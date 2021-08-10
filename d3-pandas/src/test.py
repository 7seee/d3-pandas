import pandas as pd
import matplotlib as plt
plt.use('Agg')

import codecs

with codecs.open('data/realized_pl.csv', 'r', 'utf-8', 'ignore') as f:
    df = pd.read_csv(f)

df.to_json("output/test.json")
df.plot(x=1)

# draw graph
plt.pyplot.savefig("datetime.png")
