import pandas as pd

# functions.english_translations('dataset/data/sw-KE.jsonl', 'sw')

# Import English, Swahili and German into dataframes
df_english = pd.read_json(path_or_buf='dataset/data/en-US.jsonl', lines=True)
df_swahili = pd.read_json(path_or_buf='dataset/data/sw-KE.jsonl', lines=True)
df_german = pd.read_json(path_or_buf='dataset/data/de-DE.jsonl', lines=True)

# From the dataframes, filter and export them into JSONL files.
df_english[df_english['partition'] == 'test'].to_json(r'outputs/en-US-test.jsonl', orient='records', lines=True)
df_swahili[df_swahili['partition'] == 'train'].to_json(r'outputs/sw-KE-train.jsonl', orient='records', lines=True)
df_german[df_german['partition'] == 'dev'].to_json(r'outputs/de-DE-dev.jsonl', orient='records', lines=True)
