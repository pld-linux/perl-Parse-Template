%include	/usr/lib/rpm/macros.perl
%define	pdir	Parse
%define	pnam	Template
Summary:	Parse::Template - Processor for templates containing Perl expressions.
Summary(pl):	Parse::Template - procesor dla szablonów zawieraj±cych wyra¿enia perla.
Name:		perl-%{pdir}-%{pnam}
Version:	0.34
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	f211413811b6a51c6637f60259ba7b10
Patch0:		perl-ParseTemplate-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
Obsoletes:	perl-ParseTemplate
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The C<Parse::Template> class evaluates Perl expressions placed within
a text.  This class can be used as a code generator, or a generator of
documents in various document formats (HTML, XML, RTF, etc.).

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Parse/Template.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/delegation2.pl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/[^d]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/d?[^l]*
