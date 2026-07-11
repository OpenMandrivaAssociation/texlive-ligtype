%global tl_name ligtype
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Comprehensive ligature suppression functionalities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/ligtype
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ligtype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ligtype.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package suppresses inappropriate ligatures following specified
rules. Both font and user kerning are applied correctly, and f-glyphs
are automatically replaced with their short-arm variant (if available).
Also there is an emphasis on speed. By default the package applies
German language ligature suppression rules. With the help of options and
macros it can be used for other languages as well. The package requires
LuaLaTeX.

