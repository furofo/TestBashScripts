#!/usr/bin/env bash

set -euo pipefail

S3_BUCKET="my-predefined-bucket"

if [[ $# -lt 1 ]]; then
	echo "Usage: $0 <name>" >&2
	exit 1
fi

name="$1"
output_file="hello_${name}.txt"

echo "hello world ${name}" > "$output_file"
if [[ "${TestScript:-}" == "True" ]]; then
    echo "Test mode: Skipping upload to S3. Output file: ${output_file}"
	true
else
	aws s3 cp "$output_file" "s3://${S3_BUCKET}/${output_file}"
fi
