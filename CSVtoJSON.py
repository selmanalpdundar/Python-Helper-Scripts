import pandas as pd
csvFileName = "CSVDataFile"
jsonOutputFileName = "jsonOutputFileName"
# you cange sep as your need , ; |  etc.
df = pd.read_csv (csvFileName, sep=';')
df.to_json(jsonOutputFileName, orient = "records", date_format = "epoch", double_precision = 0, force_ascii = True, date_unit = "ms", default_handler = None)