import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json, datetime


schema = avro.schema.parse(open("transaction-checker.avsc", "rb").read())

writer = DataFileWriter(open("transaction-checker.avro", "wb"), DatumWriter(), schema)

# Sample data
data = {
  'block_number': 157077,
  'lock_time': 0,
  'fee': 4294967296,
  'hash': '371fdf9eddba61b624e63f67c072a49d3e52f7ca835668f9bcce2b11610b5357',
  'inputs': [{
    'index': 0,
    'script_asm': '304402206a93bda33ddc0b399552781c612244e548c7be80b004481ca34b1b212be40a7b022027a0fa8c864d9d3e95c53105270977beb4975182f5dd2978ac744d8d0270bb3e[ALL] 044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'addresses': ['15kDcr9wDhZmvPufKP7vYyELSoLg4bKbAR'],
    'sequence': 4294967295,
    'value': 210388607,
    'script_hex': '47304402206a93bda33ddc0b399552781c612244e548c7be80b004481ca34b1b212be40a7b022027a0fa8c864d9d3e95c53105270977beb4975182f5dd2978ac744d8d0270bb3e0141044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'required_signatures': 1,
    'spent_transaction_hash': 'a5317507758745128489664e60c7946272702ab944e473decdaa396853f28b6a',
    'type': 'pubkeyhash',
    'spent_output_index': 2
  }, {
    'index': 1,
    'script_asm': '3044022049266357f3a3d589c21970221eb295f9f2bd76ed51792ee12b1b814a4d8d62bb02209cfa26dc4fc10ab8721e251f07081567743958178cd9bc953768222968325aff01 044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'addresses': ['15kDcr9wDhZmvPufKP7vYyELSoLg4bKbAR'],
    'sequence': 4294967295,
    'value': 698220000,
    'script_hex': '473044022049266357f3a3d589c21970221eb295f9f2bd76ed51792ee12b1b814a4d8d62bb02209cfa26dc4fc10ab8721e251f07081567743958178cd9bc953768222968325aff0141044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'required_signatures': 1,
    'spent_transaction_hash': 'e7b3d1b7a4363c81eb36c9221701b2eedacff3c7948ed944db9483dc68349bb1',
    'type': 'pubkeyhash',
    'spent_output_index': 1
  }, {
    'index': 2,
    'script_asm': '30440220499d8a68bc404d0548acabfaa254322782ccabd86858c0e5b28cb7a2f6a5f6010220cec5e9a6229efc503f7c14d0aa92b3e5cc2248aac15b1197ca99f4956e0e295401 044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'addresses': ['15kDcr9wDhZmvPufKP7vYyELSoLg4bKbAR'],
    'sequence': 4294967295,
    'value': 3594420000,
    'script_hex': '4730440220499d8a68bc404d0548acabfaa254322782ccabd86858c0e5b28cb7a2f6a5f6010220cec5e9a6229efc503f7c14d0aa92b3e5cc2248aac15b1197ca99f4956e0e29540141044329536fa5271dfb7094691ff93c434d665519f72055f0a0d19d43851fa0178a07bc001033e33c363fab8d6d20494f6ba789d753bc3150bf649142d36ba3e04d',
    'required_signatures': 1,
    'spent_transaction_hash': 'b942484b190b715eba44ccfc7f4399f5c3b463924c375088dabe1eb596579ca6',
    'type': 'pubkeyhash',
    'spent_output_index': 1
  }, {
    'index': 3,
    'script_asm': '30440220c89692dae8489d1bc947ac630e114055067f3db8637e3f1d37eef7815501a9e90220dbd9fd6500c20af8db4642b5a6b829a4f37c2ac94f17a37a361c25861ec4348901 04657b2d0577195047940b26ed8d5c59cb8d3c6feb6c571192dd3ecbe8a544bfed43a3bc44f06d5bbdfdb1b86854d894f77f22d7efe40e1ae7d1fa338581ad2692',
    'addresses': ['18acFQe4qGB7wEhApeSHcx49Aeh76y137B'],
    'sequence': 4294967295,
    'value': 1781240000,
    'script_hex': '4730440220c89692dae8489d1bc947ac630e114055067f3db8637e3f1d37eef7815501a9e90220dbd9fd6500c20af8db4642b5a6b829a4f37c2ac94f17a37a361c25861ec43489014104657b2d0577195047940b26ed8d5c59cb8d3c6feb6c571192dd3ecbe8a544bfed43a3bc44f06d5bbdfdb1b86854d894f77f22d7efe40e1ae7d1fa338581ad2692',
    'required_signatures': 1,
    'spent_transaction_hash': '8719c37e47b522b5af1a4de80127d4278b2376a339313027741d636b187b77c5',
    'type': 'pubkeyhash',
    'spent_output_index': 1
  }],
  'block_timestamp': 1323616207,
  'output_count': 3,
  'output_value': 1989301311,
  'block_hash': '00000000000004530bff812eddb78db46a076b1ff9b5d68f38d9204fa88ceb32',
  'input_value': 6284268607,
  'version': 1,
  'input_count': 4,
  'outputs': [{
    'index': 0,
    'script_asm': 'OP_DUP OP_HASH160 9a959609b75bc50c3c136b64f7b12c6ab27d7efe OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['1F6NFxzNsHpyaKRtyHB8JMsn5ccxQqDpEQ'],
    'script_hex': '76a9149a959609b75bc50c3c136b64f7b12c6ab27d7efe88ac',
    'value': 705032704,
    'required_signatures': 1,
    'type': 'pubkeyhash'
  }, {
    'index': 1,
    'script_asm': 'OP_DUP OP_HASH160 641ad5051edd97029a003fe9efb29359fcee409d OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['1A8JiWcwvpY7tAopUkSnGuEYHmzGYfZPiq'],
    'script_hex': '76a914641ad5051edd97029a003fe9efb29359fcee409d88ac',
    'value': 50000000,
    'required_signatures': 1,
    'type': 'pubkeyhash'
  }, {
    'index': 2,
    'script_asm': 'OP_DUP OP_HASH160 340cec2a26413ec235c114c0216f4cb978202825 OP_EQUALVERIFY OP_CHECKSIG',
    'addresses': ['15kDcr9wDhZmvPufKP7vYyELSoLg4bKbAR'],
    'script_hex': '76a914340cec2a26413ec235c114c0216f4cb97820282588ac',
    'value': 1234268607,
    'required_signatures': 1,
    'type': 'pubkeyhash'
  }],
  'is_coinbase': False,
  'virtual_size': 828,
  'size': 828
}

# write into DB
writer.append(data)
writer.close()

# # Reading data
# reader = DataFileReader(open("transaction2.avro", "rb"), DatumReader())
# for user in reader:
#         print(user)
# reader.close()
