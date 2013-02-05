#!/usr/bin/env bash

echo "Downloading Ubuntu 13.04 Source Package Database..."
[ -f Sources.bz2 ] && rm Sources.bz2
[ -f Sources ] && rm Sources
curl -O http://archive.ubuntu.com/ubuntu/dists/raring/universe/source/Sources.bz2
bunzip2 Sources.bz2
PACKAGES=($(grep "Package: unity-webapps" Sources | sed 's/Package: unity-webapps-//g'))

printline() {
  COLS=$(tput cols)
  while [ ${COLS} -gt 0 ]; do
    echo -n ${1}
    let COLS--
  done
  echo
}

LINE_THICK=$(printline '=')
LINE_THIN=$(printline '-')

for i in ${PACKAGES[@]}; do
  UBUNTU_VER=$(grep -A2 "Package: unity-webapps-${i}$" Sources | sed -n 's/^Version: \(.*\)/\1/p')
  SPEC_VER=$(sed -n "s/^%define[ \t]*_ver_${i/-/_}[ \t]*\(.*\)$/\1/p" unity-webapps.spec)

  echo "${LINE_THICK}"
  echo "Package: unity-webapps-${i}"
  echo "${LINE_THIN}"
  echo "spec file version: ${SPEC_VER}"
  echo "Ubuntu version:    ${UBUNTU_VER}"
done

rm Sources
