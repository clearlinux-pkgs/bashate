#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bashate
Version  : 0.3.2
Release  : 12
URL      : http://tarballs.openstack.org/bashate/bashate-0.3.2.tar.gz
Source0  : http://tarballs.openstack.org/bashate/bashate-0.3.2.tar.gz
Summary  : A pep8 equivalent for bash scripts
Group    : Development/Tools
License  : Apache-2.0
Requires: bashate-bin
Requires: bashate-python
BuildRequires : Babel-python
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2-python
BuildRequires : unittest2-python
Patch1: unlock-pbr.patch
Patch2: 0001-use-testscenarios-0.5.patch

%description
===============================
bashate
===============================
A pep8 equivalent for bash scripts

%package bin
Summary: bin components for the bashate package.
Group: Binaries

%description bin
bin components for the bashate package.


%package python
Summary: python components for the bashate package.
Group: Default
Requires: Babel-python

%description python
python components for the bashate package.


%prep
%setup -q -n bashate-0.3.2
%patch1 -p1
%patch2 -p1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bashate

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
