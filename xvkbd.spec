Name:		xvkbd
Summary: 	Virtual (on-screen) keyboard for X
Version: 	4.1
Release: 	1

Source0:	http://t-sato.in.coocan.jp/xvkbd/%{name}-%{version}.tar.gz
URL:		http://t-sato.in.coocan.jp/xvkbd/
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
mkdir -p %{buildroot}%{_datadir}/X11
%make_install install.man
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
%lang(en) %{_datadir}/X11/words.english
