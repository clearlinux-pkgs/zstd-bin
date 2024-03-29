#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xEF8FE99528B52FFD (signing@zstd.net)
#
%define keepstatic 1
Name     : zstd-bin
Version  : 1.5.6
Release  : 109
URL      : https://github.com/facebook/zstd/releases/download/v1.5.6/zstd-1.5.6.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.5.6/zstd-1.5.6.tar.gz
Source1  : https://github.com/facebook/zstd/releases/download/v1.5.6/zstd-1.5.6.tar.gz.sig
Summary  : Fast lossless compression algorithm library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-bin-bin = %{version}-%{release}
Requires: zstd-bin-license = %{version}-%{release}
Requires: zstd-bin-man = %{version}-%{release}
BuildRequires : lz4-dev
BuildRequires : lz4-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: multi-thread-default.patch
Patch2: notrace.patch
Patch3: fopen-use-m.patch
Patch4: nolib.patch
Patch5: cflags.patch
Patch6: quiet.patch

%description
Zstandard, or zstd as short version, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level and better compression
ratios. It's backed by a very fast entropy stage, provided by Huff0 and FSE
library. The project is provided as an open-source dual BSD and GPLv2 licensed
C library, and a command line utility producing and decoding .zst, .gz, .xz and
.lz4 files.

%package bin
Summary: bin components for the zstd-bin package.
Group: Binaries
Requires: zstd-bin-license = %{version}-%{release}

%description bin
bin components for the zstd-bin package.


%package license
Summary: license components for the zstd-bin package.
Group: Default

%description license
license components for the zstd-bin package.


%package man
Summary: man components for the zstd-bin package.
Group: Default

%description man
man components for the zstd-bin package.


%prep
%setup -q -n zstd-1.5.6
cd %{_builddir}/zstd-1.5.6
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
pushd ..
cp -a zstd-1.5.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711736801
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} -j8 zstd

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} -j8 zstd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711736801
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zstd-bin
cp %{_builddir}/zstd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/zstd-bin/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8 || :
cp %{_builddir}/zstd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zstd-bin/d5e630eee1d3500039f2e16bed21d0f0cd580994 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3 PREFIX=%{_prefix} LIBDIR=%{_libdir}
popd
GOAMD64=v2
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/zstd
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd-bin/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/zstd-bin/d5e630eee1d3500039f2e16bed21d0f0cd580994

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1
