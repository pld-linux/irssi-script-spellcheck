%include	/usr/lib/rpm/macros.perl
Summary:	Irssi script to check for spelling errors using Aspell
Name:		irssi-script-spellcheck
Version:	0.4
Release:	0.2
License:	distributable
Group:		Applications/Communications
Source0:	http://outpo.st/irssi/spellcheck.pl
# Source0-md5:	a0c39a5531f487c99d398bddde773a69
URL:		http://outpo.st/irssi/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	irssi >= 0.8.12-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir	%{_prefix}/share/irssi/scripts

%description
Works as you type, marking words when Aspell thinks a word was
misspelled.

It also adds suggestions to the list of tabcompletions, so once you
know last word is wrong, you can go back and tabcomplete through what
Aspell suggests.

%prep
%setup -qcT
install %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}
install *.pl $RPM_BUILD_ROOT%{_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_scriptdir}/spellcheck.pl
