%define name		freealut
%define version		1.1.0
%define	release		%mkrel 3
%define lib_name_orig	lib%{name}
%define lib_major	0
%define lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} %{lib_major} -d

Name:		%{name}
Summary:	OpenAL Utility Toolkit (ALUT)
Version:	%{version}
Release:	%{release}
License:	LGPL
Source:		http://www.openal.org/openal_webstf/downloads/%{name}-%{version}.tar.bz2
URL:		http://www.openal.org/
Group:		Sound
BuildRequires:	openal-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ALUT is the OpenAL Utility Toolkit.

%package -n	%{lib_name}
Summary:	Main library for ALUT
Group:		Sound
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with ALUT.

%package -n	%{lib_name_devel}
Summary:	Headers for developing programs that will use ALUT
Group:		Development/C

Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	openal-devel < 0.0.8-2

%description -n	%{lib_name_devel}
This package contains the headers that programmers will need to develop
applications which will use ALUT.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -n	%{lib_name} -p /sbin/ldconfig

%post -n	%{lib_name}-devel
%_install_info %{name}.info

%preun -n	%{lib_name}-devel
%_remove_install_info %{name}.info

%postun -n	%{lib_name} -p /sbin/ldconfig

%files -n	%{lib_name}
%defattr(644,root,root,0755)
%doc AUTHORS ChangeLog NEWS README
%defattr(755,root,root,0755)
%{_libdir}/*.so.*

%files -n	%{lib_name_devel}
%defattr(644,root,root,0755)
%{_includedir}/AL
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc
%defattr(755,root,root,0755)
%{_libdir}/*.so
%{_bindir}/%{name}-config


