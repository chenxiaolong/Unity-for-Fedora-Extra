#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' ubuntu-mono-icon-theme.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/ubuntu-mono' -O - | sed -n 's/.*>ubuntu-mono_\(.*\)\.tar\.gz<.*/\1/p'))

echo ""

echo -e "PKGBUILD version: ${SPEC_VER}"
echo -e "Upstream version: (none)"
echo -e "Ubuntu version:   ${UBUNTU_VER[@]}"
