#!/usr/bin/env bash

./combine_benchdeploy.sh

python benchmark_replicas_find.py ../benchmark/combined_benchmark.csv
python benchmark_version_find.py ../benchmark/combined_benchmark.csv
python benchmark_replicas_import.py ../benchmark/combined_benchmark.csv
python benchmark_version_import.py ../benchmark/combined_benchmark.csv
python benchmark_replicas_mapreduce.py ../benchmark/combined_benchmark.csv
python benchmark_version_mapreduce.py ../benchmark/combined_benchmark.csv
python benchmark_shard_mapreduce.py ../benchmark/combined_benchmark.csv
python benchmark_shards_find.py ../benchmark/combined_benchmark.csv
python benchmark_shards_import.py ../benchmark/combined_benchmark.csv

