%define name	ocaml-syslog
%define up_name syslog
%define version	1.4
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Syslog routines for OCaml
Source:		http://homepage.mac.com/letaris/%{up_name}-%{version}.tar.gz
URL:		http://homepage.mac.com/letaris
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:  ocaml-findlib
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
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%_defaultdocdir/%{name}/html
ocamlfind install syslog META -destdir %{buildroot}/%{_libdir}/ocaml \
  syslog.cmi syslog.mli syslog.cma syslog.cmxa syslog.a
rm -f %{buildroot}/%{_libdir}/ocaml/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog doc/syslog/html
%dir %{_libdir}/ocaml/syslog
%{_libdir}/ocaml/syslog/*.cmi
%{_libdir}/ocaml/syslog/*.cma
%{_libdir}/ocaml/syslog/META

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/syslog/*.a
%{_libdir}/ocaml/syslog/*.cmxa
%{_libdir}/ocaml/syslog/*.mli
