# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		lightdm-remote-session-uccsconfigure
Version:	1.1
Release:	2%{?dist}
Summary:	Session and configuration files to login to configure UCCS

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/lightdm-remote-session-uccsconfigure
Source0:	https://launchpad.net/lightdm-remote-session-uccsconfigure/1.0/%{version}/+download/lightdm-remote-session-uccsconfigure-%{version}.tar.gz

Patch0:		0001_PAM_include.patch

Requires:	firefox
Requires:	lightdm
Requires:	unity

%description
This package contains the configuration files and scripts needed to run a guest
session with a browser to setup a UCCS account.


%prep
%setup -q

%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rv $RPM_BUILD_ROOT%{_sysconfdir}/apparmor.d/


%files
%doc AUTHORS ChangeLog README
%{_sysconfdir}/pam.d/lightdm-remote-uccsconfigure
%dir %{_libexecdir}/lightdm-remote-session-uccsconfigure/
%{_libexecdir}/lightdm-remote-session-uccsconfigure/uccsconfigure-session-wrapper
%dir %{_datadir}/lightdm-remote-session-uccsconfigure/
%{_datadir}/lightdm-remote-session-uccsconfigure/firefox-uccsconfigure.desktop
%{_datadir}/lightdm-remote-session-uccsconfigure/firefox-uccsconfigure.sh
%{_datadir}/lightdm-remote-session-uccsconfigure/uccsconfigure-session
%dir %{_datadir}/lightdm/remote-sessions/
%{_datadir}/lightdm/remote-sessions/uccsconfigure.desktop


%changelog
* Tue Feb 05 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.1-2
- Fix includes in PAM configuration file

* Fri Sep 28 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.1-1
- Initial release
- Version 1.1
