%define modname	GD-Graph3d
%define modver	0.63

Summary:	Create 3D Graphs with GD and GD::Graph
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/W/WA/WADG/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-GDGraph

%description
This is the GD::Graph3d extensions module. It provides 3D graphs for the
GD::Graph module by Martien Verbruggen, which in turn generates graph using
Lincoln Stein's GD.pm.

You use these modules just as you would any of the GD::Graph modules, except
that they generate 3d-looking graphs. Each graph type is described below with
only the options that are unique to the 3d version. The modules are based on
their 2d versions (e.g. GD::Graph::bars3d works like GD::Graph::bars), and
support all the options in those. Make sure to read the documentation on
GD::Graph.

%prep
%setup -qn %{modname}-%{modver}
perl -pi -e 'tr/\r//d;' Changes

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/GD
%{_mandir}/man3/*

