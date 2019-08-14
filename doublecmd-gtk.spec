%global doublecmd doublecmd
%global svn_revision 8901

Name:		doublecmd-gtk
Summary:	Twin-panel (commander-style) file manager (GTK2)
Version:	1.0.0
Release:	0.svn%{svn_revision}%{?dist}
URL:		http://doublecmd.sourceforge.net
# svn export -r 7901 http://svn.code.sf.net/p/doublecmd/code/trunk doublecmd-0.9.0
# tar cafv doublecmd-0.9.0-r7901.tar.xz doublecmd-0.9.0
Source0:	%{doublecmd}-%{version}-r%{svn_revision}.tar.xz
Patch0:		doublecmd-svn-revision-in-rpm.patch
License:	GPL
Group:		Applications/File
BuildRequires:	fpc >= 2.6.0 fpc-src glib2-devel gtk2-devel lazarus >= 1.0.0
BuildRequires:	ncurses-devel dbus-devel bzip2-devel xorg-x11-proto-devel xorg-x11-xtrans-devel
Provides:	doublecmd = %{version}-%{release}

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%prep
%setup -q -n %{doublecmd}-%{version}
%patch0 -p1

%build
# Don't use external debug symbols, since the rpmbuild's find-debuginfo can't
# find them.
sed -i '/UseExternalDbgSyms/ s/True/False/' src/doublecmd.lpi

# Keep debug info. It is stripped later by rpmbuild's find-debuginfo.sh.
sed -i '/strip/ s/^/#/' build.sh

# Since we want to have internal debug info, let's generate .zdli from it.
# http://doublecmd.sourceforge.net/mantisbt/view.php?id=963
sed -i '/extractdwrflnfo/ s/.dbg//' build.sh

# Apply SVN revision number resolved at SPEC file preparation time
DC_REVISION=%{svn_revision} install/linux/update-revision.sh . .

./build.sh beta gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}

%files
%{_libdir}/%{doublecmd}
%{_bindir}/%{doublecmd}
%{_datadir}/%{doublecmd}
%{_datadir}/applications/%{doublecmd}.desktop
%{_datadir}/icons
%{_datadir}/pixmaps/%{doublecmd}.png
%{_datadir}/polkit-1/actions/org.%{doublecmd}.root.policy
%doc %{_mandir}/man1/*

%changelog
* Thu Aug 15 2019 Marcin Zajaczkowski - CI Bot <mszpak ATT wp DOTT pl> - 1.0.0-0.svn8901
- Version built automatically - intermediate changelog entries since r8900 may be missing

* Wed Aug 14 2019 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.0-0.svn8900
- New base revision for automatically triggered CI builds in COPR - https://github.com/szpak/doublecmd-rpm
- Version number updated to 1.0.0 alpha available upstream

* Thu Jun 14 2018 Marcin Zajaczkowski - CI Bot <mszpak ATT wp DOTT pl> - 0.9.0-0.svn8101
- Version built automatically - intermediate changelog entries since r8100 may be missing

* Thu Jun 14 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.9.0-0.svn8100
- New base revision for automatically triggered CI builds in COPR - https://github.com/szpak/doublecmd-rpm
- Package also polkit policy file

* Wed Feb 21 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.9.0-0.svn7910
- New base revision for automatically triggered CI builds in COPR - https://github.com/szpak/doublecmd-rpm
- Pass SVN revision to DoubleCmd build - https://github.com/szpak/doublecmd-rpm/issues/4

* Sat Feb 10 2018 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.9.0-0.svn7900
- Base revision for automatically triggered CI builds in COPR - https://github.com/szpak/doublecmd-rpm
- Fix some rpmlint issues

* Tue Mar 07 2017 Vít Ondruch <vondruch@redhat.com> - 0.8.0-0.svn7324
- Revision 7324.

* Thu Sep 01 2016 Vít Ondruch <vondruch@redhat.com> - 0.7.4-0.svn7080
- Revision 7080.

* Mon Nov 02 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.0-0.svn6368
- Revision 6368.

* Fri Mar 06 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.0-0.svn5869
- Revision 5869.

* Mon Dec 01 2014 Vít Ondruch <vondruch@redhat.com> - 0.6.0-0.svn5681
- Revision 5681.

* Mon Feb 03 2014 Vít Ondruch <vondruch@redhat.com> - 0.6.0-0.svn5447
- Revision 5447.

* Mon Jul 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn5256
- Revision 5256.

* Wed May 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn5205
- Revision 5205.

* Mon Sep 17 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn4969
- Revision 4969.

* Mon Jul 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn4912
- Revision 4912.

* Thu Feb 23 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn4690
- Revision 4690.

* Thu Feb 23 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn4304
- Revision 4304.

* Tue Nov 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn4036
- Revision 4036.

* Wed Aug 24 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn3836
- Revision 3836.

* Fri Jun 17 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1.svn3643
- Version 0.5.5
- Revision 3643.

* Tue May 24 2011 Vít Ondruch <vondruch@redhat.com> - 0.4.6-2
- Revision 3617.

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
