# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu3

Name:		webapps-applications
Version:	2.4.10
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	Unity WebApp integration scripts

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://launchpad.net/webapps-applications
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/webapps-applications_%{version}.orig.tar.gz

Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/webapps-applications_%{version}-%{_ubuntu_rel}.debian.tar.gz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gnome-common

BuildRequires:	python-polib

BuildRequires:	pkgconfig(libunity_webapps-0.2)

%description
(no files)


%package -n unity-webapps-common
Summary:	Unity WebApp integration scripts
Group:		User Interface/Desktops

BuildArch:	noarch

Requires:	unity-webapps-service
Requires:	xdg-utils

%description -n unity-webapps-common
This package contains example scripts for WebApp integration with the Unity
desktop.


%prep
%setup -q -n webapps-%{version}

# Apply Ubuntu's patches
tar zxvf '%{SOURCE99}'
for i in $(grep -v '#' debian/patches/series); do
  patch -p1 -i "debian/patches/${i}"
done


%build
%configure --enable-default-applications
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

install -dm755 $RPM_BUILD_ROOT%{_bindir}/
install -m755 scripts/install-default-webapps-in-launcher.py \
  $RPM_BUILD_ROOT%{_bindir}/webapps-add-defaults-to-launcher

# What is heck is zn_CN? zh stands for the first two letter of the pinyin of
# 中文 (zhongwen)
mv $RPM_BUILD_ROOT%{_datadir}/locale/{zn,zh}_CN/

desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/UbuntuOneMusiconeubuntucom.desktop
desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/ubuntu-amazon-default.desktop

%find_lang webapps


%post -n unity-webapps-common
touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null || :

%postun
if [ ${1} -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor/ &>/dev/null
  gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache -f %{_datadir}/icons/hicolor/ &>/dev/null || :


%files -n unity-webapps-common -f webapps.lang
%doc AUTHORS
%{_bindir}/webapps-add-defaults-to-launcher
%{_datadir}/applications/UbuntuOneMusiconeubuntucom.desktop
%{_datadir}/applications/ubuntu-amazon-default.desktop
%{_datadir}/icons/hicolor/128x128/apps/amazon-store.png
%{_datadir}/icons/hicolor/128x128/apps/ubuntuone-music.png
%{_datadir}/icons/unity-webapps-applications/
%dir %{_datadir}/unity-webapps/
%dir %{_datadir}/unity-webapps/userscripts/
%{_datadir}/unity-webapps/userscripts/Amazon/
%{_datadir}/unity-webapps/userscripts/common/


%changelog
* Tue Feb 05 2013 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.4.10-1.0ubuntu3
- Version 2.4.10
- Ubuntu release 0ubuntu3

* Thu Oct 04 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 2.4.7-1
- Initial release
- Version 2.4.7
