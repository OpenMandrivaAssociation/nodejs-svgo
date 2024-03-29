Name: nodejs-svgo
Version: 2.8.0
Release: 2
# Generated by tarring up the results of
# npm install -g --prefix /tmp/SVGO/usr https://registry.npmjs.org/svgo/-/svgo-2.8.0.tgz
Source0: %{name}-%{version}.tar.xz
Summary: Tool for optimizing SVG files
URL: https://github.com/svg/svgo
License: MIT
Group: Development/Other
BuildRequires: nodejs-packaging
Requires: nodejs

%description
SVG Optimizer is a Node.js-based tool for optimizing SVG vector graphics
files.

SVG files, especially those exported from various editors, usually contain a
lot of redundant and useless information. This can include editor metadata,
comments, hidden elements, default or non-optimal values and other stuff that
can be safely removed or converted without affecting the SVG rendering result.

%prep

%build

%install
mkdir -p %{buildroot}
cd %{buildroot}
tar xf %{S:0}

%files
%{_bindir}/*
%{nodejs_sitelib}/svgo
