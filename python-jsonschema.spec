# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-jsonschema
Epoch: 100
Version: 4.18.0
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
Requires: python3-attrs >= 22.2.0
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
Requires: python3-attrs >= 22.2.0
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-jsonschema-specifications >= 2023.03.6
Requires: python3-pkgutil-resolve-name >= 1.3.10
Requires: python3-referencing >= 0.28.4
Requires: python3-rpds-py >= 0.7.1
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
Requires: python3-attrs >= 22.2.0
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-jsonschema-specifications >= 2023.03.6
Requires: python3-pkgutil-resolve-name >= 1.3.10
Requires: python3-referencing >= 0.28.4
Requires: python3-rpds-py >= 0.7.1
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
