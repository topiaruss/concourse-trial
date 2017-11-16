#!/bin/bash

set -ex

realpath() {
  [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

usage() {
  echo "USAGE: run.sh path/to/credentials.yml"
  exit 1
}

if [ -z "${stub}" ]; then
  stub="~/.quay_io.yaml"
fi
stub=$(realpath $stub)
if [[ ! -f ${stub} ]]; then
  usage
fi

fly_target=
#pushd $DIR
  fly sp -t ${fly_target} configure -c pipeline.yml -p main --load-vars-from ${stub} -n
  fly -t ${fly_target} unpause-pipeline --pipeline main
  fly -t ${fly_target} trigger-job -j main/concourse-trial-publish
  fly -t ${fly_target} watch -j main/concourse-trial-publish
#popd
