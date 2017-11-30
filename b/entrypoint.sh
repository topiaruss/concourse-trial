#!/bin/bash
set -e

kill_devpi() {
    echo "SIGNAL TERM, EXIT, or INT received"
    test -n "$DEVPI_PID" && kill $DEVPI_PID
}
trap kill_devpi EXIT
trap kill_devpi INT
trap kill_devpi TERM

$(pipenv --venv)/bin/python3 component.py &
DEVPI_PID=$!

wait $DEVPI_PID
