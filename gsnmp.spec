%define major	0
%define	libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	An SNMP library implementation based on glib and gnet
Name:		gsnmp
Version:	0.3.0
Release:	10
License:	GPLv2
Group:		Networking/Other
Url:		http://www.ibr.cs.tu-bs.de/projects/scli/
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/gsnmp/%{name}-%{version}.tar.gz
Patch0:		gsnmp-linkage_fix.diff
# (fc) 0.3.0-2mdv fix m4 warning
Patch1:		gsnmp-0.3.0-fix-underquoted-warning.patch
Patch2:		gsnmp-0.3.0-automake-1.13.patch

BuildRequires:	readline-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnet-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncurses)

%description
GNET-SNMP is an SNMP library implementation based on glib and gnet. This
library has been developed as part of the scli package (an SNMP command line
interface).  Some examples demonstrating the API can be found in the examples
directory.  Some examples use stub files generated by the smidump MIB compiler,
which is part of the libsmi package.

%package -n	%{libname}
Summary:	A library of functions for the snmp protocol
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with libgsnmp.

%package -n 	%{devname}
Summary:	Development tools for the snmp protocol
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files and libraries
necessary for developing programs using libgsnmp.

%prep

%setup -q
%apply_patches
autoreconf -fis

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README 
%{_bindir}/gsnmp-get
%{_mandir}/man1/gsnmp-get.*

%files -n %{libname}
%{_libdir}/libgsnmp.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libgsnmp.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4

