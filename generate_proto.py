#!/usr/bin/env python3
import subprocess
import sys

subprocess.run([
  sys.executable, "-m", "grpc_tools.protoc",
  "-Iprotobufs",
  "--python_out=src/generated",
  "--grpc_python_out=src/generated",
  "protobufs/helloworld.proto"
])

grpc_file = "src/generated/helloworld_pb2_grpc.py"

with open(grpc_file, 'r') as f:
  content = f.read()

content = content.replace(
  'import helloworld_pb2 as helloworld__pb2',
  'from . import helloworld_pb2 as helloworld__pb2'
)

with open(grpc_file, 'w') as f:
  f.write(content)
