%define upstream_name	 GD-Graph3d
%define upstream_version 0.63

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Create 3D Graphs with GD and GD::Graph
License:	GPL+ or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/W/WA/WADG/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-GDGraph
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 'tr/\r//d;' Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/GD
%{_mandir}/*/*
