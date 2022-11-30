#!/usr/bin/env bash
#
# Автор : Никола Иванов Македонски
# Създаден на 30.ноември.2022 14:20:28 +0200
#
# Author : Nikola Ivanov Makedonski
# Created Date : 30-11-2022 14:20:28 +0200
#
# Last modified : <2022-11-30 14:37:07 niki>
# File: protogen.sh

# Look How to generate correct import using grpcio-tools #9575 at:
# https://github.com/grpc/grpc/issues/9575#issuecomment-293934506
# and https://grpc.io/docs/languages/python/quickstart/


python -m grpc_tools.protoc -I../pydgraph --python_out=. --pyi_out=. --grpc_python_out=. ../pydgraph/pydgraph/proto/api.proto
