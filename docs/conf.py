
import os

suppress_warnings = ['toc.secnum']
source_suffix = '.rst'
# Ignore included files in root and in child folders from being reported
# as not part of the toctree.
exclude_patterns = ['**.include.rst', '**/*.include.rst']
master_doc = 'index'
pygments_style = 'sphinx'
smartquotes = False
html4_writer = False

html_static_path = ['_static']
html_extra_path = ['versions.js']
html_theme = 'integrated_v2'


_docs_dir = os.path.dirname(os.path.abspath(__file__))
_repo_root = os.path.abspath(os.path.join(_docs_dir, ".."))
_theme_dir = os.path.join(_repo_root, "sphinx")

html_theme_path = [_theme_dir]
templates_path = [_theme_dir]

html_theme_options = {
  "accent_color": "sky",
  "show_ai_links": False,
}

project = "SFTPPlus"
copyright = "ProAtria Team"

version = "5.26.4"
release = "5.26.4"

primary_domain = 'py'

pdf_documents = [(
    'index',
    'SFTPPlus-5.26.4',
    'SFTPPlus Documentation',
    'ProAtria Team',
    )]
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
pdf_use_toc = False
pdf_toc_depth = 2

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
    'sphinx_design',
    ]

html_context = {
"wip_redirect": "",
"robots": "noindex, nofollow",
"canonical_site": "https://www.sftpplus.com/documentation/sftpplus/latest/",
"source_type": "github",
"source_user": "sftpplus",
"source_repo": "sftpplus-docs",
"source_version": "main",
"source_docs_path": "/src/doc_source/",
}
