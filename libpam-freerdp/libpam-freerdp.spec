# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		libpam-freerdp
Version:	1.0.1
Release:	1%{?dist}
Summary:	PAM module to authenticate against an RDP server with FreeRDP

Group:		System Environment/Base
License:	GPLv3
URL:		https://launchpad.net/libpam-freerdp
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/libpam-freerdp_%{version}.orig.tar.gz

# Ubuntu's gtest is packaged differently
Patch0:		0001_Disable_tests.patch

BuildRequires:	autoconf
BuildRequires:	automake

BuildRequires:	pkgconfig(freerdp)

BuildRequires:	pam-devel

Requires:	freerdp

%description
This package contains an auth and session PAM module that uses FreeRDP to
authenticate a user against an RDP server.


%prep
%setup -q

%patch0 -p1 -b .disable-tests

autoreconf -vfi


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove libtool files
find $RPM_BUILD_ROOT -type f -name '*.la' -delete


%files
%doc AUTHORS ChangeLog README
/lib/security/pam_freerdp.so
%dir %{_libexecdir}/libpam-freerdp/
%{_libexecdir}/libpam-freerdp/freerdp-auth-check


%changelog
* Sat Sep 29 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0.1-1
- Initial release
- Version 1.0.1
