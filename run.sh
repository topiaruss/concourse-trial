#!/bin/bash

set -ex

creds=~/.concourse_credentials.yaml

# The build system - often forwarded like:
# export POD_NAME=$(kubectl get pods --namespace default -l "app=wise-possum-web" \
#    -o jsonpath="{.items[0].metadata.name}")
# kubectl port-forward --namespace default $POD_NAME 8080:8080

fly_target=lite
fly -t lite login -c http://localhost:8080

fly -t ${fly_target} sp configure -c pipeline.yaml -p conc-trial-combo --load-vars-from ${creds} -n
fly -t ${fly_target} unpause-pipeline --pipeline conc-trial-combo

# if you want to automatically trigger and watch
#fly -t ${fly_target} trigger-job -j conc-trial-combo/concourse-trial-publish-combo
#fly -t ${fly_target} watch -j conc-trial-combo/concourse-trial-publish-combo
