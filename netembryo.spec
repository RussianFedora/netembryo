#%%define git 1
%define rev 20071031

Summary: Network abstraction library
Name: netembryo
Version: 0.1.1
Release: 1%{?git:.%{rev}git}%{?dist}
License: LGPLv2+
Group: Development/Libraries
%if %{?git:1}0
# http://live.polito.it/gitweb/?p=netembryo.git;a=snapshot;h=HEAD
Source: %{name}-%{rev}git.tar.gz
%else
Source: http://www.lscube.org/files/downloads/netembryo/%{name}-%{version}.tar.bz2
%endif
URL: http://www.lscube.org/projects/netembryo
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lksctp-tools-devel
%{?git:BuildRequires: libtool}

%description
Netembryo is a network abstraction library (originated from our old wrapper
socket) plus some misc utility functions used as foundation for feng,
libnemesi, felix.

It provides an uniform access to the following protocols:

    * UDP
    * TCP
    * SCTP

%package devel
Summary: Netembryo development library and headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The netembryo-devel package contains the header files and some
documentation needed to develop application with netembryo.

%prep
%setup -q %{?git:-n %{name}.git}

%build
%{?git:autoreconf -i}
%configure --disable-dependency-tracking --disable-static --without-openssl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%{__rm} %{buildroot}%{_libdir}/libnetembryo.la

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/libnetembryo.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/netembryo
%{_libdir}/libnetembryo.so
%{_libdir}/pkgconfig/libnetembryo*.pc

%changelog
* Tue Feb 15 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.1.1-1
- Update to 0.1.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 25 2009 Dominik Mierzejewski <rpm at greysector.net> 0.0.9-1
- updated to 0.0.9
- explicitly disabled openssl support (requires exception in the license)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Dominik Mierzejewski <rpm at greysector.net> 0.0.5-4
- fix Source and project URLs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.5-2
- Autorebuild for GCC 4.3

* Tue Jan 01 2008 Dominik Mierzejewski <rpm at greysector.net> 0.0.5-1
- updated to 0.0.5 (security update)

* Sun Nov 11 2007 Dominik Mierzejewski <rpm at greysector.net> 0.0.4-1
- updated to release

* Thu Nov 01 2007 Dominik Mierzejewski <rpm at greysector.net> 0.0.4-0.3.20071031git
- updated to latest snaphot (requested by upstream)
- really fixed changelog version

* Wed Oct 24 2007 Dominik Mierzejewski <rpm at greysector.net> 0.0.4-0.2.20071011
- fixed changelog version
- capitalized -devel Summary
- added test directory to -devel docs
- use disttag

* Thu Oct 11 2007 Dominik Mierzejewski <rpm at greysector.net> 0.0.4-0.1.20071011
- latest git snapshot
