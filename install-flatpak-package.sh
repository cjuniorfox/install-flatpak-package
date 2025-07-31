#!/bin/bash

set -euo pipefail

SYSTEMD_PARAM="$1"
PACKAGE=$(systemd-escape --unescape "$SYSTEMD_PARAM")
TIMEOUT=300  # 5 minutes

log() {
    echo "[install-flatpak-package] $*"
}

# Check for permission to install Flatpaks
if ! flatpak --version &>/dev/null; then
    log "Flatpak is not installed. Exiting."
    systemctl disable "install-flatpak-package@${SYSTEMD_PARAM}.service"
    exit 0
fi

if ! flatpak remote-list &>/dev/null; then
    log "No permission to install Flatpaks. Disabling service."
    systemctl disable "install-flatpak-package@${SYSTEMD_PARAM}.service"
    exit 0
fi

# Wait for internet (up to $TIMEOUT seconds)
log "Waiting for internet connectivity (timeout: ${TIMEOUT}s)..."
for ((i=0; i<TIMEOUT; i++)); do
    if ping -q -c1 -W1 flathub.org &>/dev/null; then
        log "Internet is available."
        break
    fi
    sleep 1
done

if (( i == TIMEOUT )); then
    log "No internet after ${TIMEOUT}s. Exiting with error."
    exit 1
fi

# Try installing the package
log "Installing Flatpak package: ${PACKAGE}"
if flatpak install -y --noninteractive flathub "$PACKAGE"; then
    log "Successfully installed ${PACKAGE}"
    systemctl disable "install-flatpak-package@${SYSTEMD_PARAM}.service"
    exit 0
else
    log "Failed to install ${PACKAGE}. Will retry on next boot."
    exit 1
fi

