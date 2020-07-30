import json
with open('main.json', encoding="utf8") as infile:
  o = json.load(infile)
  chunkSize = 60000
  for i in range(0, len(o), chunkSize):
    with open('json_' + str(i//chunkSize) + '.json', 'w') as outfile:
      json.dump(o[i:i+chunkSize], outfile)