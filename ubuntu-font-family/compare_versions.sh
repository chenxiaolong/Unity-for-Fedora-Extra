#!/usr/bin/env bash

SPEC_VER="$(rpmspec -q --qf '%{version}\n' ubuntu-font-family.spec | head -1)"
UBUNTU_REL="$(sed -n 's/^%define[ ]*_ubuntu_rel[ ]*\(.*\)$/\1/p' ubuntu-font-family.spec)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/ubuntu-font-family-sources' -O - | sed -n 's/.*>ubuntu-font-family-sources_\(.*\)-\(.*\)\.debian\.tar\.gz<.*/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q 'http://font.ubuntu.com/' -O - | sed -n 's/^.*ubuntu-font-family-\(.*\)\.zip.*$/\1/p')

echo ""

echo -e "spec file version: ${SPEC_VER} ${UBUNTU_REL}"
echo -e "Upstream version:  ${UPSTREAM_VER}"
echo -e "Ubuntu version:    ${UBUNTU_VER[@]}"
