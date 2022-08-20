%global debug_package %{nil}

Name: python-jsonschema
Epoch: 100
Version: 4.14.0
Release: 1%{?dist}
BuildArch: noarch
Summary: An implementation of JSON Schema validation for Python
License: MIT
URL: https://github.com/python-jsonschema/jsonschema/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
jsonschema is an implementation of the JSON Schema specification for
Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-jsonschema
Summary: An implementation of JSON Schema validation for Python
Requires: python3
Requires: python3-attrs >= 17.4.0
Requires: python3-importlib-metadata
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-pkgutil-resolve-name >= 1.3.10
Requires: python3-pyrsistent >= 0.14.0
Requires: python3-typing-extensions
Provides: python3-jsonschema = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-jsonschema
jsonschema is an implementation of the JSON Schema specification for
Python.

%files -n python%{python3_version_nodots}-jsonschema
%license COPYING
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-jsonschema
Summary: An implementation of JSON Schema validation for Python
Requires: python3
Requires: python3-attrs >= 17.4.0
Requires: python3-importlib-metadata
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-pkgutil-resolve-name >= 1.3.10
Requires: python3-pyrsistent >= 0.14.0
Requires: python3-typing-extensions
Provides: python3-jsonschema = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema) = %{epoch}:%{version}-%{release}

%description -n python3-jsonschema
jsonschema is an implementation of the JSON Schema specification for
Python.

%files -n python3-jsonschema
%license COPYING
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-jsonschema
Summary: An implementation of JSON Schema validation for Python
Requires: python3
Requires: python3-attrs >= 17.4.0
Requires: python3-importlib-metadata
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-pkgutil-resolve-name >= 1.3.10
Requires: python3-pyrsistent >= 0.14.0
Requires: python3-typing-extensions
Provides: python3-jsonschema = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema) = %{epoch}:%{version}-%{release}

%description -n python3-jsonschema
jsonschema is an implementation of the JSON Schema specification for
Python.

%files -n python3-jsonschema
%license COPYING
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
