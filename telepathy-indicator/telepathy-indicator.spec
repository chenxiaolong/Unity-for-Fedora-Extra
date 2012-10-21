# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu3

Name:		telepathy-indicator
Version:	0.3.0
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	Telepathy integration with the messaging menu

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/telepathy-indicator
Source0:	https://launchpad.net/telepathy-indicator/trunk/%{version}/+download/telepathy-indicator-%{version}.tar.gz

Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/telepathy-indicator_%{version}-%{_ubuntu_rel}.debian.tar.gz

BuildRequires:	intltool

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(messaging-menu)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(unity)

%description
This package contains a service that allows telepathy to integrate with the
messaging menu.


%prep
%setup -q

# Apply Ubuntu's patches
tar zxvf '%{SOURCE99}'
for i in $(grep -v '#' debian/patches/series); do
  patch -Np1 -i "debian/patches/${i}"
done


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog
%{_sysconfdir}/xdg/autostart/telepathy-indicator.desktop
%{_bindir}/telepathy-indicator


%changelog
* Sat Oct 20 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.3.0-1.0ubuntu3
- Version 0.3.0
- Ubuntu release 0ubuntu3

* Tue Oct 02 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.3.0-1
- Initial release
- Version 0.3.0
