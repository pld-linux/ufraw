
# TODO:
# - manual page for ufraw-batch?

Summary:	RAW photo loader
Summary(pl):	Narzêdzie do wczytywania zdjêæ w formacie RAW
Name:		ufraw
Version:	0.10
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/ufraw/%{name}-%{version}.tar.gz
# Source0-md5:	12d9bfdb8ed22e28129a729847ba6664
URL:		http://ufraw.sourceforge.net/
BuildRequires:	exiv2-devel
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
UFRaw to narzêdzie do czytania i przetwarzania zdjêæ w formacie RAW ró¿nych
aparatów cyfrowych. Mo¿e byæ u¿ywane samodzielnie lub jako wtyczka programu
GIMP. Zdjêcia w formacie RAW s± wczytywane za pomoc± programu DCRaw Dave'a
Coffina. U¿ytkownik ma mo¿liwo¶æ stosowania profili kolorów dziêki
bibliotece Little CMS.

%package -n gimp-plugin-ufraw
Summary:	RAW photo loader GIMP plugin
Summary(pl):	Wtyczka GIMP-a do wczytywania zdjêæ w formacie RAW
Group:		Applications

%description -n gimp-plugin-ufraw
RAW photo loader GIMP plugin.

%description -n gimp-plugin-ufraw -l pl
Wtyczka GIMP-a do wczytywania zdjêæ w formacie RAW.

%package batch
Summary:	RAW photo loader batch software
Summary(pl):	Program do wsadowego przetwarzania zdjêæ w formacie RAW
Group:		Applications

%description batch
RAW photo loader batch software.

%description batch -l pl
Program do wsadowego przetwarzania zdjêæ w formacie RAW.

%prep
%setup -q

%build
%configure \
	--with-exiv2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/%{_desktopdir}
cp ufraw.desktop $RPM_BUILD_ROOT/%{_desktopdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
