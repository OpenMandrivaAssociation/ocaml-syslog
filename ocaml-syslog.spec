%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Syslog routines for OCaml
Name:		ocaml-syslog
Version:	1.4
Release:	7
License:	LGPLv2.1+
Group:		Development/Other
Url:		https://homepage.mac.com/letaris
Source0:	http://homepage.mac.com/letaris/syslog-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Syslog routines for OCaml.

%files
%doc Changelog doc/syslog/html
%dir %{_libdir}/ocaml/syslog
%{_libdir}/ocaml/syslog/*.cmi
%{_libdir}/ocaml/syslog/*.cma
%{_libdir}/ocaml/syslog/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/syslog/*.a
%{_libdir}/ocaml/syslog/*.cmxa
%{_libdir}/ocaml/syslog/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n syslog-%{version}

%build
make
make opt
make htdoc

%install
install -d -m 755 %{buildroot}%{_libdir}/ocaml
install -d -m 755 %{buildroot}%{_defaultdocdir}/%{name}/html
ocamlfind install syslog META -destdir %{buildroot}%{_libdir}/ocaml \
  syslog.cmi syslog.mli syslog.cma syslog.cmxa syslog.a
rm -f %{buildroot}%{_libdir}/ocaml/stublibs/*.owner

