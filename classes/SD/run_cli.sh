#!/bin/bash
RUN_TARGET="${1:-shell}"
export APPTAINER_NO_HOME=1
export APPTAINER_NO_MOUNT="cwd" # not available via /etc/apptainer/apptainer.conf
export APPTAINER_BINDPATH="$HOME/.ssh,$HOME:$HOME/area-de-aluno"
export APPTAINER_CLEANENV=1
export APPTAINER_UNSHARE_PID=1
export APPTAINER_WRITABLE_TMPFS=1
export APPTAINER_DISABLE_CACHE=1

mkdir -p "$HOME/.ssh"

if ! apptainer instance list | grep -cq "SD"; then
    apptainer instance start /opt/sifs/SD.sif SD
fi


if [[ "$RUN_TARGET" == "code" ]]; then
    code --remote ssh-remote+apptainer-fcul
elif [[ "$RUN_TARGET" == "shell" ]]; then
    apptainer shell instance://SD
elif [[ "$RUN_TARGET" == "stop" ]]; then
    apptainer instance stop SD
fi

$SHELL