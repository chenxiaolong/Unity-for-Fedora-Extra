# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

%define _ubuntu_rel 0ubuntu5

Name:		ubuntu-fonts
Version:	0.80
Release:	1.%{_ubuntu_rel}%{?dist}
Summary:	A sans-serif font hinted for clarity

Group:		User Interface/X
# See source package for the actual text of the Ubuntu Font License v1.0
License:	Freely redistributable without restriction
URL:		http://font.ubuntu.com/
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-font-family-sources_%{version}.orig.tar.gz

# Programs for creating the console fonts
Source10:	http://www.math.nmsu.edu/~mleisher/Software/otf2bdf/otf2bdf-3.1.tbz2
Source11:	http://ftp.de.debian.org/debian/pool/main/c/console-setup/console-setup_1.82.tar.gz


Source99:	https://launchpad.net/ubuntu/+archive/primary/+files/ubuntu-font-family-sources_%{version}-%{_ubuntu_rel}.debian.tar.gz

#BuildRequires:	
#Requires:	

BuildArch:	noarch

%description
The Ubuntu Font Family are a set of matching new libre/open fonts in development
during 2010--2011. The development is being funded by Canonical Ltd on behalf
the wider Free Software community and the Ubuntu project. The technical font
design work and implementation is being undertaken by Dalton Maag.

Both the final font Truetype/OpenType files and the design files used to produce
the font family are distributed under an open license and you are expressly
encouraged to experiment, modify, share and improve.


%prep
%setup -q -n ubuntu-font-family-sources-%{version} -a10 -a11 -a99


%build
mkdir bin

pushd otf2bdf-3.1
%configure
make %{?_smp_mflags}
cp otf2bdf ../bin/
popd

pushd console-setup-1.82/Fonts/
cp bdf2psf ../../bin/
popd

PATH="${PATH}:$(pwd)/bin" make -C debian/console


%install
# Install TTF fonts
install -dm755 $RPM_BUILD_ROOT%{_datadir}/fonts/ubuntu-font-family/
install -m644 \
  Ubuntu-L*.ttf \
  Ubuntu-R*.ttf \
  `# Ubuntu-M*.ttf # Ubuntu does not ship these` \
  Ubuntu-B*.ttf \
  Ubuntu-C.ttf \
  UbuntuMono-*.ttf \
  $RPM_BUILD_ROOT%{_datadir}/fonts/ubuntu-font-family/

# Install Console fonts
install -dm755 $RPM_BUILD_ROOT%{_prefix}/lib/kbd/consolefonts/
install -m644 debian/console/*.psf \
  $RPM_BUILD_ROOT%{_prefix}/lib/kbd/consolefonts/

sed 's|/usr/share/consolefonts|%{_prefix}/lib/kbd/consolefonts|g' \
  < debian/console/README \
  > $RPM_BUILD_ROOT%{_prefix}/lib/kbd/consolefonts/README.Ubuntu


%files
%doc CONTRIBUTING.txt copyright.txt FONTLOG.txt LICENCE-FAQ.txt LICENCE.txt
%doc README.txt TRADEMARKS.txt
%dir %{_datadir}/fonts/ubuntu-font-family/
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-LI.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-L.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-RI.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-R.ttf
#%{_datadir}/fonts/ubuntu-font-family/Ubuntu-MI.ttf
#%{_datadir}/fonts/ubuntu-font-family/Ubuntu-M.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-BI.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-B.ttf
%{_datadir}/fonts/ubuntu-font-family/Ubuntu-C.ttf
%{_datadir}/fonts/ubuntu-font-family/UbuntuMono-BI.ttf
%{_datadir}/fonts/ubuntu-font-family/UbuntuMono-B.ttf
%{_datadir}/fonts/ubuntu-font-family/UbuntuMono-RI.ttf
%{_datadir}/fonts/ubuntu-font-family/UbuntuMono-R.ttf
%dir %{_prefix}/lib/kbd/
%dir %{_prefix}/lib/kbd/consolefonts/
%{_prefix}/lib/kbd/consolefonts/README.Ubuntu
%{_prefix}/lib/kbd/consolefonts/UbuntuMono-B-8x16.psf
%{_prefix}/lib/kbd/consolefonts/UbuntuMono-BI-8x16.psf
%{_prefix}/lib/kbd/consolefonts/UbuntuMono-R-8x16.psf
%{_prefix}/lib/kbd/consolefonts/UbuntuMono-RI-8x16.psf


%changelog
* Sat Oct 20 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.80-1.0ubuntu5
- Version 0.80
- Ubuntu release 0ubuntu5

* Mon Sep 24 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 0.80-1.0ubuntu4
- Initial release
- Version 0.80
- Ubuntu release 0ubuntu4
