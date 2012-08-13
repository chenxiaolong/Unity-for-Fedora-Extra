# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		libreoffice-menubar
Version:	0.1.1
Release:	1%{?dist}
Summary:	Global menubar plugin for LibreOffice

Group:		Applications/Productivity
License:	LGPLv3
URL:		https://launchpad.net/lo-menubar
Source0:	https://launchpad.net/lo-menubar/trunk/%{version}/+download/lo-menubar-%{version}.tar.bz2

Patch0:		0001_wscript_fixes.patch

BuildRequires:	pkgconfig

BuildRequires:	pkgconfig(dbusmenu-glib-0.4)
BuildRequires:	pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:	pkgconfig(x11)

BuildRequires:	boost-devel
BuildRequires:	libreoffice-sdk
BuildRequires:	xorg-x11-proto-devel

%description
This package contains an extension for LibreOffice which allows its menubar to
be displayed in the panel.


%prep
%setup -q -n lo-menubar-%{version}

%patch0 -p1 -b .wscript-fix


%build
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:%{_libdir}/libreoffice/ure/lib

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

./waf configure \
  --libreoffice-prefix=%{_libdir}/libreoffice \
  --ure-prefix=%{_libdir}/libreoffice/ure

./waf build


%install
./waf install \
  --libreoffice-prefix=%{_libdir}/libreoffice \
  --destdir=$RPM_BUILD_ROOT


%files
%doc README
%dir %{_libdir}/libreoffice/
%dir %{_libdir}/libreoffice/share/
%dir %{_libdir}/libreoffice/share/extensions/
%dir %{_libdir}/libreoffice/share/extensions/menubar/
%dir %{_libdir}/libreoffice/share/extensions/menubar/META-INF/
%{_libdir}/libreoffice/share/extensions/menubar/Jobs.xcu
%{_libdir}/libreoffice/share/extensions/menubar/META-INF/manifest.xml
%ifarch x86_64
%dir %{_libdir}/libreoffice/share/extensions/menubar/Linux_x86_64/
%{_libdir}/libreoffice/share/extensions/menubar/Linux_x86_64/menubar.uno.so
%endif
%ifarch %{ix86}
%dir %{_libdir}/libreoffice/share/extensions/menubar/Linux_x86/
%{_libdir}/libreoffice/share/extensions/menubar/Linux_x86/menubar.uno.so
%endif


%changelog
* Mon Aug 13 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.1.1-1
- Initial release
- Version 0.1.1
