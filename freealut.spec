%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		freealut
Summary:	OpenAL Utility Toolkit (ALUT)
Version:	1.1.0
Release:	%mkrel 10
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

rm -f %{buildroot}%{_libdir}/*.la

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
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
%{_bindir}/%{name}-config


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-9mdv2011.0
+ Revision: 664353
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-8mdv2011.0
+ Revision: 605216
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2010.1
+ Revision: 522670
- rebuilt for 2010.1

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 1.1.0-6mdv2010.0
+ Revision: 419591
- update file list
- drop la files (openal does not ship la files now)

* Sat Aug 02 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.1.0-5mdv2009.0
+ Revision: 260499
- Redid freealut-oopenal.patch to fix underlinking in libalut.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.0-4mdv2008.1
+ Revision: 101395
- rebuild for new era
- new devel library policy
- new license policy
- add patch 0 (stolen from Fedora ;)
- spec file clean


* Tue Dec 05 2006 Olivier Blin <oblin@mandriva.com> 1.1.0-3mdv2007.0
+ Revision: 90690
- make devel package conflicts with old openal-devel

* Tue Dec 05 2006 Olivier Blin <oblin@mandriva.com> 1.1.0-2mdv2007.1
+ Revision: 90658
- initial freealut release
- Create freealut

