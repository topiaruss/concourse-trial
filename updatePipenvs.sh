#!/usr/bin/env bash

( pipenv update) &
( cd alpha; pipenv update > alpha.update.log)&
( cd beta; pipenv update > beta.update.log )&
( cd gamma; pipenv update > gamma.update.log )&

echo "waiting"
wait
echo "all done"