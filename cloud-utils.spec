Name:           cloud-utils
Version:        0.19
Release:        %mkrel 1
License:        GPL3
Summary:        Cloud image management utilities
Url:            https://launchpad.net/ubuntu/+source/cloud-utils
Group:          Productivity/Networking/System
Source:         cloud-utils_0.19ubuntu1.tar.gz
BuildRequires:  sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:       python euca2ools file e2fsprogs >= 1.4  python-yaml python-paramiko
Requires:       licenses

%description
This package provides a useful set of utilities for managing cloud
images.
The euca2ools package (a dependency of cloud-utils) provides an
Amazon EC2 API compatible set of utilities for bundling kernels,
ramdisks, and root filesystems, and uploading them to either EC2
or UEC.
The tasks associated with image bundling are often tedious and
repetitive.  The cloud-utils package provides several scripts
that wrap the complicated tasks with a much simpler interface.

%prep
%setup -q -n cloud-utils-0.19ubuntu1

%build
sed -i 's@/usr/share/common-licenses/GPL-3@/usr/share/doc/licenses/gpl-3.0.txt@' debian/copyright

%install
cat debian/install | while read a b; do
	install -D -m 0755 $a %{buildroot}/$b/$a
done
cat debian/manpages | while read a; do
	section=${a#*.}
	install -D -m 0644 $a %{buildroot}/usr/share/man/man${section}/$a
done

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc debian/copyright debian/changelog
%{_bindir}/*
%{_mandir}/*

