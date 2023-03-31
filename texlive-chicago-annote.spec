Name:		texlive-chicago-annote
Version:	15878
Release:	2
Summary:	Chicago-based annotated BibTeX style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chicago-annote/chicago-annote.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicago-annote.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a revision of chicagoa.bst, using the commonly-used
annote field in place of the original's annotation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chicago-annote/chicago-annote.bst
%doc %{_texmfdistdir}/doc/bibtex/chicago-annote/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
