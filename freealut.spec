%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		freealut
Summary:	OpenAL Utility Toolkit (ALUT)
Version:	1.1.0
Release:	%mkrel 5
License:	LGPLv2
Group:		Sound
URL:		http://www.openal.org
Source:		http://www.openal.org/openal_webstf/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-openal.patch
BuildRequires:	openal-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ALUT is the OpenAL Utility Toolkit.

%package -n %{libname}
Summary:	Main library for ALUT
Group:		Sound
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with ALUT.

%package -n %{develname}
Summary:	Headers for developing programs that will use ALUT
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d
Provides:	%mklibname %{name} 0 -d
Conflicts:	openal-devel < 0.0.8-2

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use ALUT.

%prep
%setup -q
%patch0 -p1 -b .openal

%build
./autogen.sh

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%post -n %{develname}
%_install_info %{name}.info

%preun -n %{develname}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/AL
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
%{_bindir}/%{name}-config
