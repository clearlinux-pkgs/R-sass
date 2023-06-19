#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-sass
Version  : 0.4.6
Release  : 17
URL      : https://cran.r-project.org/src/contrib/sass_0.4.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sass_0.4.6.tar.gz
Summary  : A C/C++ implementation of a Sass compiler
Group    : Development/Tools
License  : MIT
Requires: R-sass-lib = %{version}-%{release}
Requires: R-sass-license = %{version}-%{release}
Requires: R-R6
Requires: R-fs
Requires: R-htmltools
Requires: R-rappdirs
Requires: R-rlang
BuildRequires : R-R6
BuildRequires : R-fs
BuildRequires : R-htmltools
BuildRequires : R-rappdirs
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
R developers can use variables, inheritance, and functions to generate
    dynamic style sheets. The package uses the 'Sass CSS' extension language,
    which is stable, powerful, and CSS compatible.

%package lib
Summary: lib components for the R-sass package.
Group: Libraries
Requires: R-sass-license = %{version}-%{release}

%description lib
lib components for the R-sass package.


%package license
Summary: license components for the R-sass package.
Group: Default

%description license
license components for the R-sass package.


%prep
%setup -q -n sass
pushd ..
cp -a sass buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683218013

%install
export SOURCE_DATE_EPOCH=1683218013
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-sass
cp %{_builddir}/sass/src/libsass/COPYING %{buildroot}/usr/share/package-licenses/R-sass/dc6b6d4b9ae804ab0dd95d46d148ee533bec260f || :
cp %{_builddir}/sass/src/libsass/LICENSE %{buildroot}/usr/share/package-licenses/R-sass/4d640cc322117dec7f97632e6ed4319131a16ad2 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sass/DESCRIPTION
/usr/lib64/R/library/sass/INDEX
/usr/lib64/R/library/sass/LICENSE
/usr/lib64/R/library/sass/Meta/Rd.rds
/usr/lib64/R/library/sass/Meta/features.rds
/usr/lib64/R/library/sass/Meta/hsearch.rds
/usr/lib64/R/library/sass/Meta/links.rds
/usr/lib64/R/library/sass/Meta/nsInfo.rds
/usr/lib64/R/library/sass/Meta/package.rds
/usr/lib64/R/library/sass/Meta/vignette.rds
/usr/lib64/R/library/sass/NAMESPACE
/usr/lib64/R/library/sass/NEWS.md
/usr/lib64/R/library/sass/R/sass
/usr/lib64/R/library/sass/R/sass.rdb
/usr/lib64/R/library/sass/R/sass.rdx
/usr/lib64/R/library/sass/doc/index.html
/usr/lib64/R/library/sass/doc/sass.R
/usr/lib64/R/library/sass/doc/sass.Rmd
/usr/lib64/R/library/sass/doc/sass.html
/usr/lib64/R/library/sass/examples/example-full.scss
/usr/lib64/R/library/sass/examples/rules.scss
/usr/lib64/R/library/sass/examples/variables.scss
/usr/lib64/R/library/sass/help/AnIndex
/usr/lib64/R/library/sass/help/aliases.rds
/usr/lib64/R/library/sass/help/figures/logo.svg
/usr/lib64/R/library/sass/help/figures/sass-logo-color.png
/usr/lib64/R/library/sass/help/paths.rds
/usr/lib64/R/library/sass/help/sass.rdb
/usr/lib64/R/library/sass/help/sass.rdx
/usr/lib64/R/library/sass/html/00Index.html
/usr/lib64/R/library/sass/html/R.css
/usr/lib64/R/library/sass/sass-color/DESCRIPTION
/usr/lib64/R/library/sass/sass-color/README.md
/usr/lib64/R/library/sass/sass-color/app.R
/usr/lib64/R/library/sass/sass-color/rsconnect/shinyapps.io/gallery/sass-color.dcf
/usr/lib64/R/library/sass/sass-font/DESCRIPTION
/usr/lib64/R/library/sass/sass-font/README.md
/usr/lib64/R/library/sass/sass-font/app.R
/usr/lib64/R/library/sass/sass-font/rsconnect/shinyapps.io/gallery/sass-font.dcf
/usr/lib64/R/library/sass/sass-font/sass-font.scss
/usr/lib64/R/library/sass/sass-size/DESCRIPTION
/usr/lib64/R/library/sass/sass-size/README.md
/usr/lib64/R/library/sass/sass-size/app.R
/usr/lib64/R/library/sass/sass-size/rsconnect/shinyapps.io/gallery/sass-size.dcf
/usr/lib64/R/library/sass/sass-size/sass-size.scss
/usr/lib64/R/library/sass/sass-theme/DESCRIPTION
/usr/lib64/R/library/sass/sass-theme/README.md
/usr/lib64/R/library/sass/sass-theme/app.R
/usr/lib64/R/library/sass/sass-theme/rsconnect/shinyapps.io/gallery/sass-theme.dcf
/usr/lib64/R/library/sass/tests/testthat.R
/usr/lib64/R/library/sass/tests/testthat/_reset.scss
/usr/lib64/R/library/sass/tests/testthat/_snaps/font-objects.md
/usr/lib64/R/library/sass/tests/testthat/_snaps/font-objects/font-css
/usr/lib64/R/library/sass/tests/testthat/_snaps/html-dependencies.md
/usr/lib64/R/library/sass/tests/testthat/_snaps/layers.md
/usr/lib64/R/library/sass/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/sass/tests/testthat/helper-cache.R
/usr/lib64/R/library/sass/tests/testthat/helper-utils.R
/usr/lib64/R/library/sass/tests/testthat/test-assets/a.txt
/usr/lib64/R/library/sass/tests/testthat/test-assets/b/b1.txt
/usr/lib64/R/library/sass/tests/testthat/test-assets/c/c1.txt
/usr/lib64/R/library/sass/tests/testthat/test-assets/c/d/d1.txt
/usr/lib64/R/library/sass/tests/testthat/test-assets/test-layer-file.scss
/usr/lib64/R/library/sass/tests/testthat/test-cache.R
/usr/lib64/R/library/sass/tests/testthat/test-compile.R
/usr/lib64/R/library/sass/tests/testthat/test-compile.sass
/usr/lib64/R/library/sass/tests/testthat/test-compile.scss
/usr/lib64/R/library/sass/tests/testthat/test-extend.R
/usr/lib64/R/library/sass/tests/testthat/test-extend.scss
/usr/lib64/R/library/sass/tests/testthat/test-font-objects.R
/usr/lib64/R/library/sass/tests/testthat/test-html-dependencies.R
/usr/lib64/R/library/sass/tests/testthat/test-import.R
/usr/lib64/R/library/sass/tests/testthat/test-import.scss
/usr/lib64/R/library/sass/tests/testthat/test-include-path/_need.scss
/usr/lib64/R/library/sass/tests/testthat/test-include-path2/_need2.scss
/usr/lib64/R/library/sass/tests/testthat/test-include-paths.R
/usr/lib64/R/library/sass/tests/testthat/test-layers-list.R
/usr/lib64/R/library/sass/tests/testthat/test-layers.R
/usr/lib64/R/library/sass/tests/testthat/test-mixins.R
/usr/lib64/R/library/sass/tests/testthat/test-mixins.scss
/usr/lib64/R/library/sass/tests/testthat/test-nesting-expected.css
/usr/lib64/R/library/sass/tests/testthat/test-nesting-input.scss
/usr/lib64/R/library/sass/tests/testthat/test-nesting.R
/usr/lib64/R/library/sass/tests/testthat/test-option-errors.R
/usr/lib64/R/library/sass/tests/testthat/test-options.R
/usr/lib64/R/library/sass/tests/testthat/test-output.R
/usr/lib64/R/library/sass/tests/testthat/test-shiny-devmode.R
/usr/lib64/R/library/sass/tests/testthat/test-unicode-bom-expected.css
/usr/lib64/R/library/sass/tests/testthat/test-unicode-bom-input.scss
/usr/lib64/R/library/sass/tests/testthat/test-unicode-css-expected.css
/usr/lib64/R/library/sass/tests/testthat/test-unicode-css-input.scss
/usr/lib64/R/library/sass/tests/testthat/test-unicode-var-expected.css
/usr/lib64/R/library/sass/tests/testthat/test-unicode-var-input.scss
/usr/lib64/R/library/sass/tests/testthat/test-unicode.R
/usr/lib64/R/library/sass/tests/testthat/test-utils.R
/usr/lib64/R/library/sass/tests/testthat/test-variables.R
/usr/lib64/R/library/sass/tests/testthat/test-variables.scss

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sass/libs/sass.so
/usr/lib64/R/library/sass/libs/sass.so.avx2
/usr/lib64/R/library/sass/libs/sass.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-sass/4d640cc322117dec7f97632e6ed4319131a16ad2
/usr/share/package-licenses/R-sass/dc6b6d4b9ae804ab0dd95d46d148ee533bec260f
