%define sname	alut
%define major	0
%define libname %mklibname %{sname} %{major}
%define devname %mklibname %{sname} -d

Summary:	OpenAL Utility Toolkit (ALUT)
Name:		freealut
Version:	1.1.0
Release:	26
License:	LGPLv2
Group:		Sound
Url:		http://www.openal.org
Source0:	http://connect.creativelabs.com/openal/Downloads/ALUT/%{name}-%{version}.tar.gz
Patch0:		%{name}-openal.patch
BuildRequires:	pkgconfig(openal)

%description
ALUT is the OpenAL Utility Toolkit.

%package -n %{libname}
Summary:	Main library for ALUT
Group:		Sound
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}freealut0 < 1.1.0-1

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with ALUT.

%package -n %{devname}
Summary:	Headers for developing programs that will use ALUT
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}freealut-devel < 1.1.0-1

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use ALUT.

%prep
%setup -q
%autopatch -p1

%build
./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/libalut.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/AL
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
%{_bindir}/%{name}-config

