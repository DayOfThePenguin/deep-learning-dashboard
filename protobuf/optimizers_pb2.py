# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: optimizers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='optimizers.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x10optimizers.proto\"N\n\x03SGD\x12\x0e\n\x02lr\x18\x01 \x01(\x02:\x02\x31\x30\x12\x13\n\x08momentum\x18\x02 \x01(\x02:\x01\x30\x12\x10\n\x05\x64\x65\x63\x61y\x18\x03 \x01(\x02:\x01\x30\x12\x10\n\x08nesterov\x18\x04 \x01(\x08\"F\n\x07RMSprop\x12\x11\n\x02lr\x18\x01 \x01(\x02:\x05\x30.001\x12\x10\n\x03rho\x18\x02 \x01(\x02:\x03\x30.9\x12\x16\n\x07\x65psilon\x18\x03 \x01(\x02:\x05\x31\x65-06\"3\n\x07\x41\x64\x61grad\x12\x10\n\x02lr\x18\x01 \x01(\x02:\x04\x30.01\x12\x16\n\x07\x65psilon\x18\x02 \x01(\x02:\x05\x31\x65-06\"D\n\x08\x41\x64\x61\x64\x65lta\x12\r\n\x02lr\x18\x01 \x01(\x02:\x01\x31\x12\x11\n\x03rho\x18\x02 \x01(\x02:\x04\x30.95\x12\x16\n\x07\x65psilon\x18\x03 \x01(\x02:\x05\x31\x65-06\"]\n\x04\x41\x64\x61m\x12\x11\n\x02lr\x18\x01 \x01(\x02:\x05\x30.001\x12\x13\n\x06\x62\x65ta_1\x18\x02 \x01(\x02:\x03\x30.9\x12\x15\n\x06\x62\x65ta_2\x18\x03 \x01(\x02:\x05\x30.999\x12\x16\n\x07\x65psilon\x18\x04 \x01(\x02:\x05\x31\x65-08\"_\n\x06\x41\x64\x61max\x12\x11\n\x02lr\x18\x01 \x01(\x02:\x05\x30.002\x12\x13\n\x06\x62\x65ta_1\x18\x02 \x01(\x02:\x03\x30.9\x12\x15\n\x06\x62\x65ta_2\x18\x03 \x01(\x02:\x05\x30.999\x12\x16\n\x07\x65psilon\x18\x04 \x01(\x02:\x05\x31\x65-08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SGD = _descriptor.Descriptor(
  name='SGD',
  full_name='SGD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='SGD.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum', full_name='SGD.momentum', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decay', full_name='SGD.decay', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nesterov', full_name='SGD.nesterov', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=98,
)


_RMSPROP = _descriptor.Descriptor(
  name='RMSprop',
  full_name='RMSprop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='RMSprop.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rho', full_name='RMSprop.rho', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='RMSprop.epsilon', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e-06,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=170,
)


_ADAGRAD = _descriptor.Descriptor(
  name='Adagrad',
  full_name='Adagrad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='Adagrad.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.01,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='Adagrad.epsilon', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e-06,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=223,
)


_ADADELTA = _descriptor.Descriptor(
  name='Adadelta',
  full_name='Adadelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='Adadelta.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rho', full_name='Adadelta.rho', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.95,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='Adadelta.epsilon', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e-06,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=293,
)


_ADAM = _descriptor.Descriptor(
  name='Adam',
  full_name='Adam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='Adam.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beta_1', full_name='Adam.beta_1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beta_2', full_name='Adam.beta_2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.999,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='Adam.epsilon', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e-08,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=388,
)


_ADAMAX = _descriptor.Descriptor(
  name='Adamax',
  full_name='Adamax',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lr', full_name='Adamax.lr', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.002,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beta_1', full_name='Adamax.beta_1', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.9,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beta_2', full_name='Adamax.beta_2', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.999,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='Adamax.epsilon', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1e-08,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=485,
)

DESCRIPTOR.message_types_by_name['SGD'] = _SGD
DESCRIPTOR.message_types_by_name['RMSprop'] = _RMSPROP
DESCRIPTOR.message_types_by_name['Adagrad'] = _ADAGRAD
DESCRIPTOR.message_types_by_name['Adadelta'] = _ADADELTA
DESCRIPTOR.message_types_by_name['Adam'] = _ADAM
DESCRIPTOR.message_types_by_name['Adamax'] = _ADAMAX

SGD = _reflection.GeneratedProtocolMessageType('SGD', (_message.Message,), dict(
  DESCRIPTOR = _SGD,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:SGD)
  ))
_sym_db.RegisterMessage(SGD)

RMSprop = _reflection.GeneratedProtocolMessageType('RMSprop', (_message.Message,), dict(
  DESCRIPTOR = _RMSPROP,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:RMSprop)
  ))
_sym_db.RegisterMessage(RMSprop)

Adagrad = _reflection.GeneratedProtocolMessageType('Adagrad', (_message.Message,), dict(
  DESCRIPTOR = _ADAGRAD,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:Adagrad)
  ))
_sym_db.RegisterMessage(Adagrad)

Adadelta = _reflection.GeneratedProtocolMessageType('Adadelta', (_message.Message,), dict(
  DESCRIPTOR = _ADADELTA,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:Adadelta)
  ))
_sym_db.RegisterMessage(Adadelta)

Adam = _reflection.GeneratedProtocolMessageType('Adam', (_message.Message,), dict(
  DESCRIPTOR = _ADAM,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:Adam)
  ))
_sym_db.RegisterMessage(Adam)

Adamax = _reflection.GeneratedProtocolMessageType('Adamax', (_message.Message,), dict(
  DESCRIPTOR = _ADAMAX,
  __module__ = 'optimizers_pb2'
  # @@protoc_insertion_point(class_scope:Adamax)
  ))
_sym_db.RegisterMessage(Adamax)


# @@protoc_insertion_point(module_scope)