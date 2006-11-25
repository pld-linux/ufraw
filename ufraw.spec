# TODO:
# - manual page for ufraw-batch?
# - move mime-schema to _sysconfdir and package it.
Summary:	RAW photo loader
Summary(pl):	Narz�dzie do wczytywania zdj�� w formacie RAW
Name:		ufraw
Version:	0.10
Release:	2
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	12d9bfdb8ed22e28129a729847ba6664
URL:		http://ufraw.sourceforge.net/
BuildRequires:	exiv2-devel >= 0.11-1
BuildRequires:	gimp-devel >= 2.0
BuildRequires:	lcms-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _plugindir      %(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles.

%description -l pl
UFRaw to narz�dzie do czytania i przetwarzania zdj�� w formacie RAW r�nych
aparat�w cyfrowych. Mo�e by� u�ywane samodzielnie lub jako wtyczka programu
GIMP. Zdj�cia w formacie RAW s� wczytywane za pomoc� programu DCRaw Dave'a
Coffina. U�ytkownik ma mo�liwo�� stosowania profili kolor�w dzi�ki
bibliotece Little CMS.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl):	Wtyczka GIMP-a do wczytywania zdj�� w formacie RAW
Group:		Applications/Graphics

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl
Wtyczka GIMP-a do wczytywania zdj�� w formacie RAW.

%package batch
Summary:	RAW photo loader batch software
Summary(pl):	Program do wsadowego przetwarzania zdj�� w formacie RAW
Group:		Applications/Graphics

%description batch
RAW photo loader batch software.

%description batch -l pl
Program do wsadowego przetwarzania zdj�� w formacie RAW.

%prep
%setup -q

%build
%configure \
	--enable-mime \
	--with-exiv2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ufraw.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/ufraw*

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/ufraw-gimp

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch
