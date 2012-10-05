#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' webaccounts-browser-extension.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/webaccounts-browser-extension' -O - | sed -n 's/.*>webaccounts-browser-extension_\(.*\)-\(.*\)\.debian\.tar\.gz<.*/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q 'https://launchpad.net/online-accounts-browser-extension/+download' -O - | sed -n 's/.*webaccounts-browser-extension-\(.*\)\.tar\.gz.*/\1/p' | head -n 1)

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
