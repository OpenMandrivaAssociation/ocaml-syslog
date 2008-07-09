%define name	ocaml-syslog
%define up_name syslog
%define version	1.4
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Syslog routines for OCaml
Source:		http://homepage.mac.com/letaris/%{up_name}-%{version}.tar.gz
URL:		http://homepage.mac.com/letaris
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Syslog routines for OCaml.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

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

%files
%defattr(-,root,root)
%doc Changelog doc/syslog/html
%dir %{ocaml_sitelib}/syslog
%{ocaml_sitelib}/syslog/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/syslog/*
%exclude %{ocaml_sitelib}/syslog/*.cmi
