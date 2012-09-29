# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		lightdm-remote-session-freerdp
Version:	1.0
Release:	1%{?dist}
Summary:	Session and configuration files to log in with FreeRDP

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/lightdm-remote-session-freerdp
Source0:	https://launchpad.net/lightdm-remote-session-freerdp/1.0/%{version}/+download/lightdm-remote-session-freerdp-%{version}.tar.gz

Requires:	freerdp
Requires:	libpam-freerdp
Requires:	lightdm
Requires:	zenity

%description
THis package contains the configuration files and scripts necessary to log in to
a full screen RDP session using LightDM and FreeRDP.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rv $RPM_BUILD_ROOT%{_sysconfdir}/apparmor.d/


%files
%doc AUTHORS ChangeLog README
%{_sysconfdir}/pam.d/lightdm-remote-freerdp
%dir %{_libexecdir}/lightdm-remote-session-freerdp/
%{_libexecdir}/lightdm-remote-session-freerdp/freerdp-session-wrapper
%{_libexecdir}/lightdm-remote-session-freerdp/socket-sucker
%dir %{_datadir}/lightdm-remote-session-freerdp/
%{_datadir}/lightdm-remote-session-freerdp/freerdp-session
%dir %{_datadir}/lightdm/remote-sessions/
%{_datadir}/lightdm/remote-sessions/freerdp.desktop


%changelog
* Sat Sep 29 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-1
- Initial release
- Version 1.0
