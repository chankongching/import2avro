import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json


schema = avro.schema.parse(open("transaction500000_2.avro", "rb").read())

writer = DataFileWriter(open("transaction2.avro", "wb"), DatumWriter(), schema)

data = {
  "hash": "c78c614d47c0facd1162d7c40bbc6a2ad3d96aacd4afdfef1453069b1a5b8345",
  "size": 225,
  "virtual_size": 225,
  "version": 2,
  "lock_time": 499979,
  "block_number": 500000,
  "block_hash": "00000000000000000024fb37364cbf81fd49cc2d51c09c75c35433c3a1945d04",
  "block_timestamp": 1513622125,
  "is_coinbase": False,
  "inputs": [{
    "index": 0,
    "spent_transaction_hash": "277f770ccce6dade20a9d797e3f88419435f465db56bd7b0a4ee94bb41a069e2",
    "spent_output_index": 1,
    "script_asm": "304402206d077981cdbd88578439a18653ae9ded88e73f903db8dfebd9a97389a33a43a502201bfe9443fe6550c36016c26c9e459af44bcfc6e4fbdbb0b7fedbf93904c7325e[ALL] 034af10276b44b10c31e4dcd5f6e6184a33151abcee75bcb369b175eaa349cf550",
    "script_hex": "47304402206d077981cdbd88578439a18653ae9ded88e73f903db8dfebd9a97389a33a43a502201bfe9443fe6550c36016c26c9e459af44bcfc6e4fbdbb0b7fedbf93904c7325e0121034af10276b44b10c31e4dcd5f6e6184a33151abcee75bcb369b175eaa349cf550"
  }]
}

writer.append(data)
writer.close()



reader = DataFileReader(open("transaction2.avro", "rb"), DatumReader())
for user in reader:
        print(user)
reader.close()
