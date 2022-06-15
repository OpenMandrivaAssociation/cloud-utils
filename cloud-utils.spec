Summary:	Cloud image management utilities
Name:		cloud-utils
Version:	0.33
Release:	1
License:	GPLv3
URL:		https://github.com/canonical/cloud-utils
Source0:	https://github.com/canonical/cloud-utils/archive/refs/tags/%{version}.tar.gz
BuildArch:	noarch
Requires:	growpart
Requires:	gawk
Requires:	e2fsprogs
Requires:	file
Requires:	python
Requires:	qemu-img
Requires:	util-linux

%description
This package provides a useful set of utilities for managing cloud images.

The tasks associated with image bundling are often tedious and repetitive. The
cloud-utils package provides several scripts that wrap the complicated tasks
with a much simpler interface.

%package -n growpart
Summary:	Script for growing a partition
Requires:	gawk
# gptfdisk is only required for resizing GPT partitions and depends on libicu
# (25MB). We don't make this a hard requirement to save some space in non-GPT
# systems.
Recommends:	gptfdisk
Requires:	util-linux
%rename %{name}-growpart

%description -n growpart
This package provides the growpart script for growing a partition. It is
primarily used in cloud images and development boards where an image has
to be DD-ed to an SD card to grow the root or home partition on first boot.

%prep
%autosetup -p1

%build

%install
# Create the target directories
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1

# Install binaries and manpages
cp bin/* $RPM_BUILD_ROOT/%{_bindir}/
cp man/* $RPM_BUILD_ROOT/%{_mandir}/man1/

# Exclude Ubuntu-specific tools
rm $RPM_BUILD_ROOT/%{_bindir}/*ubuntu*

# Exclude the cloud-run-instances manpage
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/cloud-run-instances.*

# Exclude euca2ools wrappers and manpages
rm -f $RPM_BUILD_ROOT/%{_bindir}/cloud-publish-*
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/cloud-publish-*

# Install the growpart binary and man page
cp bin/growpart $RPM_BUILD_ROOT/%{_bindir}/
cp man/growpart.* $RPM_BUILD_ROOT/%{_mandir}/man1/

%files
%doc ChangeLog
%license LICENSE
%{_bindir}/cloud-localds
%{_bindir}/write-mime-multipart
%{_bindir}/ec2metadata
%{_bindir}/resize-part-image
%{_bindir}/mount-image-callback
%{_bindir}/vcs-run
%doc %{_mandir}/man1/resize-part-image.*
%doc %{_mandir}/man1/write-mime-multipart.*
%doc %{_mandir}/man1/cloud-localds.*

%files -n growpart
%doc ChangeLog
%license LICENSE
%{_bindir}/growpart
%doc %{_mandir}/man1/growpart.*
