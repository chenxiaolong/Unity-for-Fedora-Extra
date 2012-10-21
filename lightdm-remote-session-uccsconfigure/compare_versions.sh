#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' lightdm-remote-session-uccsconfigure.spec | head -1)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q -O - 'https://launchpad.net/ubuntu/quantal/+source/lightdm-remote-session-uccsconfigure' | sed -n 's/^.*current\ release\ (\(.*\)-\(.*\)).*$/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q 'https://launchpad.net/lightdm-remote-session-uccsconfigure/+download' -O - | sed -n 's/.*lightdm-remote-session-uccsconfigure-\(.*\)\.tar\.gz.*/\1/p' | head -n 1)

echo ""

echo -e "spec file version: ${SPEC_VER}"
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
