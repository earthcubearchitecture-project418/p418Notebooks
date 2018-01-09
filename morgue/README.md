### About pv418Notebooks
Repository for notebook and related work.





#### Notes on grpcTest
You can review the gRPC basics for python at https://grpc.io/docs/tutorials/basic/python.html.  
These are what were used to the generate the library from the various .proto files in this project.

```
  *  export SRC_DIR=~/src/go/src/earthcube.org/Project418/services/grpcBleveSearch/protobufs
  *  ~/bin/protoc -I=$SRC_DIR --python_out=./libraries $SRC_DIR/bleve.proto
  *  ls -lt libraries/
```