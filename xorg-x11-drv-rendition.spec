%define tarball xf86-video-rendition
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:    Xorg X11 rendition video driver
Name:	    xorg-x11-drv-rendition
Version:    4.2.2
Release:    4.1%{?dist}
URL:	    http://www.x.org
License:    MIT
Group:	    User Interface/X Hardware Support
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:    rendition.xinf
Patch0:	    rendition-4.2.2-abi.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 rendition video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .abi

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

rm -f $RPM_BUILD_ROOT%{moduledir}/*.uc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/rendition_drv.so
%{_datadir}/hwdata/videoaliases/rendition.xinf
%{_mandir}/man4/rendition.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 4.2.2-4.1
- Rebuilt for RHEL 6

* Tue Aug 18 2009 Adam Jackson <ajax@redhat.com> 4.2.2-4
- rendition-4.2.2-abi.patch: Fix for RAC removal and etc.

* Fri Aug 07 2009 Adam Jackson <ajax@redhat.com> 4.2.2-3
- Un-ship the microcode, it doesn't actually get loaded.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 4.2.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 4.2.2-1
- rendition 4.2.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 24 2009 Adam Jackson <ajax@redhat.com> 4.2.1-1
- rendition 4.2.1

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 4.2.0-1
- Latest upstream release

* Mon Mar 03 2008 Adam Jackson <ajax@redhat.com> 4.1.3-7.20080303
- Git snapshot for pciaccess lovin.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.1.3-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 4.1.3-5
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 4.1.3-4
- Update Requires and BuildRequires.  Add Requires: hwdata.

* Tue May 08 2007 Adam Jackson <ajax@redhat.com> 4.1.3-3
- rendition.xinf: Be non-empty.  And get installed. (#208827)

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 4.1.3-2
- ExclusiveArch -> ExcludeArch

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 4.1.3-1
- Update to 4.1.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.1.0-3.1
- rebuild

* Tue Jun 27 2006 Adam Jackson <ajackson@redhat.com> 4.1.0-3
- Build on x86_64.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 4.1.0-2
- Rebuild for 7.1 ABI fix.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 4.1.0-1
- Update to 4.1.0 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 4.0.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 4.0.1.3-1
- Updated xorg-x11-drv-rendition to version 4.0.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 4.0.1.2-1
- Updated xorg-x11-drv-rendition to version 4.0.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.
- Remove unnecessary *.data files from moduledir.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 4.0.1-1
- Updated xorg-x11-drv-rendition to version 4.0.1 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 4.0.0.1-1
- Updated xorg-x11-drv-rendition to version 4.0.0.1 from X11R7 RC1
- Fix *.la file removal.
- Added v10002d.uc, v20002d.uc, vgafont-std.data, vgafont-vrx.data,
  vgapalette.data to file manifest, although these really belong as C files
  in the source, that end up built into the driver.

* Mon Oct 03 2005 Mike A. Harris <mharris@redhat.com> 4.0.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 4.0.0-0
- Initial spec file for rendition video driver generated automatically
  by my xorg-driverspecgen script.
