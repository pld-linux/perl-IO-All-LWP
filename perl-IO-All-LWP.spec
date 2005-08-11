#
# Conditional build:
%bcond_without	tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	All-LWP
Summary:	IO::All::LWP - IO::All interface to LWP
Summary(pl):	IO::All::LWP - interfejs IO::All do LWP
Name:		perl-IO-All-LWP
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4d4a3041fc14c80a0c174f00a540df8a
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

%description -l pl
Modu³ ten dzia³a jako modu³ ³±cz±cy IO::All i LWP tak, ¿e mo¿na czytaæ
z plików i zapisywaæ do nich poprzez siec, korzystaj±c z wygodnego
interfejsu IO:All. Uwaga: modu³u tego nie u¿ywa siê bezpo¶rednio;
nale¿y po prostu korzystaæ z IO::All, który wie, kiedy za³adowaæ
modu³y IO::All::HTTP, IO::All::HTTPS lub IO::All::FTP implementuj±ce
poszczególne protoko³y w oparciu o IO::All::LWP.

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
