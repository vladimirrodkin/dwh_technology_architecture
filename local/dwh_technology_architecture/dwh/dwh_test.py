import pandas as pd
from pyarrow.parquet import ParquetFile
import pyarrow.parquet as pq

parquet_file = '../../source/good.parquet'
open(parquet_file, 'r')
source_df = pd.read_parquet(parquet_file, engine='pyarrow')
print(ParquetFile(parquet_file).metadata)
pd.set_option('display.max_columns', None)


table = pq.read_table(parquet_file)
print(table.schema)

print(source_df.head(5))


