import sys
import pandas as pd

print('arguments', sys.argv)

# sys.argv is a list in Python, which contains the command-line arguments passed to the script. 0 is the script name, and 1 is the first argument.
month = int(sys.argv[1]) 

df = pd.DataFrame({"day": [1,2], "num_passengers": [3,4]})
df['month'] = month

print(df.head())
df.to_parquet(f"output-{month:02d}.parquet")
