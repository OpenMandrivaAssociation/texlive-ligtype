Name:		texlive-ligtype
Version:	63577
Release:	2
Summary:	Comprehensive ligature suppression functionalities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ligtype
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ligtype.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ligtype.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package suppresses inappropriate ligatures following
specified rules. Both font and user kerning are applied
correctly, and f-glyphs are automatically replaced with their
short-arm variant (if available). Also there is an emphasis on
speed. By default the package applies German language ligature
suppression rules. With the help of options and macros it can
be used for other languages as well. The package requires
LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/ligtype
%doc %{_texmfdistdir}/doc/lualatex/ligtype

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
