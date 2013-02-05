# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		unity-firefox-extension
Version:	2.4.4bzr13.01.29
Release:	1%{?dist}
Summary:	Firefox extension for Unity integration

Group:		User Interface/Desktops
License:	GPLv3+
URL:		https://launchpad.net/unity-firefox-extension
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/unity-firefox-extension_%{version}.orig.tar.gz

Patch0:		0001_Multilib.patch

BuildRequires:	/usr/bin/xsltproc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	zip

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libunity_webapps-0.2)

%description
(contains no files)


%package -n firefox-unity
Summary:	Firefox extension for Unity integration
Group:		User Interface/Desktops

Requires:	firefox
Requires:	firefox-websites-integration
Requires:	libufe-xidgetter = %{version}-%{release}
Requires:	libunity-webapps

%description -n firefox-unity
This package contains a Firefox extension which allows WebApps to integrate with
the Unity desktop.


# Ubuntu/upstream: please provide a description on what this library does :)
%package -n libufe-xidgetter
Summary:	Firefox extension for Unity integration
Group:		System Environment/Libraries

%description -n libufe-xidgetter
This package contains a Firefox extension which allows WebApps to integrate with
the Unity desktop.


%prep
%setup -q

%patch0 -p1 -b .multilib

sed -i 's|@LIBDIR@|%{_libdir}|g' \
  unity-firefox-extension/content/unity-xid-helper.js \
  unity-firefox-extension/tools/gir-ctypes.xslt

pushd libufe-xidgetter/
autoreconf -vfi
popd


%build
pushd libufe-xidgetter/
%configure --disable-static
make %{?_smp_mflags}
popd

pushd unity-firefox-extension/
bash ./build.sh
popd


%install
pushd libufe-xidgetter/
make install DESTDIR=$RPM_BUILD_ROOT
popd

pushd unity-firefox-extension/
EMID=$(sed -n 's/.*<em:id>\(.*\)<\/em:id>.*/\1/p' install.rdf | head -1)
install -dm755 $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/
unzip unity.xpi -d $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/
popd

# Use Fedora logo
rm $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/skin/cof.png
ln -s %{_datadir}/pixmaps/fedora-logo-sprite.png \
  $RPM_BUILD_ROOT%{_libdir}/firefox/extensions/${EMID}/skin/cof.png

# Remove libtool files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete


%post -n libufe-xidgetter -p /sbin/ldconfig

%postun -n libufe-xidgetter -p /sbin/ldconfig


%files -n firefox-unity
%doc unity-firefox-extension/COPYING
%{_libdir}/firefox/extensions/webapps-team@lists.launchpad.net/


%files -n libufe-xidgetter
%doc libufe-xidgetter/COPYING
%{_libdir}/libufe-xidgetter.so
%{_libdir}/libufe-xidgetter.so.0
%{_libdir}/libufe-xidgetter.so.0.0.0


%changelog
* Tue Feb 05 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.4.4bzr13.01.29-1
- Version 2.4.4bzr13.01.29

* Sat Oct 20 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.3.5-1
- Version 2.3.5

* Sun Oct 07 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.3.4-3
- Use Fedora logo

* Sun Oct 07 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.3.4-2
- Add 0001_Multilib.patch
  - Load libraries from appropriate multilib libdir

* Thu Oct 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.3.4-1
- Initial release
- Version 2.3.4
