#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' ubuntu-sounds.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q -O - 'https://launchpad.net/ubuntu/quantal/+source/ubuntu-sounds' | sed -n 's/^.*current\ release\ (\(.*\)).*$/\1/p'))

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  (none)"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
