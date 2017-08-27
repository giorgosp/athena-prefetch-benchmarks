# Athena - ROOT asynchronous prefetching benchmarks
This repo contains benchmark scripts to assess ROOT's asynchronous file prefetching in the Athena(ATLAS)framework.

The benchmarks can be run with `athena mergeTest.py > out.txt`. The athena job options can be configured in the `mergeTest.py`
file.

The `out.sh` script `grep`'s the output of the benchmark and prints only the most interesting facts.
