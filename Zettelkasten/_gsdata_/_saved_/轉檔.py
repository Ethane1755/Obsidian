import os
def auto_md_to_docx(file_dir):
    all_whole_path_files = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            try:
                if file[-3:] == ".md":
                    file_info = [root+'/', file]
                    all_whole_path_files.append(file_info)
            except Exception as e:
                print(e)
    print("==>", all_whole_path_files)

    for file_info in all_whole_path_files:
        md_file_path_file = file_info[0] + file_info[1]
        docx_file_name = file_info[1][:-3] + '.html' # <- 改變最後一個變數就可以轉檔
        docx_file_path_file = file_info[0] + docx_file_name
        new_command = 'pandoc ' + md_file_path_file + ' -o ' + docx_file_path_file

        try:
            result = os.popen(new_command).readlines()
            if len(result) == 0:
                print(md_file_path_file, "已轉換成", docx_file_path_file)
        except Exception as e:
            print(e)

def main():
    auto_md_to_docx('.')

if __name__ == '__main__':
    main()

# 支援的轉檔格式
# asciidoc (AsciiDoc) or asciidoctor (AsciiDoctor)
# beamer (LaTeX beamer slide show)
# bibtex (BibTeX bibliography)
# biblatex (BibLaTeX bibliography)
# commonmark (CommonMark Markdown)
# commonmark_x (CommonMark Markdown with extensions)
# context (ConTeXt)
# csljson (CSL JSON bibliography)
# docbook or docbook4 (DocBook 4)
# docbook5 (DocBook 5)
# docx (Word docx)
# dokuwiki (DokuWiki markup)
# epub or epub3 (EPUB v3 book)
# epub2 (EPUB v2)
# fb2 (FictionBook2 e-book)
# gfm (GitHub-Flavored Markdown), or the deprecated and less accurate markdown_github; use markdown_github only if you need extensions not supported in gfm.
# haddock (Haddock markup)
# html or html5 (HTML, i.e. HTML5/XHTML polyglot markup)
# html4 (XHTML 1.0 Transitional)
# icml (InDesign ICML)
# ipynb (Jupyter notebook)
# jats_archiving (JATS XML, Archiving and Interchange Tag Set)
# jats_articleauthoring (JATS XML, Article Authoring Tag Set)
# jats_publishing (JATS XML, Journal Publishing Tag Set)
# jats (alias for jats_archiving)
# jira (Jira/Confluence wiki markup)
# json (JSON version of native AST)
# latex (LaTeX)
# man (roff man)
# markdown (Pandoc’s Markdown)
# markdown_mmd (MultiMarkdown)
# markdown_phpextra (PHP Markdown Extra)
# markdown_strict (original unextended Markdown)
# mediawiki (MediaWiki markup)
# ms (roff ms)
# muse (Muse),
# native (native Haskell),
# odt (OpenOffice text document)
# opml (OPML)
# opendocument (OpenDocument)
# org (Emacs Org mode)
# pdf (PDF)
# plain (plain text),
# pptx (PowerPoint slide show)
# rst (reStructuredText)
# rtf (Rich Text Format)
# texinfo (GNU Texinfo)
# textile (Textile)
# slideous (Slideous HTML and JavaScript slide show)
# slidy (Slidy HTML and JavaScript slide show)
# dzslides (DZSlides HTML5 + JavaScript slide show),
# revealjs (reveal.js HTML5 + JavaScript slide show)
# s5 (S5 HTML and JavaScript slide show)
# tei (TEI Simple)
# xwiki (XWiki markup)
# zimwiki (ZimWiki markup)asciidoc (AsciiDoc) or asciidoctor (AsciiDoctor)
