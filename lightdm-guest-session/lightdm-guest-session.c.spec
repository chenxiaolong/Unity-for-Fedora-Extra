# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

Name:		lightdm-guest-session
Version:	1.0
Release:	1%{?dist}
Summary:	Guest Session Support for LightDM

Group:		User Interface/X
License:	GPLv3+
URL:		https://github.com/chenxiaolong/Unity-for-Fedora
Source0:	guest-account.c

Source10:	postadd_disable_gnome-screensaver
Source11:	postadd_disable_autorun
Source12:	postadd_disable_kde_settings

BuildRequires:	procps-ng-devel

Requires:	desktop-file-utils
Requires:	lightdm

%description
This package includes a helper for LightDM to create and remove a guest account.
It is rewrite of Ubuntu's guest-account script in C.


%prep
%setup -q -T -c


%build
gcc '%{SOURCE0}' -o guest-account -lprocps


%install
install -dm755 $RPM_BUILD_ROOT%{_sbindir}/
install -m755 guest-account $RPM_BUILD_ROOT%{_sbindir}/

install -dm755 $RPM_BUILD_ROOT%{_sysconfdir}/guest-session/post-add.d/
install -dm755 $RPM_BUILD_ROOT%{_sysconfdir}/guest-session/post-remove.d/

install -m755 \
  '%{SOURCE10}' \
  '%{SOURCE11}' \
  '%{SOURCE12}' \
  $RPM_BUILD_ROOT%{_sysconfdir}/guest-session/post-add.d/


%files
%{_sbindir}/guest-account
%dir %{_sysconfdir}/guest-session/
%dir %{_sysconfdir}/guest-session/post-add.d/
%dir %{_sysconfdir}/guest-session/post-remove.d/
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_gnome-screensaver
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_autorun
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_kde_settings


%changelog
* Mon Oct 01 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-1
- Initial release
- Version 1.0
