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
%bcond_without	opengl		# OpenGL rendering
%bcond_with	gtest		# configure Google Test Framework
%bcond_without	joystick	# SDL joystick support
%bcond_without	libcap		# libcap support
%bcond_with	libcec		# libcec support
%bcond_without	gif		# GIF support via giflib
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
%bcond_with	system_dvdread	# build with system dvdread

%define	codename Leia
#define	subver	rc1
Summary:	Kodi is a free and open source media-player and entertainment hub
Name:		kodi
Version:	18.4
Release:	5
License:	GPL v2+ and GPL v3+
Group:		Applications/Multimedia
Source0:	https://github.com/xbmc/xbmc/archive/%{version}-%{codename}.tar.gz
# Source0-md5:	5e5e1e2527c2619785597b04e35fda6c
Patch0:		jpeglib-boolean.patch
Patch1:		disable-static.patch
Patch2:		dvdread.patch
Patch3:		ffmpeg3.patch
Patch4:		gcc5.patch
Patch5:		libdvd.patch
Patch6:		microhttpd.patch
Patch7:		assert.patch
URL:		https://kodi.tv/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	avahi-devel
BuildRequires:	bluez-libs-devel >= 4.99
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.4
BuildRequires:	crossguid-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	libfmt-devel >= 3.0.1
BuildRequires:	rapidjson-devel >= 1.1.0
# libavcodec >= 56.26.100 libavfilter >= 5.11.102 libavformat >= 56.25.101 libavutil >= 54.20.100 libpostproc >= 53.3.100 libswscale >= 3.1.101 libswresample >= 1.1.100
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 2.4.4}
BuildRequires:	flac-devel
BuildRequires:	flatbuffers-devel >= 1.9.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-tools
%{?with_gif:BuildRequires:	giflib-devel}
BuildRequires:	gperf
BuildRequires:	jre
BuildRequires:	lcms2-devel
BuildRequires:	libass-devel
BuildRequires:	libatomic-devel
BuildRequires:	libbluray-devel >= 0.7.0
BuildRequires:	libcap-devel
BuildRequires:	libcdio-devel
%{?with_libcec:BuildRequires:	libcec-devel >= 3.0.0}
BuildRequires:	libdrm-devel
BuildRequires:	libdvdcss-devel >= 1.4.1
%{?with_system_dvdread:BuildRequires:	libdvdread-devel}
BuildRequires:	libgcrypt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmicrohttpd-devel >= 0.9.40
BuildRequires:	libogg-devel
BuildRequires:	libplist-devel
BuildRequires:	libpng-devel
BuildRequires:	librtmp-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libssh-devel
BuildRequires:	libstdc++-devel
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
BuildRequires:	fstrcmp-devel >= 0.7
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

# extracting debug info from /home/users/glen/tmp/kodi-18.0-root-glen/usr/lib64/kodi/kodi-x11
# /usr/lib/rpm/bin/debugedit: canonicalization unexpectedly shrank by one character
%define		_noautostrip    kodi-x11
%define		_enable_debug_packages	0

%description
Kodi Entertainment Center (formerly XBMC) is a free and open-source
media player software developed by the XBMC Foundation, a non-profit
technology consortium. Kodi is available for multiple operating
systems and hardware platforms, with a software 10-foot user interface
for use with televisions and remote controls. It allows users to play
and view most videos, music, such as podcasts from the internet, and
all common digital media files from local and network storage media.

%prep
%setup -q -n xbmc-%{version}%{?subver}-%{codename}
#%patch0 -p1
%patch1 -p1
%{?with_system_dvdread:%patch2 -p1}
#%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

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
install -d build
cd build
# cmake not picking up include path from pkgconfig
# https://trac.kodi.tv/ticket/16861
%define	specflags -I/usr/include/freetype2
%cmake \
	-DENABLE_INTERNAL_LIBDVD=OFF \
	-DENABLE_INTERNAL_CROSSGUID=OFF \
	-DENABLE_DVDCSS=%{__true_false dvdcss} \
	-DENABLE_UPNP=%{__true_false upnp} \
	-DENABLE_AIRTUNES=%{__true_false airtunes} \
	-DENABLE_OPTICAL=%{__true_false optical_drive} \
	-DENABLE_INTERNAL_FFMPEG=%{!?with_system_ffmpeg:ON}%{?with_system_ffmpeg:OFF} \
	..
%if 0
%configure \
	ac_cv_type__Bool=yes \
	--disable-silent-rules \
	--disable-debug \
	--disable-ccache \
	--with-ffmpeg=%{!?with_system_ffmpeg:force}%{?with_system_ffmpeg:shared} \
	%{__enable_disable afpclient} \
	%{__enable_disable airplay} \
	%{__enable_disable alsa} \
	%{__enable_disable asap_codec asap-codec} \
	%{__enable_disable avahi} \
	%{__enable_disable dbus} \
	%{__enable_disable gles} \
	%{__enable_disable opengl gl} \
	%{__enable_disable gtest} \
	%{__enable_disable joystick} \
	%{__enable_disable libbluray} \
	%{__enable_disable libcap} \
	%{__enable_disable libcec} \
	%{__enable_disable gif libgif} \
	%{__enable_disable libusb} \
	%{__enable_disable mdnsembedded} \
	%{__enable_disable mid} \
	%{__enable_disable mysql} \
	%{__enable_disable nfs} \
	%{__enable_disable non_free non-free} \
	%{__enable_disable openmax} \
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
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_docdir}/{version.txt,README.Linux.md,LICENSE.md}

# not packaged
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/firewalld/services/kodi-*.xml

# no -devel package yet
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/kodi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/README.Linux.md
%attr(755,root,root) %{_bindir}/TexturePacker
%attr(755,root,root) %{_bindir}/kodi
%attr(755,root,root) %{_bindir}/kodi-standalone
%{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_desktopdir}/kodi.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/xsessions/kodi.desktop
