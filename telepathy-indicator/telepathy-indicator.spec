# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		telepathy-indicator
Version:	0.3.0
Release:	1%{?dist}
Summary:	Telepathy integration with the messaging menu

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/telepathy-indicator
Source0:	https://launchpad.net/telepathy-indicator/trunk/%{version}/+download/telepathy-indicator-%{version}.tar.gz

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
* Tue Oct 02 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.3.0-1
- Initial release
- Version 0.3.0
