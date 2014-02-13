Summary:	Cloud image management utilities
Name:		cloud-utils
Version:	0.27
Release:	1
License:	GPLv3+
Group:		Networking/Other
Url:		https://launchpad.net/ubuntu/+source/cloud-utils
Source:		https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:	LICENSE
Patch0:		0001-supress-partx-usage-error.patch
Requires:	%{name}-growpart
Requires:	e2fsprogs
Requires:	euca2ools
Requires:	file
Requires:	gawk
Requires:	python-paramiko
Requires:	qemu-img
Requires:	util-linux
BuildArch:	noarch

%description
This package provides a useful set of utilities for managing cloud
images.

The euca2ools package (a dependency of cloud-utils) provides an Amazon
EC2 API compatible set of utilities for bundling kernels, ramdisks,
and root filesystems, and uploading them to either EC2 or UEC.

The tasks associated with image bundling are often tedious and
repetitive.  The cloud-utils package provides several scripts
that wrap the complicated tasks with a much simpler interface.

%files
%doc ChangeLog LICENSE
%{_bindir}/cloud-localds
%{_bindir}/cloud-publish-tarball
%{_bindir}/cloud-run-instances
%{_bindir}/write-mime-multipart
%{_bindir}/cloud-publish-image
%{_bindir}/ec2metadata
%{_bindir}/resize-part-image
%doc %{_mandir}/man1/cloud-publish-image.*
%doc %{_mandir}/man1/cloud-publish-tarball.*
%doc %{_mandir}/man1/cloud-run-instances.*
%doc %{_mandir}/man1/resize-part-image.*
%doc %{_mandir}/man1/write-mime-multipart.*

#----------------------------------------------------------------------------

%package growpart
Summary:	Script for growing a partition
Group:		Networking/Other
Requires:	gawk
# gdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
#Requires:	gdisk
Requires:	util-linux
Conflicts:	%{name} < 0.27

%description growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images in conjunction with the dracut-modules-growroot
package to grow the root partition on first boot.

%files growpart
%doc ChangeLog LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
cp %{SOURCE1} LICENSE
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

cp bin/* %{buildroot}%{_bindir}/
cp man/* %{buildroot}%{_mandir}/man1/

rm -f %{buildroot}%{_bindir}/*ubuntu*

# Install the growpart binary and man page
cp bin/growpart %{buildroot}%{_bindir}/
cp man/growpart.* %{buildroot}%{_mandir}/man1/

