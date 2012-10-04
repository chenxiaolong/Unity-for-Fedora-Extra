#!/bin/bash
# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

if ! $(which bzr &>/dev/null); then
  echo "Please install bzr"
  exit 1
fi

_bzrtrunk=lp:messagingmenu-extension/1.0
_bzrname=messagingmenu-extension
_specfile=messagingmenu-extension.spec
_bzrrev=$(sed -n 's/^%define.*_bzr_rev[ \t]*\(.*\)/\1/p' ${_specfile})

[ -d ${_bzrname}/ ] && \
  rm -rvf ${_bzrname}/
[ -d ${_bzrname}-bzr${_bzrrev}/ ] && \
  rm -rvf ${_bzrname}-bzr${_bzrrev}/

bzr branch ${_bzrtrunk} ${_bzrname} -r ${_bzrrev}

mv ${_bzrname}/ ${_bzrname}-bzr${_bzrrev}/

tar -Jcv --exclude-vcs -f ${_bzrname}-bzr${_bzrrev}.tar.xz \
  ${_bzrname}-bzr${_bzrrev}/

rm -rvf ${_bzrname}-bzr${_bzrrev}/
