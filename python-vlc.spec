#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-vlc
Version  : 3.0.10114
Release  : 12
URL      : https://files.pythonhosted.org/packages/3a/17/e8bd7e99af5972b9927e9ab994fad1d5e878960b4e4d0fd8e29f28fef5c1/python-vlc-3.0.10114.tar.gz
Source0  : https://files.pythonhosted.org/packages/3a/17/e8bd7e99af5972b9927e9ab994fad1d5e878960b4e4d0fd8e29f28fef5c1/python-vlc-3.0.10114.tar.gz
Summary  : VLC bindings for python.
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: python-vlc-license = %{version}-%{release}
Requires: python-vlc-python = %{version}-%{release}
Requires: python-vlc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Python ctypes-based bindings libvlc
===================================
The bindings use ctypes to directly call the libvlc dynamic lib, and
the code is generated from the include files defining the public
API. The same module should be compatible with various versions of
libvlc 3.*. However, there may be incompatible changes between major
versions.

%package license
Summary: license components for the python-vlc package.
Group: Default

%description license
license components for the python-vlc package.


%package python
Summary: python components for the python-vlc package.
Group: Default
Requires: python-vlc-python3 = %{version}-%{release}

%description python
python components for the python-vlc package.


%package python3
Summary: python3 components for the python-vlc package.
Group: Default
Requires: python3-core
Provides: pypi(python_vlc)

%description python3
python3 components for the python-vlc package.


%prep
%setup -q -n python-vlc-3.0.10114
cd %{_builddir}/python-vlc-3.0.10114

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592412535
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-vlc
cp %{_builddir}/python-vlc-3.0.10114/COPYING %{buildroot}/usr/share/package-licenses/python-vlc/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-vlc/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
