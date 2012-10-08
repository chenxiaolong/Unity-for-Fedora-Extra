# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%global selinux_variants mls strict targeted

Name:		lightdm-guest-session
Version:	1.0
Release:	2%{?dist}
Summary:	Guest Session Support for LightDM

Group:		User Interface/X
License:	GPLv3+
URL:		https://github.com/chenxiaolong/Unity-for-Fedora
Source0:	guest-account.c
Source1:	guest-account.fc
Source2:	guest-account.te

Source10:	postadd_disable_gnome-screensaver
Source11:	postadd_disable_autorun
Source12:	postadd_disable_kde_settings

BuildRequires:	procps-ng-devel

BuildRequires:	checkpolicy
BuildRequires:	hardlink
BuildRequires:	selinux-policy-devel
BuildRequires:	/usr/share/selinux/devel/policyhelp

Requires:	desktop-file-utils
Requires:	lightdm

Requires(post):	/usr/sbin/semodule, /sbin/fixfiles
Requires(postun):	/usr/sbin/semodule, /sbin/fixfiles

%description
This package includes a helper for LightDM to create and remove a guest account.
It is rewrite of Ubuntu's guest-account script in C.


%prep
%setup -q -T -c

mkdir SELinux
cp -p %{SOURCE1} %{SOURCE2} SELinux


%build
gcc '%{SOURCE0}' -o guest-account -lprocps

cd SELinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv guest-account.pp guest-account.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -


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

for selinuxvariant in %{selinux_variants}
do
  install -dm755 $RPM_BUILD_ROOT%{_datadir}/selinux/${selinuxvariant}/
  install -p -m644 SELinux/guest-account.pp.${selinuxvariant} \
    $RPM_BUILD_ROOT%{_datadir}/selinux/${selinuxvariant}/guest-account.pp
done

hardlink -cv $RPM_BUILD_ROOT%{_datadir}/selinux/


%post
for selinuxvariant in %{selinux_variants}; do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/guest-account.pp &>/dev/null || :
done
/sbin/fixfiles -R lightdm-guest-session restore || :

%postun
if [ ${1} -eq 0 ]; then
  for selinuxvariant in %{selinux_variants}; do
    /usr/sbin/semodule -s ${selinuxvariant} -r guest-account &>/dev/null || :
  done
  /sbin/fixfiles -R lightdm-guest-session restore || :
fi


%files
%doc SELinux/*
%{_sbindir}/guest-account
%dir %{_sysconfdir}/guest-session/
%dir %{_sysconfdir}/guest-session/post-add.d/
%dir %{_sysconfdir}/guest-session/post-remove.d/
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_gnome-screensaver
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_autorun
%{_sysconfdir}/guest-session/post-add.d/postadd_disable_kde_settings
%{_datadir}/selinux/*/guest-account.pp


%changelog
* Mon Oct 08 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-2
- Add SELinux policy to transition from the xdm_t domain to the unconfined_t
  domain when LightDM runs guest-account
  - Allows useradd, usermod, userdel, etc to be run

* Mon Oct 01 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 1.0-1
- Initial release
- Version 1.0
