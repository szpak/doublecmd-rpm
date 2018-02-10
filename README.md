# Nightly builds of Double Commander for Fedora [![Build Status Travis](https://travis-ci.org/szpak/doublecmd-rpm.svg?branch=master)](https://travis-ci.org/szpak/doublecmd-rpm)

This project provides nightly (weekly) builds of [Double Commander](http://doublecmd.sourceforge.net/) for Fedora using [Travis](https://travis-ci.org/) and [COPR](http://copr.fedorainfracloud.org/).

[Double Commander](http://doublecmd.sourceforge.net/) is open source file manager with two panels side by side. It is inspired by Total Commander and features some new ideas.

**Beta warning**. The nightly builds are produced directly from the source code repository and may be unstable. If you prefer stable releases the author provides a dedicated stable RPM [repository](https://software.opensuse.org/download.html?project=home%3AAlexx2000&package=doublecmd-gtk).

## Quick start

Enable a COPR repository in Fedora and install a package:

```
sudo dnf copr enable vondruch/doublecmd 
sudo dnf install doublecmd-gtk
```

The package will be upgraded automatically together by the other system upgrades installed via `dnf` (or `Package updater`). The new versions are automatically released, usually on a weekly basis.

More infromation: the project's [COPR repository](https://copr.fedorainfracloud.org/coprs/vondruch/doublecmd/).

## Support

Issues related to the (nightly) **Fedora build only** (e.g. missing new versions) can be reported via the GitHub [issues tracker](https://github.com/szpak/doublecmd-rpm/issues).

Bugs, questions and feature requests related to **Double Commander itself** should be posted using the project [support forum](https://doublecmd.sourceforge.io/forum/).

The nightly Fedora builds are provided to you by [Marcin Zajączkowski](https://github.com/szpak/) and [Vít Ondruch](https://copr.fedorainfracloud.org/coprs/vondruch/).

The Travis build script is licensed under the terms of [the Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt).
