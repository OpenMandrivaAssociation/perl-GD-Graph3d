%define upstream_name	 GD-Graph3d
%define upstream_version 0.63

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Create 3D Graphs with GD and GD::Graph
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/W/WA/WADG/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-GDGraph
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/GD
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.630.0-4mdv2012.0
+ Revision: 765281
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.630.0-3
+ Revision: 763774
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.630.0-2
+ Revision: 667155
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.630.0-1mdv2010.1
+ Revision: 403185
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.63-12mdv2009.0
+ Revision: 223766
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.63-11mdv2008.1
+ Revision: 180400
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.63-10mdv2008.0
+ Revision: 23407
- rebuild


* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-9mdk
- fix buildrequires

* Tue Mar 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-8mdk
- fix doc file encoding

* Tue Mar 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-7mdk
- spec cleanup
- %%mkrel
- rpmbuilupdate aware
- fix directory ownership
- better summary, description and url

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.63-6mdk
- rebuild for new perl

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.63-5mdk
- fix deps

* Fri Sep 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.63-4mdk
- rebuilt

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.63-3mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro
- don't own man directories, only man pages..

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.63-2mdk
- rebuild for new auto{prov,req}

