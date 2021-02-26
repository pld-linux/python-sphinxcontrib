#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Namespace for Python 2 sphinxcontrib.* packages
Summary(pl.UTF-8):	Przestrzeń nazw dla pakietów Pythona 2 sphinxcontrib.*
Name:		python-sphinxcontrib
Version:	0
Release:	3
Group:		Libraries/Python
# Only code is sourced from http://www.python.org/dev/peps/pep-0382/
License:	Public Domain
Source0:	__init__.py
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.507
Conflicts:	python-sphinxcontrib-asyncio < 0.2.0-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
This package provides sphinxcontrib namespace for Python 2 packages.

%description -l pl.UTF-8
Ten pakiet dostarcza przestrzeń nazw sphinxcontrib dla pakietów
Pythona 2.

%package -n python3-sphinxcontrib
Summary:	Namespace for Python 3 sphinxcontrib.* packages
Summary(pl.UTF-8):	Przestrzeń nazw dla pakietów Pythona 3 sphinxcontrib.*
Group:		Libraries/Python
Conflicts:	python3-sphinxcontrib-asyncio < 0.2.0-2

%description -n python3-sphinxcontrib
This package provides sphinxcontrib namespace for Python 3 packages.

%description -n python3-sphinxcontrib -l pl.UTF-8
Ten pakiet dostarcza przestrzeń nazw sphinxcontrib dla pakietów
Pythona 3.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}/sphinxcontrib

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_postclean
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/__init__.py[co]
%endif

%if %{with python3}
%files -n python3-sphinxcontrib
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/sphinxcontrib
%{py3_sitescriptdir}/sphinxcontrib/__init__.py
%dir %{py3_sitescriptdir}/sphinxcontrib/__pycache__
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/__init__.cpython-*.py[co]
%endif
