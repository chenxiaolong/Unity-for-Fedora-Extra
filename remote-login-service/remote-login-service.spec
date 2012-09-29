# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		remote-login-service
Version:	1.0.0
Release:	1%{?dist}
Summary:	Service to track the remote servers to use

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/remote-login-service
Source0:	https://launchpad.net/remote-login-service/1.0/%{version}/+download/remote-login-service-%{version}.tar.gz

# Disable tests: need dbus-test-runner
Patch0:		0001_Disable_tests.patch

# Do not use g_clear_pointer() on Fedora 17 (not available with glib <= 2.33)
Patch1:		0002_No_g_clear_pointer.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool

BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(python3)

Requires:	thin-client-config-agent

%description
This package contains a small service to get a list of remote servers and create
a simple DBus list.


%prep
%setup -q

%patch0 -p1 -b .no-tests
%if 0%{fedora} <= 17
%patch1 -p1 -b .g_clear_pointer
%endif

autoreconf -vfi


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/remote-login-service.conf
%dir %{_libexecdir}/remote-login-service/
%{_libexecdir}/remote-login-service/remote-login-service
%{_datadir}/dbus-1/services/com.canonical.RemoteLogin.service


%changelog
* Fri Sep 28 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0.0-1
- Initial release
- Version 1.0.0
