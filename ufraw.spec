# TODO:
# - manual page for ufraw-batch?
#
# Conditional build:
%bcond_with	lensfun		# build with lensfun support

Summary:	RAW photo loader
Summary(pl.UTF-8):	Narzędzie do wczytywania zdjęć w formacie RAW
Name:		ufraw
Version:	0.16
Release:	2
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	008acc06f13efad58e0edf2dca8c6afd
URL:		http://ufraw.sourceforge.net/
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cfitsio-devel
#BuildRequires:	cinepaint-devel
BuildRequires:	exiv2-devel >= 0.11-1
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel >= 2.6
BuildRequires:	gtkimageview-devel >= 1.3
BuildRequires:	lcms-devel
%{?with_lensfun:BuildRequires:	lensfun-devel}
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info >= 0.21
Requires(post,preun):	GConf2 >= 2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles.
%if %{with lensfun}
NOTE: This package has been compiled with lensfun support which is
UFRaw is a utility to read and manipulate raw images from digital
cameras. It can be used by itself or as a GIMP plug-in. It reads raw
images using Dave Coffin's raw conversion utility DCRaw. And it
supports basic color management using Little CMS, allowing the user to
apply color profiles. considered experimental. Please read
http://ufraw.sourceforge.net/lensfun.html for information about
problems with current implementation.
%endif

%description -l pl.UTF-8
UFRaw to narzędzie do czytania i przetwarzania zdjęć w formacie RAW
różnych aparatów cyfrowych. Może być używane samodzielnie lub jako
wtyczka programu GIMP. Zdjęcia w formacie RAW są wczytywane za pomocą
programu DCRaw Dave'a Coffina. Użytkownik ma możliwość stosowania
profili kolorów dzięki bibliotece Little CMS.
%if %{with lensfun}
UWAGA: Ten pakiet został skompilowany ze wsparciem dla lensfun, które
UFRaw to narzędzie do czytania i przetwarzania zdjęć w formacie RAW
różnych aparatów cyfrowych. Może być używane samodzielnie lub jako
wtyczka programu GIMP. Zdjęcia w formacie RAW są wczytywane za pomocą
programu DCRaw Dave'a Coffina. Użytkownik ma możliwość stosowania
profili kolorów dzięki bibliotece Little CMS. jest w fazie
eksperymentalnej. Proszę zapoznać się z dokumenem
http://ufraw.sourceforge.net/lensfun.html w którym opisane są problemy
z obecną wersją.
%endif

UFRaw to narzędzie do czytania i przetwarzania zdjęć w formacie RAW
różnych aparatów cyfrowych. Może być używane samodzielnie lub jako
wtyczka programu GIMP. Zdjęcia w formacie RAW są wczytywane za pomocą
programu DCRaw Dave'a Coffina. Użytkownik ma możliwość stosowania
profili kolorów dzięki bibliotece Little CMS. jest w fazie
eksperymentalnej. Proszę zapoznać się z dokumenem
http://ufraw.sourceforge.net/lensfun.html w którym opisane są problemy
z obecną wersją.
%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl.UTF-8):	Wtyczka GIMP-a do wczytywania zdjęć w formacie RAW
Group:		Applications/Graphics

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl.UTF-8
Wtyczka GIMP-a do wczytywania zdjęć w formacie RAW.

%package batch
Summary:	RAW photo loader batch software
Summary(pl.UTF-8):	Program do wsadowego przetwarzania zdjęć w formacie RAW
Group:		Applications/Graphics

%description batch
RAW photo loader batch software.

%description batch -l pl.UTF-8
Program do wsadowego przetwarzania zdjęć w formacie RAW.

%prep
%setup -q

%build
cp -f /usr/share/automake/mkinstalldirs .
%configure \
	--enable-contrast \
	--enable-dst-correction \
	--enable-extras \
	--enable-hotpixels \
	--enable-mime \
	--with-gtk \
	--with-gimp \
	--with-exiv2 \
	%{?with_lensfun:--with-lensfun}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	schemasdir=%{_sysconfdir}/gconf/schemas

install ufraw.desktop $RPM_BUILD_ROOT%{_desktopdir}
rm -f $RPM_BUILD_ROOT%{_bindir}/dcraw

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ufraw.schemas
%update_desktop_database_post

%preun
%gconf_schema_uninstall ufraw.schemas

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/nikon-curve
%attr(755,root,root) %{_bindir}/ufraw
%{_desktopdir}/*.desktop
# XXX add extension here not to match dirs accidentally
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_mandir}/man1/ufraw*

%files -n gimp-plugin-ufraw
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/ufraw-gimp

%files batch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ufraw-batch
