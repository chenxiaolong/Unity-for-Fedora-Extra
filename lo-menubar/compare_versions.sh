#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' lo-menubar.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/lo-menubar' -O - | sed -n 's/.*>lo-menubar_\(.*\)-\(.*\)\.debian\.tar\.gz<.*/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q 'https://launchpad.net/lo-menubar/+download' -O - | sed -n 's/.*lo-menubar-\(.*\)\.tar\.bz2.*/\1/p' | head -n 1)

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"