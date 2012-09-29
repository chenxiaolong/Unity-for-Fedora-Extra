#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' lightdm-remote-session-freerdp.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/lightdm-remote-session-freerdp' -O - | sed -n 's/.*>lightdm-remote-session-freerdp_\(.*\)-\(.*\)\.debian\.tar\.gz<.*/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q 'https://launchpad.net/lightdm-remote-session-freerdp/+download' -O - | sed -n 's/.*lightdm-remote-session-freerdp-\(.*\)\.tar\.gz.*/\1/p' | head -n 1)

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
