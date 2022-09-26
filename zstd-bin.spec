#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEF8FE99528B52FFD (signing@zstd.net)
#
%define keepstatic 1
Name     : zstd-bin
Version  : 1.5.2
Release  : 96
URL      : https://github.com/facebook/zstd/releases/download/v1.5.2/zstd-1.5.2.tar.gz
Source0  : https://github.com/facebook/zstd/releases/download/v1.5.2/zstd-1.5.2.tar.gz
Source1  : https://github.com/facebook/zstd/releases/download/v1.5.2/zstd-1.5.2.tar.gz.sig
Summary  : Fast lossless compression algorithm library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: zstd-bin-bin = %{version}-%{release}
Requires: zstd-bin-filemap = %{version}-%{release}
Requires: zstd-bin-license = %{version}-%{release}
Requires: zstd-bin-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : lz4-dev
BuildRequires : lz4-dev32
BuildRequires : xz-dev
BuildRequires : xz-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: multi-thread-default.patch
Patch2: notrace.patch
Patch3: fopen-use-m.patch
Patch4: nolib.patch
Patch5: cflags.patch

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
Requires: zstd-bin-filemap = %{version}-%{release}

%description bin
bin components for the zstd-bin package.


%package filemap
Summary: filemap components for the zstd-bin package.
Group: Default

%description filemap
filemap components for the zstd-bin package.


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
%setup -q -n zstd-1.5.2
cd %{_builddir}/zstd-1.5.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a zstd-1.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661272500
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} -j8 zstd

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  PREFIX=%{_prefix} LIBDIR=%{_libdir} -j8 zstd
popd

%install
export SOURCE_DATE_EPOCH=1661272500
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zstd-bin
cp %{_builddir}/zstd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/zstd-bin/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
cp %{_builddir}/zstd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zstd-bin/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
pushd ../buildavx2/
%make_install_v3 PREFIX=%{_prefix} LIBDIR=%{_libdir}
popd
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/share/clear/optimized-elf/bin*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-zstd-bin

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zstd-bin/1d8c93712cbc9117a9e55a7ff86cebd066c8bfd8
/usr/share/package-licenses/zstd-bin/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/unzstd.1
/usr/share/man/man1/zstd.1
/usr/share/man/man1/zstdcat.1
/usr/share/man/man1/zstdgrep.1
/usr/share/man/man1/zstdless.1
