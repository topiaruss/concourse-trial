#!/bin/bash

set -ex

creds=~/.concourse_credentials.yaml
CONCOURSE_HOST=${CONCOURSE_HOST-concourse}
fly_target=lite
#fly -t ${fly_target} login -c http://${CONCOURSE_HOST}:8080
fly -t ${fly_target} sp configure -c pipeline.yaml -p conc-trial-combo --load-vars-from ${creds} -n
fly -t ${fly_target} unpause-pipeline --pipeline conc-trial-combo

# if you want to automatically trigger and watch
#fly -t ${fly_target} trigger-job -j conc-trial-combo/concourse-trial-publish-combo
#fly -t ${fly_target} watch -j conc-trial-combo/concourse-trial-publish-combo
