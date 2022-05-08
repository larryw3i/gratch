#!/usr/bin/bash

app_name='gratch'

cf_files=$(find . -name "*.c" -o -name "*.h")
for f in $cf_files
do
    clang-format -i $f
done

echo $@
