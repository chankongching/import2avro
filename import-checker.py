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
  'hash': 'cee16a9b222f636cd27d734da0a131cee5dd7a1d09cb5f14f4d1330b22aaa38e',
  'inputs': [{
    'index': 0,
    'script_asm': '304502207432778ec1345015b0c67eece490e38c792efadc3e91d42dfe57f26ac3eb4d870221009160f5c6e69d7d31fd47efb52c3f12a4c6210104ca9136d587720725d8c5d2c9[ALL] 043a18eb7431c9fc130c49baf0e4d0d75d6037ae1934b546a4c86b626d66a635fc4144b1daf9fbfdae156a1b64ef17aaa01c0bba64a365400be90c2f8c9938ba3a',
    'addresses': ['13tgr4Z3xeYqg4WAX6KRkoUMmK8iWsQ2a'],
    'sequence': 4294967295,
    'value': 1179641,
    'script_hex': '48304502207432778ec1345015b0c67eece490e38c792efadc3e91d42dfe57f26ac3eb4d870221009160f5c6e69d7d31fd47efb52c3f12a4c6210104ca9136d587720725d8c5d2c90141043a18eb7431c9fc130c49baf0e4d0d75d6037ae1934b546a4c86b626d66a635fc4144b1daf9fbfdae156a1b64ef17aaa01c0bba64a365400be90c2f8c9938ba3a',
    'required_signatures': 1,
    'spent_transaction_hash': '435bd1e992837dee55558b0b3f142af3c931320f51edf6a4a02ad5d8755bbf74',
    'type': 'pubkeyhash',
    'spent_output_index': 0
  }, {
    'index': 1,
    'script_asm': '3046022100cca0ff06394dccae15261816715b9d23b3fd5d1fb62db6e3b7d05f35158b3c33022100e516fb366dc812b8765c0f7339f227b482c5fdd734a01528b9fd090e843ab677[ALL] 04b70d8e243b24a0c042f4d120ce1c655556292e72d66e395620774e19ef3717f2bb1611eda029e376b2bbd33820f20429ee1b459e28607b992d2214a42e904836',
    'addresses': ['1FzLZkwAWJcTBE9E7fox2G5cK3VjNc8WcV'],
    'sequence': 4294967295,
    'value': 500000000,
    'script_hex': '493046022100cca0ff06394dccae15261816715b9d23b3fd5d1fb62db6e3b7d05f35158b3c33022100e516fb366dc812b8765c0f7339f227b482c5fdd734a01528b9fd090e843ab677014104b70d8e243b24a0c042f4d120ce1c655556292e72d66e395620774e19ef3717f2bb1611eda029e376b2bbd33820f20429ee1b459e28607b992d2214a42e904836',
    'required_signatures': 1,
    'spent_transaction_hash': 'cef6b3726370dc9a6cb29d34d7971c40433e11fe8277f996d3936f95b2fabdb9',
    'type': 'pubkeyhash',
    'spent_output_index': 1
  }],
  'block_timestamp': 1306753419,
  'output_count': 3,
  'output_value': 501179641,
  'block_hash': '0000000000001d39eac1016f91da0ebf79714e2e425e7b8f9c188635df2fca58',
  'input_value': 501179641,
  'version': 1,
  'input_count': 2,
  'outputs': [{
    'index': 0,
    'script_asm': 'OP_DUP OP_HASH160 baa72d8650baec634cdc439c1b84a982b2e596b2 OP_EQUALVERIFY OP_CHECKSIG OP_NOP',
    'addresses': ['nonstandardb464ff8f77e8058539b14759da26583232ecedd6'],
    'script_hex': '76a914baa72d8650baec634cdc439c1b84a982b2e596b288ac61',
    'value': 1175545,
    'required_signatures': None,
    'type': 'nonstandard'
  }, {
    'index': 1,
    'script_asm': 'OP_DUP OP_HASH160 a35bc692e248dbf84f642b6998a40521562054d6 OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['1Ftm5xMJNgqnthfgbJXpApukx3HBbrTC7R'],
    'script_hex': '76a914a35bc692e248dbf84f642b6998a40521562054d688ac',
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
  'virtual_size': 474,
  'size': 474
}

# write into DB
writer.append(data)
writer.close()

# # Reading data
# reader = DataFileReader(open("transaction2.avro", "rb"), DatumReader())
# for user in reader:
#         print(user)
# reader.close()
