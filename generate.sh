#!/bin/bash

rm -rf go-diagrams

go run ./main.go

pushd go-diagrams

dot -Tpng app.dot > diagram.png

popd