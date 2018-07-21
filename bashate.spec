#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bashate
Version  : 0.5.1
Release  : 31
URL      : http://tarballs.openstack.org/bashate/bashate-0.5.1.tar.gz
Source0  : http://tarballs.openstack.org/bashate/bashate-0.5.1.tar.gz
Summary  : A pep8 equivalent for bash scripts
Group    : Development/Tools
License  : Apache-2.0
Requires: bashate-bin
Requires: bashate-python3
Requires: bashate-license
Requires: bashate-python
Requires: Babel
Requires: pbr
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
bashate
        ===============================
        
        A pep8 equivalent for bash scripts
        
        This program attempts to be an automated style checker for bash scripts
        to fill the same part of code review that pep8 does in most OpenStack
        projects. It started from humble beginnings in the DevStack project,
        and will continue to evolve over time.

%package bin
Summary: bin components for the bashate package.
Group: Binaries
Requires: bashate-license

%description bin
bin components for the bashate package.


%package license
Summary: license components for the bashate package.
Group: Default

%description license
license components for the bashate package.


%package python
Summary: python components for the bashate package.
Group: Default
Requires: bashate-python3

%description python
python components for the bashate package.


%package python3
Summary: python3 components for the bashate package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bashate package.


%prep
%setup -q -n bashate-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532216693
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/bashate
cp LICENSE %{buildroot}/usr/share/doc/bashate/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bashate

%files license
%defattr(-,root,root,-)
/usr/share/doc/bashate/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
