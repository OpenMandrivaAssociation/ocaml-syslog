%define name	ocaml-syslog
%define up_name syslog
%define version	1.4
%define release	%mkrel 5

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


%changelog
* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-5mdv2010.0
+ Revision: 390307
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-4mdv2009.1
+ Revision: 320758
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Wed Jul 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-3mdv2009.0
+ Revision: 233047
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-2mdv2009.0
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-2mdv2008.0
+ Revision: 77683
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdv2008.0
+ Revision: 77093
- import ocaml-syslog


* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-1mdv2008.0
- contributed by Andre Nathan <andre@digirati.com.br>
