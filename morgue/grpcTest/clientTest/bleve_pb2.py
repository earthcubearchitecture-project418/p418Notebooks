# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bleve.proto

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
  name='bleve.proto',
  package='protobufs',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x62leve.proto\x12\tprotobufs\",\n\rSearchRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\"\x1e\n\x0bSearchReply\x12\x0f\n\x07message\x18\x01 \x01(\t2H\n\x06Search\x12>\n\x08\x44oSearch\x12\x18.protobufs.SearchRequest\x1a\x16.protobufs.SearchReply\"\x00\x62\x06proto3')
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='protobufs.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobufs.SearchRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='protobufs.SearchRequest.index', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=70,
)


_SEARCHREPLY = _descriptor.Descriptor(
  name='SearchReply',
  full_name='protobufs.SearchReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='protobufs.SearchReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchReply'] = _SEARCHREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'bleve_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchReply = _reflection.GeneratedProtocolMessageType('SearchReply', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREPLY,
  __module__ = 'bleve_pb2'
  # @@protoc_insertion_point(class_scope:protobufs.SearchReply)
  ))
_sym_db.RegisterMessage(SearchReply)



_SEARCH = _descriptor.ServiceDescriptor(
  name='Search',
  full_name='protobufs.Search',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=104,
  serialized_end=176,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoSearch',
    full_name='protobufs.Search.DoSearch',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCH)

DESCRIPTOR.services_by_name['Search'] = _SEARCH

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class SearchStub(object):
    """The service definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.DoSearch = channel.unary_unary(
          '/protobufs.Search/DoSearch',
          request_serializer=SearchRequest.SerializeToString,
          response_deserializer=SearchReply.FromString,
          )


  class SearchServicer(object):
    """The service definition.
    """

    def DoSearch(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'DoSearch': grpc.unary_unary_rpc_method_handler(
            servicer.DoSearch,
            request_deserializer=SearchRequest.FromString,
            response_serializer=SearchReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'protobufs.Search', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaSearchServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The service definition.
    """
    def DoSearch(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaSearchStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The service definition.
    """
    def DoSearch(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    DoSearch.future = None


  def beta_create_Search_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('protobufs.Search', 'DoSearch'): SearchRequest.FromString,
    }
    response_serializers = {
      ('protobufs.Search', 'DoSearch'): SearchReply.SerializeToString,
    }
    method_implementations = {
      ('protobufs.Search', 'DoSearch'): face_utilities.unary_unary_inline(servicer.DoSearch),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Search_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('protobufs.Search', 'DoSearch'): SearchRequest.SerializeToString,
    }
    response_deserializers = {
      ('protobufs.Search', 'DoSearch'): SearchReply.FromString,
    }
    cardinalities = {
      'DoSearch': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'protobufs.Search', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
