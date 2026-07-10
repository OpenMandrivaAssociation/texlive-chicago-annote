%global tl_name chicago-annote
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Chicago-based annotated BibTeX style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago-annote
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a revision of chicagoa.bst, using the commonly-used annote field
in place of the original's annotation.

