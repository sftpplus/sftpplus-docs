

extensions = []
suppress_warnings = ['toc.secnum']
source_suffix = '.rst'
# Ignore included files in root and in child folders from being reported
# as not part of the toctree.
exclude_patterns = ['**.include.rst', '**/*.include.rst']
master_doc = 'index'
pygments_style = 'sphinx'
smartquotes = False
html4_writer = False
html_experimental_html5_writer = True
intersphinx_mapping = {}
templates_path = ['../templates']
html_static_path = ['_static']
html_theme_path = ['../templates']
html_theme = 'integrated'
project = "SFTPPlus"
copyright = "ProAtria Team"
version = "4.15.0"
release = "4.15.0"
autodoc_default_flags = ['members']
primary_domain = 'py'

pdf_documents = [(
    'index',
    u'SFTPPlus-4.16.0.dev0',
    u'SFTPPlus Documentation',
    u'ProAtria Team',
    )]
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
pdf_use_toc = False
pdf_toc_depth = 2
