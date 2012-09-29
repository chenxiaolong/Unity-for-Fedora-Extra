# Written by: Xiao-Long Chen <chenxiaolong@cxl.epac.to>

# Based on Fedora 18's python-pycurl spec file

Name:		python3-pycurl
Version:	7.19.0
Release:	1%{?dist}
Summary:	A Python interface to libcurl

Group:		Development/Languages
License:	LGPLv2+ or MIT
URL:		http://pycurl.sourceforge.net/
Source0:	http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz

# Fedora's patches
Patch0:		python-pycurl-no-static-libs.patch
Patch1:		python-pycurl-fix-do_curl_reset-refcount.patch
# Ubuntu's patches
Patch2:		python3.patch

BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)

Requires:	keyutils-libs

# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%global libcurl_sed '/^#define LIBCURL_VERSION "/!d;s/"[^"]*$//;s/.*"//;q'
%global curlver_h /usr/include/curl/curlver.h
%global libcurl_ver %(sed %{libcurl_sed} %{curlver_h} 2>/dev/null || echo 0)

Requires:	libcurl >= %{libcurl_ver}

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch objects
identified by a URL from a Python program, similar to the urllib Python module.
PycURL is mature, very fast, and supports a lot of features.


%prep
%setup -q -n pycurl-%{version}

%patch0 -p0
#patch1 -p1
%patch2 -p1

chmod a-x examples/*


%build
CFLAGS="$RPM_OPT_FLAGS -DHAVE_CURL_OPENSSL" %{__python3} setup.py build


%check
export PYTHONPATH=$PWD/build/lib*
%{__python3} tests/test_internals.py -q


%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -rv $RPM_BUILD_ROOT%{_datadir}/doc/pycurl/


%files
%doc COPYING COPYING2 ChangeLog README TODO examples doc tests
%{python3_sitearch}/curl/
%{python3_sitearch}/pycurl-%{version}-py*.egg-info
%{python3_sitearch}/pycurl.cpython-*m.so


%changelog
* Fri Sep 28 2012 Xiao-Long Chen <chenxiaolong@cxl.epac.to> - 7.19.0-1
- Initial release
- Based on Fedora 18's python-pycurl spec file
- Version 7.19.0
