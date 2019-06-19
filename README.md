# spdx-pdf-template
This is a template for the spdx specifications in the markdown format and will generate cover-page, header, footer and the table of contents for the pdf version of the specifications.

### Clone the spdx-spec repository

  * ``git clone https://github.com/spdx/spdx-spec.git``
    
    and
    
    get the template file from this repository.

### Next you need to install dependencies

  * Latex: 

    + Debian/Ubuntu: ``apt-get install texlive``

    + Windows: The "Basic MiKTeX Installer" is used to set up a standard TeX/LaTeX system and can be downloaded from (https://miktex.org/download)

    + Mac : The current distribution is MacTeX-2019
      This distribution requires Mac OS 10.12, Sierra, or higher and runs on Intel processors and can be downloaded from (http://www.tug.org/mactex/mactex-download.html) 



  * Pandoc:

    + Windows: Just use pandoc installer for windows
     (https://github.com/jgm/pandoc/releases/download/2.7.2/pandoc-2.7.2-windows-x86_64.msi)

    + Mac:  You can install pandoc using Homebrew:

         `` brew install pandoc``

         To include pandoc’s citation parser:

         ``brew install pandoc-citeproc``    

    + Linux: 

         Download the binary package for amd64 architecuture from
          (https://github.com/jgm/pandoc/releases/latest)

     + To install the deb:

         ``sudo dpkg -i $DEB``

         where $DEB is the path to the downloaded deb. This will install the pandoc and pandoc-citeproc executables and man pages.
      
         On any distro, you may install from the tarball into $DEST (say, /usr/local/ or $HOME/.local) by doing

         ``tar xvzf $TGZ --strip-components 1 -C $DEST``

         where $TGZ is the path to the downloaded zipped tarball. For Pandoc versions before 2.0, which don’t provide a tarball, try instead

         ``ar p $DEB data.tar.gz | tar xvz --strip-components 2 -C $DEST``



### Copy spdx-latex-template in your latex templates folder and rename the file to .latex extension.
   Default location of the folder, if not present create one:

   * Unix, Linux, macOS: $XDG_DATA_HOME/pandoc/templates or ~/.pandoc/templates/

   * Windows XP: C:\Documents And Settings\USERNAME\Application Data\pandoc\templates

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

## Usage

  * When all the steps are done, run the following command:
   
    ``pandoc example.md -o example.pdf --from markdown --template spdx-pdf-template --table-of-contents --listings --pdf-engine=xelatex``

    OR
    
  * To make a single pdf of all the markdown files, run :

    ``pandoc *.md -o example.pdf --from markdown --template spdx-pdf-template --table-of-contents --listings --pdf-engine=xelatex``

