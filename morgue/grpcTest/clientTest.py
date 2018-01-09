from __future__ import print_function

import grpc
import os
import sys

module_path = os.path.abspath(os.path.join('./libraries'))
if module_path not in sys.path:
    sys.path.append(module_path)

from bleve_pb2 import SearchRequest
from bleve_pb2_grpc import DoSearch

def run():
    
  channel = grpc.insecure_channel('localhost:50051')
  stub = bleve_pb2_grpc.pb.NewSearchClient(channel)
  response = stub.DoSearch(bleve_pb2.SearchRequest(term='thermal', index='csdco'))
  print("Client received: " + response.message)


if __name__ == '__main__':
  run()
