%define name	gsnmp
%define lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}
%define develname	%mklibname %{name} -d

Summary:	An SNMP library implementation based on glib and gnet
Name:		%{name}
Version:	0.3.0
Release:	%mkrel 3
License:	GPLv2
Group:		Networking/Other
URL:		http://www.ibr.cs.tu-bs.de/projects/scli/
Source0:	ftp://ftp.ibr.cs.tu-bs.de/local/gsnmp/%{name}-%{version}.tar.bz2
Patch0:		gsnmp-linkage_fix.diff
# (fc) 0.3.0-2mdv fix m4 warning
Patch1:		gsnmp-0.3.0-fix-underquoted-warning.patch
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	libglib2-devel
BuildRequires:	libgnet2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GNET-SNMP is an SNMP library implementation based on glib and gnet. This
library has been developed as part of the scli package (an SNMP command line
interface).  Some examples demonstrating the API can be found in the examples
directory.  Some examples use stub files generated by the smidump MIB compiler,
which is part of the libsmi package.

%package -n	%{lib_name}
Summary:	A library of functions for the snmp protocol
Group:		System/Libraries

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with libgsnmp.

%package -n 	%{develname}
Summary:	Development tools for the snmp protocol
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release} glib2-devel
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{lib_name}-devel

%description -n %{develname}
This package contains the header files and libraries
necessary for developing programs using libgsnmp.

%prep

%setup -q
%patch0 -p0
%patch1 -p1 -b .fix_underquoted

autoreconf -fis
%build

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_bindir}/gsnmp-get
%{_mandir}/man1/gsnmp-get.*

%files -n %{lib_name}
%{_libdir}/libgsnmp.so.*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/libgsnmp.a
%{_libdir}/libgsnmp.la
%{_libdir}/libgsnmp.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4
