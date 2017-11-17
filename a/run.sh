#!/bin/bash

set -ex

# realpath() {
#   [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
# }

# usage() {
#   echo "USAGE: run.sh path/to/credentials.yml"
#   exit 1
# }

# if [ -z "${stub}" ]; then
#   stub="~/.concourse_credentials.yaml"
# fi
# stub=$(realpath $stub)
# if [[ ! -f ${stub} ]]; then
#   usage
# fi

stub=~/.concourse_credentials.yaml

fly_target=lite
#pushd $DIR
  fly -t ${fly_target} sp configure -c pipeline.yaml -p maina --load-vars-from ${stub} -n
  fly -t ${fly_target} unpause-pipeline --pipeline maina
  fly -t ${fly_target} trigger-job -j maina/concourse-trial-publish-a
  fly -t ${fly_target} watch -j maina/concourse-trial-publish-a
#popd
