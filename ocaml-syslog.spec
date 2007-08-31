%define name	ocaml-syslog
%define distname syslog
%define version	1.4
%define release	%mkrel 1
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Syslog routines for OCaml.
Source:		http://homepage.mac.com/letaris/syslog-1.4.tar.gz
URL:		http://homepage.mac.com/letaris
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{distname}-%{version}

%description
Syslog routines for OCaml.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Obsoletes:	%{name}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{distname}-%{version}

%build
make 
make opt
make htdoc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%_defaultdocdir/%{name}/html
ocamlfind install syslog META -destdir %{buildroot}/%{ocaml_sitelib} \
  syslog.cmi syslog.mli syslog.cma syslog.cmxa syslog.a
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc Changelog doc/syslog/html
%{ocaml_sitelib}/syslog

