#
# spec file for package perl-Test-Archive-Libarchive (Version 0.02)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name Test-Archive-Libarchive
Name:           perl-Test-Archive-Libarchive
Version:        0.02
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Testing tools for Archive::Libarchive
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  (rpm-build-perl or perl-generators)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Tools::Basic) >= 0.000121
BuildRequires:  perl(Test2::Tools::Compare) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(Ref::Util)
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::Tools::Basic) >= 0.000121
Requires:       perl(Test2::Tools::Compare) >= 0.000121
Provides:       perl(Test::Archive::Libarchive)
%{perl_requires}

%description
Error handling for 'libarchive' and Archive::Libarchive is fairly
primitive. Most methods return an 'int' which correspond to 'ARCHIVE_EOF',
'ARCHIVE_OK', 'ARCHIVE_RETRY', 'ARCHIVE_WARN', 'ARCHIVE_FAILED' or
'ARCHIVE_FATAL'. Some methods will also return the number of actual bytes
written on success and one of these codes on failure. It can be tedious
doing the necessary checks for each method call in a test, so this module
provides tools for testing Archive::Libarchive method calls that follow
this pattern.

%prep
%autosetup  -n %{cpan_name}-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
