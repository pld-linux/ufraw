
# todo:
# - manual page for ufraw-batch?

Summary:	RAW photo loader
Name:		ufraw
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	2074676b9437738630eee72b9fc6c50c
URL:		http://ufraw.sourceforge.net/
BuildRequires:	gimp-devel
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _plugindir      %(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital cameras.
It can be used by itself or as a GIMP plug-in.  It reads raw images using
Dave Coffin's raw conversion utility DCRaw.  And it supports basic color
management using Little CMS, allowing the user to apply color profiles.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Group:		Applications

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%package batch
Summary:	RAW photo loader batch software
Group:		Applications

%description batch
RAW photo loader GIMP plugin.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man1/ufraw*

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/ufraw-gimp

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch
