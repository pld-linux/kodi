# TODO:
#  - fix build flags - some files are compiled with -O3 and without rpm*flags
#  - add and/or fix users/groups permissions
#  - split to subpackages?
# - bundled ffmpeg build (tools/depends/target/ffmpeg/autobuild.sh) enables nonfree & gpl!
#
# Conditional build:
# Features:
%bcond_with	afpclient	# AFP support via libafpclient
%bcond_without	airplay		# AirPlay support
%bcond_with	airtunes	# AirTunes support
%bcond_without	alsa		# ALSA support
%bcond_without	avahi		# Avahi support
%bcond_without	dbus		# DBUS support
%bcond_without	dvdcss		# DVDCSS support
%bcond_without	gl		# OpenGL rendering
%bcond_with	gtest		# configure Google Test Framework
%bcond_without	joystick	# SDL joystick support
%bcond_without	libcap		# libcap support
%bcond_with	libcec		# libcec support
%bcond_without	libgif		# gif support via libgif
%bcond_without	libusb		# libusb support
%bcond_with	mdnsembedded	# mDNSEmbedded support
%bcond_without	mysql		# MySQL
%bcond_without	nfs		# NFS support via libnfs
%bcond_without	non_free	# componentents with non-compliant licenses
%bcond_with	openmax		# OpenMax decoding, requires OpenGLES
%bcond_without	optical_drive	# optical drive
%bcond_without	projectm	# ProjectM visualisation
%bcond_without	pulse		# PulseAudio support
%bcond_without	rtmp		# RTMP support via librtmp
%bcond_without	samba		# SAMBA support
%bcond_without	sdl		# SDL
%bcond_without	ssh		# SSH SFTP support
%bcond_without	texturepacker	# texturepacker support
%bcond_without	udev		# udev support
%bcond_without	upnp		# UPnP support
%bcond_without	vaapi		# VAAPI decoding
%bcond_without	vdpau		# VDPAU decoding
%bcond_with	vtbdecoder	# VTBDecoder decoding (VTB Decoder not supported on this platform)
%bcond_without	webserver	# webserver
%bcond_without	x11		# x11 'Linux Only'
%bcond_without	xrandr		# XRandR support
%bcond_with	asap_codec	# ASAP ADPCM support
%bcond_with	gles		# OpenGLES rendering
%bcond_without	libbluray	# libbluray support
%bcond_without	mid		# MID support
%bcond_with	profiling	# gprof profiling
%bcond_with	tegra		# Tegra2 arm
%bcond_with	wayland		# wayland
# System libs:
%bcond_without	system_ffmpeg	# build with system ffmpeg
%bcond_without	system_dvdread	# build with system dvdread

%define	codename Krypton
Summary:	Kodi is a free and open source media-player and entertainment hub
Name:		kodi
Version:	17.6
Release:	1
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
#Source0:	http://mirrors.kodi.tv/releases/source/%{version}-%{codename}.tar.gz
Source0:	https://github.com/xbmc/xbmc/archive/%{version}-%{codename}.tar.gz
# Source0-md5:	a64c2fc56ddc41b9b0dded55eaabf170
Patch0:		jpeglib-boolean.patch
Patch1:		disable-static.patch
Patch2:		dvdread.patch
Patch3:		ffmpeg3.patch
Patch4:		gcc5.patch
URL:		http://kodi.tv/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	crossguid-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	dcadec-devel
BuildRequires:	doxygen
# libavcodec >= 56.26.100 libavfilter >= 5.11.102 libavformat >= 56.25.101 libavutil >= 54.20.100 libpostproc >= 53.3.100 libswscale >= 3.1.101 libswresample >= 1.1.100
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 2.4.4}
BuildRequires:	flac-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
%{?with_libgif:BuildRequires:	giflib-devel}
BuildRequires:	glew-devel
BuildRequires:	gperf
BuildRequires:	jasper-devel
BuildRequires:	jre
BuildRequires:	libass-devel
BuildRequires:	libatomic-devel
BuildRequires:	libbluray-devel >= 0.7.0
BuildRequires:	libcap-devel
BuildRequires:	libcdio-devel
%{?with_libcec:BuildRequires:	libcec-devel >= 3.0.0}
BuildRequires:	libdrm-devel
%{?with_system_dvdread:BuildRequires:	libdvdread-devel}
%ifarch i686 pentium4 athlon %{x8664}
BuildRequires:	libcrystalhd-devel
%endif
BuildRequires:	libgcrypt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
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
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libva-devel
BuildRequires:	libva-x11-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
BuildRequires:	lzo-devel
BuildRequires:	mysql-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	openssl-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.0
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRequires:	swig
BuildRequires:	taglib-devel >= 1.8
BuildRequires:	tinyxml-devel >= 2.6.2
BuildRequires:	udev-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	yajl-devel >= 2
BuildRequires:	zip
BuildRequires:	zlib-devel
# kodi uses it's own, modified squish
BuildConflicts:	squish-devel
#https://github.com/sahlberg/libnfs
BuildRequires:	libnfs-devel
#http://sites.google.com/site/alexthepuffin/home
#BuildRequires:	afpfs-ng-devel
#BuildRequires:	shairplay-devel
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
#%patch0 -p1
%patch1 -p1
#%{?with_system_dvdread:%patch2 -p1}
#%patch3 -p1
#%patch4 -p1

#%{__rm} -r lib/cximage-6.0/zlib
#%{__rm} -r lib/libhdhomerun
#%{__rm} -r lib/libmpeg2
#%{__rm} -r xbmc/cores/dvdplayer/DVDCodecs/Video/libmpeg2
#%{__rm} -r lib/libbluray
#%{__rm} -r lib/librtmp
%{__rm} -r lib/win32
#%{?with_system_dvdread:%{__rm} -r lib/libdvd/libdvdread}

%if %{without system_ffmpeg}
#ln -s %{SOURCE1} tools/depends/target/ffmpeg/ffmpeg-2.4.4-%{codename}.tar.gz
%endif

%build
#%{__make} -C tools/depends/native/libsquish-native \
#	CXX="%{__cxx}"

./bootstrap
%configure \
	ac_cv_type__Bool=yes \
	--disable-silent-rules \
	--disable-debug \
	--disable-ccache \
	--with-ffmpeg=%{!?with_system_ffmpeg:force}%{?with_system_ffmpeg:shared} \
	%{__enable_disable afpclient} \
	%{__enable_disable airplay} \
	%{__enable_disable airtunes} \
	%{__enable_disable alsa} \
	%{__enable_disable asap_codec asap-codec} \
	%{__enable_disable avahi} \
	%{__enable_disable dbus} \
	%{__enable_disable dvdcss} \
	%{__enable_disable gles} \
	%{__enable_disable gl} \
	%{__enable_disable gtest} \
	%{__enable_disable joystick} \
	%{__enable_disable libbluray} \
	%{__enable_disable libcap} \
	%{__enable_disable libcec} \
	%{__enable_disable libgif} \
	%{__enable_disable libusb} \
	%{__enable_disable mdnsembedded} \
	%{__enable_disable mid} \
	%{__enable_disable mysql} \
	%{__enable_disable nfs} \
	%{__enable_disable non_free non-free} \
	%{__enable_disable openmax} \
	%{__enable_disable optical_drive optical-drive} \
	%{__enable_disable profiling} \
	%{__enable_disable pulse} \
	%{__enable_disable rtmp} \
	%{__enable_disable samba} \
	%{__enable_disable sdl} \
	%{__enable_disable ssh} \
	%{__enable_disable tegra} \
	%{__enable_disable texturepacker} \
	%{__enable_disable udev} \
	%{__enable_disable upnp} \
	%{__enable_disable vaapi} \
	%{__enable_disable vdpau} \
	%{__enable_disable vtbdecoder} \
	%{__enable_disable wayland} \
	%{__enable_disable webserver} \
	%{__enable_disable x11} \
	%{__enable_disable xrandr} \
	%{nil}

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# no -devel package yet
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/kodi
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/xbmc

# no real use for symlinks to datadir, and make rpm packaging more difficult (symlink vs dir issues)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xbmc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/xbmc

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
%{_datadir}/xsessions/xbmc.desktop
