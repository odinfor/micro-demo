# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jsf.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='jsf.proto',
  package='lightweight',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tjsf.proto\x12\x0blightweight\"\'\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63tions\x18\x02 \x03(\t\"\"\n\x05Reply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x17\n\x07Student\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\"*\n\x0cStudentReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t2\x82\x01\n\x03Gym\x12\x39\n\x0c\x42odyBuilding\x12\x13.lightweight.Person\x1a\x12.lightweight.Reply\"\x00\x12@\n\x0bStudentName\x12\x14.lightweight.Student\x1a\x19.lightweight.StudentReply\"\x00\x62\x06proto3'
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='lightweight.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='lightweight.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='lightweight.Person.actions', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=26,
  serialized_end=65,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='lightweight.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='lightweight.Reply.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='lightweight.Reply.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=67,
  serialized_end=101,
)


_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='lightweight.Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='lightweight.Student.code', index=0,
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
  serialized_start=103,
  serialized_end=126,
)


_STUDENTREPLY = _descriptor.Descriptor(
  name='StudentReply',
  full_name='lightweight.StudentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='lightweight.StudentReply.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='lightweight.StudentReply.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=128,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['StudentReply'] = _STUDENTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'jsf_pb2'
  # @@protoc_insertion_point(class_scope:lightweight.Person)
  })
_sym_db.RegisterMessage(Person)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'jsf_pb2'
  # @@protoc_insertion_point(class_scope:lightweight.Reply)
  })
_sym_db.RegisterMessage(Reply)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'jsf_pb2'
  # @@protoc_insertion_point(class_scope:lightweight.Student)
  })
_sym_db.RegisterMessage(Student)

StudentReply = _reflection.GeneratedProtocolMessageType('StudentReply', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTREPLY,
  '__module__' : 'jsf_pb2'
  # @@protoc_insertion_point(class_scope:lightweight.StudentReply)
  })
_sym_db.RegisterMessage(StudentReply)



_GYM = _descriptor.ServiceDescriptor(
  name='Gym',
  full_name='lightweight.Gym',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=173,
  serialized_end=303,
  methods=[
  _descriptor.MethodDescriptor(
    name='BodyBuilding',
    full_name='lightweight.Gym.BodyBuilding',
    index=0,
    containing_service=None,
    input_type=_PERSON,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StudentName',
    full_name='lightweight.Gym.StudentName',
    index=1,
    containing_service=None,
    input_type=_STUDENT,
    output_type=_STUDENTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GYM)

DESCRIPTOR.services_by_name['Gym'] = _GYM

# @@protoc_insertion_point(module_scope)
