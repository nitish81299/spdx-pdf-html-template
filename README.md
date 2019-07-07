# spdx-pdf-template
This is a template for the SPDX specifications in the markdown format and will generate the PDF version as well as the HTML version of the specifications with cover-page, header, footer and the table of contents.

### Clone the spdx-spec repository

  * ``git clone https://github.com/spdx/spdx-spec.git``
    
    and
    
    get the template file from this repository.

### Next you need to install dependencies

  * Latex: 

    + Debian/Ubuntu: ``apt-get install texlive``

    + Windows: The "Basic MiKTeX Installer" is used to set up a standard TeX/LaTeX system and can be downloaded from [here.](https://miktex.org/download)

    + Mac : The current distribution is MacTeX-2019
      This distribution requires Mac OS 10.12, Sierra, or higher and runs on Intel processors and can be downloaded from [here.](http://www.tug.org/mactex/mactex-download.html) 



  * Pandoc:

    + Windows: Just use pandoc installer for windows from [here.](https://github.com/jgm/pandoc/releases/download/2.7.2/pandoc-2.7.2-windows-x86_64.msi)

    + Mac:  You can install pandoc using Homebrew:

         `` brew install pandoc``

         To include pandoc’s citation parser:

         ``brew install pandoc-citeproc``    

    + Linux: 

         Download the binary package for amd64 architecuture from [here.](https://github.com/jgm/pandoc/releases/latest)

     + To install the deb:

         ``sudo dpkg -i $DEB``

         where $DEB is the path to the downloaded deb. This will install the pandoc and pandoc-citeproc executables and man pages.
      
         On any distro, you may install from the tarball into $DEST (say, /usr/local/ or $HOME/.local) by doing

         ``tar xvzf $TGZ --strip-components 1 -C $DEST``

         where $TGZ is the path to the downloaded zipped tarball. For Pandoc versions before 2.0, which don’t provide a tarball, try instead

         ``ar p $DEB data.tar.gz | tar xvz --strip-components 2 -C $DEST``



### Copy spdx-pdf-template in your latex templates folder and rename the file to .latex extension.
   Default location of the folder, if not present create one:

   * Unix, Linux, macOS: $XDG_DATA_HOME/pandoc/templates or ~/.pandoc/templates/

   * Windows Vista or later: C:\Users\USERNAME\AppData\Roaming\pandoc\templates

### To include titlepage, header footers you must provide the YAML metadata block at the very starting of the md file content    which you are going to convert.


```markdown---
---
title: "Software Package Data Exchange® (SPDX®) Specifications"
titlepage: true
titlepage-text-color: "123F66"
titlepage-rule-color: "213E4C"
titlepage-rule-height: 2
header-left: "Here comes header"
footer-left: "Here comes footer"
logo: "logo.pdf"
logo-width: 220
...
```

## Usage for PDF

  * When all the steps are done, run the following command:
   
    ``pandoc example.md -o example.pdf --from markdown --template spdx-pdf-template --table-of-contents --listings --pdf-engine=xelatex``

    OR
    
  * To make a single pdf of all the markdown files serially, run :

    ``pandoc index.md 1-rationale.md 2-document-creation-information.md 3-package-information.md 4-file-information.md 5-snippet-information.md 6-other-licensing-information-detected.md 7-relationships-between-SPDX-elements.md 8-annotations.md 9-review-information-deprecated.md appendix-I-SPDX-license-list.md appendix-II-license-matching-guidelines-and-templates.md appendix-III-RDF-data-model-implementation-and-identifier-syntax.md appendix-IV-SPDX-license-expressions.md appendix-V-using-SPDX-short-identifiers-in-source-files.md appendix-VI-external-repository-identifiers.md appendix-VII-creative-commons-attribution-license-3.0-unported.md -o example.pdf --from markdown --template spdx-pdf-template --table-of-contents --listings --pdf-engine=xelatex --file-scope``
    

## Usage for HTML

**NOTE**: Move the **spdx-html-template** into pandoc templates folder same as the latex template.

  * To generate the HTML run:

  ``pandoc -s index.md 1-rationale.md 2-document-creation-information.md 3-package-information.md 4-file-information.md 5-snippet-information.md 6-other-licensing-information-detected.md 7-relationships-between-SPDX-elements.md 8-annotations.md 9-review-information-deprecated.md appendix-I-SPDX-license-list.md appendix-II-license-matching-guidelines-and-templates.md appendix-III-RDF-data-model-implementation-and-identifier-syntax.md appendix-IV-SPDX-license-expressions.md appendix-V-using-SPDX-short-identifiers-in-source-files.md appendix-VI-external-repository-identifiers.md appendix-VII-creative-commons-attribution-license-3.0-unported.md -o example.html --from markdown --file-scope --toc --toc-depth=1 --template=spdx-html-template -H header.html -B footer.html``
