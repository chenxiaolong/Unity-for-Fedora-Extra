# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

# This package is for the OBS only! It contains workarounds for the OBS and
# takes a longer time to build than the regular version of this package.

%define _bzr_rev 348
%define _fedora_xul_ver 14.0.1
%define _fedora_xul_rel 5.fc17

%global debug_package %{nil}

Name:		globalmenu-extension
Version:	3.2.6
Release:	1%{?dist}
Summary:	Global menubar extension for Firefox and Thunderbird

Group:		Applications/Internet
License:	GPLv2 and LGPLv2 and MPLv1.1
URL:		https://launchpad.net/globalmenu-extension
Source0:	globalmenu-extension-bzr%{_bzr_rev}.tar.xz
# Create source 0 by running this script (change _bzr_rev above as needed)
Source1:	create-source-from-bzr-rev.sh
# We need to download the latest xulrunner packages from Koji because OBS does
# not use the updates repository. This causes globalmenu-extension to link with
# an old version of xulrunner (which breaks the extension).
Source2:	http://kojipkgs.fedoraproject.org//packages/xulrunner/%{_fedora_xul_ver}/%{_fedora_xul_rel}/%{_arch}/xulrunner-%{_fedora_xul_ver}-%{_fedora_xul_rel}.%{_arch}.rpm
Source3:	http://kojipkgs.fedoraproject.org//packages/xulrunner/%{_fedora_xul_ver}/%{_fedora_xul_rel}/%{_arch}/xulrunner-devel-%{_fedora_xul_ver}-%{_fedora_xul_rel}.%{_arch}.rpm

BuildRequires:	autoconf213
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

BuildRequires:	pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(libxul)

%description
(No files installed)


%package -n firefox-globalmenu
Summary:	Global menubar extension for Firefox
Group:		Applications/Internet

Requires:	firefox

%description -n firefox-globalmenu
This package contains an extension for Firefox which provides global menubar
support.


%package -n thunderbird-globalmenu
Summary:	Global menubar extension for Thunderbird
Group:		Applications/Internet

Requires:	thunderbird

%description -n thunderbird-globalmenu
This package contains an extension for Thunderbird which provides global menubar
support.


%prep
%setup -q -n %{name}-bzr%{_bzr_rev}

# Set up xulrunner
mkdir fedora_xulrunner
pushd fedora_xulrunner

# Extract official RPM's
rpm2cpio '%{SOURCE2}' | cpio -idmv
rpm2cpio '%{SOURCE3}' | cpio -idmv

XUL_DIR=$(pkg-config --variable=sdkdir libxul)
XUL_DIR=${XUL_DIR#/}

# Fix symlinks to point to our xulrunner, not the system one
for i in bin idl include lib \
         sdk/lib/libmozalloc.so \
         sdk/lib/libmozjs.so \
         sdk/lib/libxpcom.so \
         sdk/lib/libxul.so; do
  TEMP_LINK=$(readlink ${XUL_DIR}/${i})
  rm ${XUL_DIR}/${i}
  ln -s $(pwd)${TEMP_LINK} ${XUL_DIR}/${i}
done

popd

# xulrunner-devel is multilib
sed -i '/MOZILLA_VERSION/ s/mozilla-config\.h/mozilla-config%{__isa_bits}.h/' \
  ./configure.in

autoconf-2.13


%build
# This package uses the Firefox/Thunderbird build system, so we need to disable
# features unneeded for global menubar support or else configure checks for extra
# dependencies.
%configure \
  --disable-pango \
  --disable-gnomevfs \
  --disable-gconf \
  --disable-libnotify \
  --disable-gnomeui \
  --disable-dbus \
  --disable-crypto \
  --disable-jsd \
  --disable-dbm \
  --disable-accessibility \
  --disable-printing \
  --disable-ogg \
  --disable-webm \
  --disable-wave \
  --disable-permissions \
  --disable-negotiateauth \
  --disable-xtf \
  --disable-pref-extensions \
  --disable-system-extension-dirs \
  --disable-universalchardet \
  --disable-angle \
  --disable-crashreporter \
  --disable-libjpeg-turbo \
  --disable-installer \
  --disable-updater \
  --disable-tests \
  --disable-parental-controls \
  --disable-feeds \
  --disable-zipwriter \
  --disable-libconic \
  --disable-necko-wifi \
  --disable-cookies \
  --disable-ctypes \
  `# Globalmenu related options` \
  --enable-application=extensions \
  --enable-extensions=globalmenu \
  `# --with-libxul-sdk=$(pkg-config --variable=sdkdir libxul)` \
  --with-libxul-sdk=$(pwd)/fedora_xulrunner$(pkg-config --variable=sdkdir libxul) \
  --with-system-nspr

make %{?_smp_mflags}


%install
EMID_GLOBAL=$(sed -n 's/^.*<em:id>\(.*\)<\/em:id>/\1/p' extensions/globalmenu/install.rdf | head -n 1)
%define _emid ${EMID_GLOBAL}

DIR_FIREFOX=$RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID_GLOBAL}
DIR_THUNDERBIRD=$RPM_BUILD_ROOT%{_libdir}/thunderbird/extensions/${EMID_GLOBAL}

install -dm755 ${DIR_FIREFOX} ${DIR_THUNDERBIRD}

pushd dist/xpi-stage/globalmenu/
  find -type f -o -type l | while read FILE; do
    PERM=0644
    # If the file is a library, then install with the correct permissions and
    # strip the library.
    if [[ "${FILE}" =~ ".so" ]]; then
      PERM=0755
      strip "${FILE}"
    fi
    install -Dm${PERM} "${FILE}" \
      ${DIR_FIREFOX}/$(dirname "${FILE}")/$(basename "${FILE}")
    install -Dm${PERM} "${FILE}" \
      ${DIR_THUNDERBIRD}/$(dirname "${FILE}")/$(basename "${FILE}")
  done
popd


%files -n firefox-globalmenu
%dir %{_libdir}/firefox/extensions/*/
%dir %{_libdir}/firefox/extensions/*/chrome/
%dir %{_libdir}/firefox/extensions/*/components/
%{_libdir}/firefox/extensions/*/install.rdf
%{_libdir}/firefox/extensions/*/chrome/globalmenu.jar
%{_libdir}/firefox/extensions/*/components/components.manifest
%{_libdir}/firefox/extensions/*/components/globalmenu.xpt
%{_libdir}/firefox/extensions/*/components/interfaces.manifest
%{_libdir}/firefox/extensions/*/components/libglobalmenu.so
%{_libdir}/firefox/extensions/*/chrome.manifest


%files -n thunderbird-globalmenu
%dir %{_libdir}/thunderbird/extensions/*/
%dir %{_libdir}/thunderbird/extensions/*/chrome/
%dir %{_libdir}/thunderbird/extensions/*/components/
%{_libdir}/thunderbird/extensions/*/install.rdf
%{_libdir}/thunderbird/extensions/*/chrome/globalmenu.jar
%{_libdir}/thunderbird/extensions/*/components/components.manifest
%{_libdir}/thunderbird/extensions/*/components/globalmenu.xpt
%{_libdir}/thunderbird/extensions/*/components/interfaces.manifest
%{_libdir}/thunderbird/extensions/*/components/libglobalmenu.so
%{_libdir}/thunderbird/extensions/*/chrome.manifest


%changelog
* Sun Aug 12 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 3.2.6-1
- Initial release
- Version 3.2.6 (bzr rev 428 tags this release)
