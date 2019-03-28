# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services.proto',
  package='services',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eservices.proto\x12\x08services\x1a\x1bgoogle/protobuf/empty.proto\"\x1f\n\x0c\x43ounterReply\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\"\x1b\n\nBooksReply\x12\r\n\x05\x62ooks\x18\x01 \x01(\t\"\x15\n\x04\x46ile\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\"\x19\n\tHourReply\x12\x0c\n\x04hour\x18\x01 \x01(\t\"\x19\n\tBookReply\x12\x0c\n\x04\x62ook\x18\x01 \x01(\t2\xb7\x02\n\x0bInformation\x12?\n\x0bSendCounter\x12\x16.google.protobuf.Empty\x1a\x16.services.CounterReply\"\x00\x12;\n\tSendBooks\x12\x16.google.protobuf.Empty\x1a\x14.services.BooksReply\"\x00\x12\x34\n\x06SendDB\x12\x16.google.protobuf.Empty\x1a\x0e.services.File\"\x00\x30\x01\x12\x39\n\x08SendHour\x12\x16.google.protobuf.Empty\x1a\x13.services.HourReply\"\x00\x12\x39\n\x08SendBook\x12\x16.google.protobuf.Empty\x1a\x13.services.BookReply\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_COUNTERREPLY = _descriptor.Descriptor(
  name='CounterReply',
  full_name='services.CounterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter', full_name='services.CounterReply.counter', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=88,
)


_BOOKSREPLY = _descriptor.Descriptor(
  name='BooksReply',
  full_name='services.BooksReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='services.BooksReply.books', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=117,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='services.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='services.File.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=140,
)


_HOURREPLY = _descriptor.Descriptor(
  name='HourReply',
  full_name='services.HourReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hour', full_name='services.HourReply.hour', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=167,
)


_BOOKREPLY = _descriptor.Descriptor(
  name='BookReply',
  full_name='services.BookReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='services.BookReply.book', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['CounterReply'] = _COUNTERREPLY
DESCRIPTOR.message_types_by_name['BooksReply'] = _BOOKSREPLY
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['HourReply'] = _HOURREPLY
DESCRIPTOR.message_types_by_name['BookReply'] = _BOOKREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CounterReply = _reflection.GeneratedProtocolMessageType('CounterReply', (_message.Message,), dict(
  DESCRIPTOR = _COUNTERREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.CounterReply)
  ))
_sym_db.RegisterMessage(CounterReply)

BooksReply = _reflection.GeneratedProtocolMessageType('BooksReply', (_message.Message,), dict(
  DESCRIPTOR = _BOOKSREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.BooksReply)
  ))
_sym_db.RegisterMessage(BooksReply)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.File)
  ))
_sym_db.RegisterMessage(File)

HourReply = _reflection.GeneratedProtocolMessageType('HourReply', (_message.Message,), dict(
  DESCRIPTOR = _HOURREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.HourReply)
  ))
_sym_db.RegisterMessage(HourReply)

BookReply = _reflection.GeneratedProtocolMessageType('BookReply', (_message.Message,), dict(
  DESCRIPTOR = _BOOKREPLY,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.BookReply)
  ))
_sym_db.RegisterMessage(BookReply)



_INFORMATION = _descriptor.ServiceDescriptor(
  name='Information',
  full_name='services.Information',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=197,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendCounter',
    full_name='services.Information.SendCounter',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_COUNTERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendBooks',
    full_name='services.Information.SendBooks',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BOOKSREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendDB',
    full_name='services.Information.SendDB',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_FILE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendHour',
    full_name='services.Information.SendHour',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_HOURREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendBook',
    full_name='services.Information.SendBook',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BOOKREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INFORMATION)

DESCRIPTOR.services_by_name['Information'] = _INFORMATION

# @@protoc_insertion_point(module_scope)
