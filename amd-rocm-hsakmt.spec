%global commit0 8a9d0231a94f73ec5396b296c36fdfd5fe13ff09
%global _name amd-rocm-hsakmt
%global rocm_path /opt/rocm
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global up_name ROCT-Thunk-Interface

%define __cmake_in_source_build 1
%define patch_level 1

%bcond_with debug
%bcond_with static

%if %{without debug}
  %if %{without static}
    %global suf %{nil}
  %else
    %global suf -static
  %endif
%else
  %if %{without static}
    %global suf -debug
  %else
    %global suf -static-debug
  %endif
%endif

Name: %{_name}%{suf}

Version:        5.6.1
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}
Summary:        TBD
License:        MIT

URL:            https://github.com/trixirt/%{up_name}
Source0:        %{url}/archive/%{commit0}/%{up_name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libdrm-devel
BuildRequires:  numactl-devel
BuildRequires:  pciutils-devel

%if %{without debug}
%global debug_package %{nil}
%endif

%description
TBD

%package devel
Summary:        TBD

%description devel
%{summary}

%prep
%autosetup -p1 -n %{up_name}-%{commit0}

%build
mkdir build
cd build

%cmake .. \
%if %{with static}
       -DBUILD_SHARED_LIBS=OFF \
%endif
%if %{without debug}
       -DCMAKE_BUILD_TYPE=RELEASE \
%else
       -DCMAKE_BUILD_TYPE=DEBUG \
%endif
       -DCMAKE_INSTALL_PREFIX=%{rocm_path}

%cmake_build

%install
cd build
%cmake_install

%files devel
/opt/rocm

%changelog
* Sat Aug 05 2023 Tom Rix <trix@redhat.com>
- Stub something together

