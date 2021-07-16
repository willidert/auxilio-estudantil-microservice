# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='model.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmodel.proto\"\x1c\n\x08\x46\x65\x61tures\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x05\"(\n\x12PredictionResponse\x12\x12\n\nprediction\x18\x01 \x01(\x05\x32\x42\n\x0cModelService\x12\x32\n\x0eMakePrediction\x12\t.Features\x1a\x13.PredictionResponse\"\x00\x62\x06proto3'
)




_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='Features.features', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=15,
  serialized_end=43,
)


_PREDICTIONRESPONSE = _descriptor.Descriptor(
  name='PredictionResponse',
  full_name='PredictionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prediction', full_name='PredictionResponse.prediction', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=45,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['PredictionResponse'] = _PREDICTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:Features)
  })
_sym_db.RegisterMessage(Features)

PredictionResponse = _reflection.GeneratedProtocolMessageType('PredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:PredictionResponse)
  })
_sym_db.RegisterMessage(PredictionResponse)



_MODELSERVICE = _descriptor.ServiceDescriptor(
  name='ModelService',
  full_name='ModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=87,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='MakePrediction',
    full_name='ModelService.MakePrediction',
    index=0,
    containing_service=None,
    input_type=_FEATURES,
    output_type=_PREDICTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELSERVICE)

DESCRIPTOR.services_by_name['ModelService'] = _MODELSERVICE

# @@protoc_insertion_point(module_scope)