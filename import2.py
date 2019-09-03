import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json


schema = avro.schema.parse(open("transaction500000_2.avro", "rb").read())

writer = DataFileWriter(open("transaction.avro", "wb"), DatumWriter(), schema)
writer.append(json.loads('{"hash": "c78c614d47c0facd1162d7c40bbc6a2ad3d96aacd4afdfef1453069b1a5b8345","size": 225,"virtual_size": 225,"version": 2,"lock_time": 499979,"block_number": 500000,"block_hash": "00000000000000000024fb37364cbf81fd49cc2d51c09c75c35433c3a1945d04","block_timestamp": 1513622125,"is_coinbase": false}'))
writer.close()



reader = DataFileReader(open("transaction.avro", "rb"), DatumReader())
for user in reader:
        print(user)
reader.close()
