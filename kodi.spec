#
# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - fix linking argument order
#  - add and/or fix users/groups permissions
#  - split to subpackages?
#
# Conditional build:
%bcond_without	cec	# build without cec support
%bcond_without	dvdcss	# DVDCSS support
%bcond_without	fishbmc		# FishBMC visualisation
%bcond_without	gl		# OpenGL rendering
%bcond_without	goom		# GOOM visualisation
%bcond_with	gtest	# configure Google Test Framework
%bcond_with	hal	# build with HAL
%bcond_without	joystick	# SDL joystick support
%bcond_without	projectm	# ProjectM visualisation
%bcond_without	rsxs		# really slick X screensavers
%bcond_without	spectrum	# Spectrum visualisation
%bcond_without	texturepacker	# texturepacker support
%bcond_without	waveform	# Waveform visualisation
%bcond_without	x11		# x11 'Linux Only'
%bcond_without	xrandr		# XRandR support

%define	codename Helix
Summary:	Kodi is a free and open source media-player and entertainment hub
Name:		kodi
Version:	14.0
Release:	0.1
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
Source0:	http://mirrors.kodi.tv/releases/source/%{version}-%{codename}.tar.gz
# Source0-md5:	9717c539789789b8aeaf1dcfdb9f2c69
Patch0:		jpeglib-boolean.patch
URL:		http://kodi.tv/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-tools
BuildRequires:	glew-devel
BuildRequires:	gperf
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	jasper-devel
BuildRequires:	jre
BuildRequires:	libass-devel
BuildRequires:	libbluray-devel >= 0.2.1
BuildRequires:	libcap-devel
BuildRequires:	libcdio-devel
%{?with_cec:BuildRequires:	libcec-devel}
%ifarch i686 pentium4 athlon %{x8664}
BuildRequires:	libcrystalhd-devel
%endif
BuildRequires:	libgcrypt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpeg2-devel
BuildRequires:	libogg-devel
BuildRequires:	libplist-devel
BuildRequires:	libpng-devel
BuildRequires:	librtmp-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libssh-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libva-glx-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxslt-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	openssl-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	python-devel >= 2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
# used internally
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	swig
BuildRequires:	taglib-devel >= 1.8
BuildRequires:	tinyxml-devel
BuildRequires:	udev-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	yajl-devel
BuildRequires:	yasm
BuildRequires:	zip
BuildRequires:	zlib-devel
#https://github.com/sahlberg/libnfs
#BuildRequires:	libnfs-devel
#http://sites.google.com/site/alexthepuffin/home
#BuildRequires:	afpfs-ng-devel
#http://mirrors.xbmc.org/build-deps/darwin-libs/libshairport-1.2.0.20310_lib.tar.gz
#https://github.com/albertz/shairport
#BuildRequires: libshairport
Requires:	/usr/bin/glxinfo
Requires:	SDL >= 1.2.14-5
Requires:	lsb-release
Requires:	xorg-app-xdpyinfo
# dlopened libraries:
# grep 'DLL_PATH_.*lib.*\.so' xbmc/DllPaths_generated.h | grep -v special://
Requires:	curl-libs
Requires:	libass
Requires:	libbluray
Requires:	libmodplug
Requires:	libmpeg2-libs
Requires:	libogg
Requires:	libplist
Requires:	libvorbis
Obsoletes:	xbmc < 14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kodi Entertainment Center (formerly XBMC) is a free and open-source
media player software developed by the XBMC Foundation, a non-profit
technology consortium. Kodi is available for multiple operating
systems and hardware platforms, with a software 10-foot user interface
for use with televisions and remote controls. It allows users to play
and view most videos, music, such as podcasts from the internet, and
all common digital media files from local and network storage media.

%prep
%setup -q -n xbmc-%{version}-%{codename}
%patch0 -p1

%build
./bootstrap
%configure \
	--disable-silent-rules \
	--disable-debug \
	--disable-afpclient \
	--disable-airtunes \
	--disable-ccache \
	--disable-libusb \
	--disable-nfs \
	--enable-pulse \
	--enable-udev \
	%{__enable_disable dvdcss} \
	%{__enable_disable fishbmc} \
	%{__enable_disable gl} \
	%{__enable_disable goom} \
	%{__enable_disable gtest} \
	%{__enable_disable gtexturepacker} \
	%{__enable_disable hal} \
	%{__enable_disable joystick} \
	%{__enable_disable libcec} \
	%{__enable_disable projectm} \
	%{__enable_disable rsxs} \
	%{__enable_disable spectrum} \
	%{__enable_disable waveform} \
	%{__enable_disable x11} \
	%{__enable_disable xrandr} \
	%{nil}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# no -devel package yet
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/kodi
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/xbmc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/README.linux
%attr(755,root,root) %{_bindir}/kodi
%attr(755,root,root) %{_bindir}/kodi-standalone
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_desktopdir}/kodi.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/xsessions/kodi.desktop

# legacy xbmc compatibility links
%attr(755,root,root) %{_bindir}/xbmc
%attr(755,root,root) %{_bindir}/xbmc-standalone
%{_libdir}/xbmc
%{_datadir}/xbmc
%{_datadir}/xsessions/xbmc.desktop
