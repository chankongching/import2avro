import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json, datetime


schema = avro.schema.parse(open("transaction-checker.avsc", "rb").read())

writer = DataFileWriter(open("transaction-checker.avro", "wb"), DatumWriter(), schema)

# Sample data
data = {
  'block_number': 127630,
  'lock_time': 0,
  'fee': 0,
  'hash': '5492a05f1edfbd29c525a3dbf45f654d0fc45a805ccd620d0a4dff47de63f90b',
  'inputs': [{
    'index': 0,
    'script_asm': '304402200f185ac16694f3f3902fb058f1a3d96f2549db4311b038742fc315685c9e6a1f022018e6c2c8e0559d87988b48ba80d214d95ed3f06795e549d4568702cc2a9e2af3[ALL] 0463cd01a8f2b56fff4e9357ccedf014ca119d64c1dff8b576e2785f603b3fd1a04e7ab451929ef5e4e2449a7999a1365db7bc08fccc19cdad16c4ce26d6ba9bf4',
    'addresses': ['1HKJgzaThRRF1BiU8fN1frHzH3199o1jZ9'],
    'sequence': 4294967295,
    'value': 796000000,
    'script_hex': '47304402200f185ac16694f3f3902fb058f1a3d96f2549db4311b038742fc315685c9e6a1f022018e6c2c8e0559d87988b48ba80d214d95ed3f06795e549d4568702cc2a9e2af301410463cd01a8f2b56fff4e9357ccedf014ca119d64c1dff8b576e2785f603b3fd1a04e7ab451929ef5e4e2449a7999a1365db7bc08fccc19cdad16c4ce26d6ba9bf4',
    'required_signatures': 1,
    'spent_transaction_hash': 'ac2dff2a1c506054e208d608e4c25a5ccbe76bfce94d989c86eb2fa979bf88d4',
    'type': 'pubkeyhash',
    'spent_output_index': 1
  }],
  'block_timestamp': 1306753419,
  'output_count': 3,
  'output_value': 796000000,
  'block_hash': '0000000000001d39eac1016f91da0ebf79714e2e425e7b8f9c188635df2fca58',
  'input_value': 796000000,
  'version': 1,
  'input_count': 1,
  'outputs': [{
    'index': 0,
    'script_asm': 'OP_DUP OP_HASH160 69d28eb9a311256338d281025a7437096149472c OP_EQUALVERIFY OP_CHECKSIG OP_NOP',
    'addresses': ['nonstandarde25b390253db4fc41336bf031dfdfb46945d40de'],
    'script_hex': '76a91469d28eb9a311256338d281025a7437096149472c88ac61',
    'value': 295995904,
    'required_signatures': None,
    'type': 'nonstandard'
  }, {
    'index': 1,
    'script_asm': 'OP_DUP OP_HASH160 5f8b65a4064ef5c071c382d594b55d94bd31ec3a OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['19iCBhaWDZQ8Z5Y9VuqArb2HuphT3zEpg7'],
    'script_hex': '76a9145f8b65a4064ef5c071c382d594b55d94bd31ec3a88ac',
    'value': 500000000,
    'required_signatures': 1,
    'type': 'pubkeyhash'
  }, {
    'index': 2,
    'script_asm': 'OP_DUP OP_HASH160 6300bf4c5c2a724c280b893807afb976ec78a92b OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['1A2UnusrwYr7DbiFbFesRKrbQMiYkj6E84'],
    'script_hex': '76a9146300bf4c5c2a724c280b893807afb976ec78a92b88ac',
    'value': 4096,
    'required_signatures': 1,
    'type': 'pubkeyhash'
  }],
  'is_coinbase': False,
  'virtual_size': 292,
  'size': 292
}
# write into DB
writer.append(data)
writer.close()

# # Reading data
# reader = DataFileReader(open("transaction2.avro", "rb"), DatumReader())
# for user in reader:
#         print(user)
# reader.close()
