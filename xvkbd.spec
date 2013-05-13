%define name	xvkbd
%define version	3.3
%define release 1

Name: 	 	%{name}
Summary: 	Virtual (on-screen) keyboard for X
Version: 	%{version}
Release: 	%{release}

Source0:	http://homepage3.nifty.com/tsato/%{name}/%{name}-%{version}.tar.gz
URL:		http://homepage3.nifty.com/tsato/xvkbd/
License:	GPL
Group:		System/X11
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	imagemagick
BuildRequires:	imake

%description
xvkbd is a virtual (graphical) keyboard program for X Window System which
provides facility to enter characters onto other clients (softwares) by
clicking on a keyboard displayed on the screen. This may be used for systems
without a hardware keyboard such as kiosk terminals or handheld devices.

This program also has facility to send characters specified as the command
line option to another client, which can help when one wants to fully utilize
some modern mice with multiple buttons.

%prep
%setup -q

%build
xmkmf
%make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std install.man
rm -f $RPM_BUILD_ROOT/%_prefix/lib/X11/app-defaults

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Virtual Keyboard
Comment=On-screen keyboard for X
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Accessibility;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 xvkbd_icon.xbm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 xvkbd.xbm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 xvkbd.xbm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%files
%doc README
#%doc %{_prefix}/X11R6/lib/X11/doc/html/xvkbd.1.html
%_prefix/bin/*
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%{_mandir}/man1/*
%{_datadir}/applications
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.3-1
+ Revision: 802706
- BR: pkgconfig(xi)
- version update 3.3

* Fri Jan 21 2011 Funda Wang <fwang@mandriva.org> 3.0-4
+ Revision: 632026
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 3.0-3mdv2010.0
+ Revision: 435325
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 3.0-2mdv2009.0
+ Revision: 269845
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon May 05 2008 Funda Wang <fwang@mandriva.org> 3.0-1mdv2009.0
+ Revision: 201441
- update to new version 3.0

* Fri Mar 07 2008 Antoine Ginies <aginies@mandriva.com> 2.8-1mdv2008.1
+ Revision: 181236
- fix xaw3d-devel buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 16 2007 Olivier Thauvin <nanardon@mandriva.org> 2.8-1mdv2008.0
+ Revision: 52642
- 2.8

