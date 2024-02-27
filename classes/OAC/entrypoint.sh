#!/bin/sh
SSH_KEY_NAME="id_apptainer-fcul"

# Create a symbolic link for the pre-installed vscode-server
if [ ! -d "$HOME/.vscode-server" ]; then
    ln -s "/.vscode-server" "$HOME/.vscode-server"
fi

# Generate SSH key pair (requires a mounted "$HOME/.ssh" dir)
if [ ! -f "$HOME/.ssh/${SSH_KEY_NAME}" ]; then
    ssh-keygen -t ed25519 -C "${SSH_KEY_NAME}" -f "$HOME/.ssh/${SSH_KEY_NAME}" -q -N ""
    cat "$HOME/.ssh/${SSH_KEY_NAME}.pub" >>"$HOME/.ssh/authorized_keys"
    chmod 644 "$HOME/.ssh/authorized_keys"
fi

# Start dropbear SSH server
if ! pgrep -x supervisord >/dev/null 2>&1; then
    supervisord
fi
