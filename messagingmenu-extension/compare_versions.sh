#!/usr/bin/env bash

SPECFILE=messagingmenu-extension.spec

source "$(dirname ${0})/../version_checker.sh"

echo -e "PKGBUILD version: $(get_spec_version)"
UPSTREAM_VER=$(wget -q -O - 'https://code.launchpad.net/~extension-hackers/messagingmenu-extension/1.0' | grep Releasing | sed -n 's/^.*<p>Releasing\ \(.*\)<\/p>/\1/p' | head -n 1)
echo -e "Upstream version: ${UPSTREAM_VER}"
echo -e "Ubuntu version:   (n/a)"
