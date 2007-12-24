#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	All-LWP
Summary:	IO::All::LWP - IO::All interface to LWP
Summary(pl.UTF-8):	IO::All::LWP - interfejs IO::All do LWP
Name:		perl-IO-All-LWP
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2971dc7889c0c523237b1fd4488c6cdb
URL:		http://search.cpan.org/dist/IO-All-LWP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IO-All >= 0.3
BuildRequires:	perl(LWP)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module acts as glue between IO::All and LWP, so that files can
be read and written through the network using the convenient IO:All
interface. Note that this module is not used directly: you just use
IO::All, which knows when to autoload IO::All::HTTP, IO::All::HTTPS,
or IO::All::FTP, which implement the specific protocols with base on
IO::All::LWP.

%description -l pl.UTF-8
Moduł ten działa jako moduł łączący IO::All i LWP tak, że można czytać
z plików i zapisywać do nich poprzez siec, korzystając z wygodnego
interfejsu IO:All. Uwaga: modułu tego nie używa się bezpośrednio;
należy po prostu korzystać z IO::All, który wie, kiedy załadować
moduły IO::All::HTTP, IO::All::HTTPS lub IO::All::FTP implementujące
poszczególne protokoły w oparciu o IO::All::LWP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/All/*.pm
%{_mandir}/man3/*
