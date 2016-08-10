Name:           libmp4v2
Version:        2.0.0
Release:        1%{?dist}
Summary:        Library for working with files using the mp4 container format

License:        MPLv1.1
URL:            http://code.google.com/p/mp4v2
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/mp4v2/mp4v2-%{version}.tar.bz2

%description
The MP4v2 library provides an API to create and modify mp4 files as defined by
ISO-IEC:14496-1:2001 MPEG-4 Systems. This file format is derived from Apple's
QuickTime file format that has been used as a multimedia file format in a
variety of platforms and applications. It is a very powerful and extensible
format that can accommodate practically any type of media.

MP4v2 was originally bundled with mpeg4ip library, but has been moved into its
own maintained library due to a combination of the cessation of support of
mpeg4ip and the usefulness of this library on its own.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n mp4v2-utils
Summary:        Utilities for work with mp4 containers

%description    -n mp4v2-utils
This package contains the utilities for work with mp4 containers.


%prep
%setup -q -n mp4v2-%{version}


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING doc/Authors.txt doc/ReleaseNotes.txt
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so

%files -n mp4v2-utils
%doc doc/ToolGuide.txt
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.0.0-1
- Public release
