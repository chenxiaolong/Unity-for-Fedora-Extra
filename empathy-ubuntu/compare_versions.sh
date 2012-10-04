#!/usr/bin/env bash

F18_SPEC_VER="$(rpmspec -q --qf '%{version}\n' empathy-ubuntu-Fedora_18.spec | head -1)"
F18_PPA_REL="$(sed -n 's/^%define[ ]*_ppa_rel[ ]*\(.*\)$/\1/p' empathy-ubuntu-Fedora_18.spec)"

echo "Getting latest Ubuntu version..."
UBUNTU_VER=($(wget -q 'http://packages.ubuntu.com/quantal/source/empathy' -O - | sed -n 's/.*>empathy_\(.*\)-\(.*\)\.debian\.tar\.bz2<.*/\1 \2/p'))

echo "Getting latest upstream version..."
UPSTREAM_VER=$(wget -q "http://ftp.gnome.org/pub/GNOME/sources/empathy/3.6/" -O - | sed -n 's/.*>LATEST-IS-\(.*\)<.*/\1/p')

echo ""

echo -e "F18 spec version: ${F18_SPEC_VER} ${F18_PPA_REL}"
echo -e "Upstream version: ${UPSTREAM_VER}"
echo -e "Ubuntu version:   ${UBUNTU_VER[@]}"
