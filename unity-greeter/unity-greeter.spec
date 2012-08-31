# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu2

Name:		unity-greeter
Version:	12.10.2
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	LightDM Unity Greeter

Group:		User Interface/X
License:	GPLv3
URL:		https://launchpad.net/unity-greeter
Source0:	https://launchpad.net/unity-greeter/12.10/%{version}/+download/unity-greeter-%{version}.tar.gz

Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/unity-greeter_%{version}-%{_ubuntu_rel}.debian.tar.gz

Patch0:		0001_Link_against_m.patch
Patch1:		0002_Beefy_Miracle_Background.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	pkgconfig
BuildRequires:	vala-tools

BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(liblightdm-gobject-1)

Requires:	gnome-settings-daemon
Requires:	indicator-datetime
#Requires:	indicator-power
Requires:	indicator-session
Requires:	indicator-sound
Requires:	NetworkManager-gnome

Requires:	beefy-miracle-backgrounds-single
Requires:	fedora-logos

%description
This package contains the greeter (login screen) application for Unity. It is
implemented as a LightDM greeter.


%prep
%setup -q

%patch0 -p1 -b .link_against_m
%patch1 -p1 -b .beefy_miracle

# Apply Ubuntu's patches
tar zxvf '%{SOURCE99}'
for i in $(grep -v '#' debian/patches/series); do
  patch -Np1 -i "debian/patches/${i}"
done

autoreconf -vfi


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Use Fedora logo
rm $RPM_BUILD_ROOT%{_datadir}/unity-greeter/logo.png
ln -s /usr/share/pixmaps/system-logo-white.png \
  $RPM_BUILD_ROOT%{_datadir}/unity-greeter/logo.png

# Install PolicyKit rule
install -dm755 \
  $RPM_BUILD_ROOT%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/
install -m644 debian/unity-greeter.pkla \
  $RPM_BUILD_ROOT%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/

%find_lang unity-greeter


%postun
if [ ${1} -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f unity-greeter.lang
%doc ChangeLog NEWS README
%{_sbindir}/unity-greeter
%{_datadir}/glib-2.0/schemas/com.canonical.unity-greeter.gschema.xml
%{_mandir}/man1/unity-greeter.1.gz
%dir %{_datadir}/unity-greeter/
%{_datadir}/unity-greeter/*.png
%{_datadir}/unity-greeter/*.svg
%dir %{_datadir}/xgreeters/
%{_datadir}/xgreeters/unity-greeter.desktop
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/unity-greeter.pkla


%changelog
* Thu Aug 30 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 12.10.2-1.0ubuntu2
- Initial release
- Version 12.10.2
- Ubuntu release 0ubuntu2
