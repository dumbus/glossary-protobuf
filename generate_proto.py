#!/usr/bin/env python3
import subprocess
import sys

# Запуск команды для генерации на основе protobuf
subprocess.run([
  sys.executable, "-m", "grpc_tools.protoc",
  "-Iprotobufs",
  "--python_out=src/generated",
  "--grpc_python_out=src/generated",
  "protobufs/glossary.proto"
])

# Исправление импортов в сгенерированных файлах (для сохранения стуктуры с директорией 'generated')
grpc_file = "src/generated/glossary_pb2_grpc.py"

with open(grpc_file, 'r') as f:
  content = f.read()

content = content.replace(
  'import glossary_pb2 as glossary__pb2',
  'from . import glossary_pb2 as glossary__pb2'
)

with open(grpc_file, 'w') as f:
  f.write(content)
