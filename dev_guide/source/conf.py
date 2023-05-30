# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# !!!
# This file is generated out of template in doc-exports repository.
# Beware overwriting it locally.

import os
import sys

extensions = [
    'otcdocstheme',
]

otcdocs_auto_name = False
otcdocs_auto_version = False

project = 'Bare Metal Server'
otcdocs_repo_name = 'opentelekomcloud-docs/bare-metal-server'
# Those variables are required for edit/bug links

# Those variables are needed for indexing into OpenSearch
otcdocs_doc_environment = 'public'
otcdocs_doc_link = '/bare-metal-server/dev-guide/'
otcdocs_doc_title = 'Developer Guide'
otcdocs_doc_type = 'dev'
otcdocs_service_category = 'compute'
otcdocs_service_title = 'Bare Metal Server'
otcdocs_service_type = 'bms'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))

# -- General configuration ----------------------------------------------------
# https://docutils.sourceforge.io/docs/user/smartquotes.html - it does not
# what it is expected
smartquotes = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2022-present, Open Telekom Cloud'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
language = 'en'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
html_theme = 'otcdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme_options = {
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".

html_title = "Bare Metal Server - Developer Guide"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Do not include sources into the rendered results
html_copy_source = False

# -- Options for PDF output --------------------------------------------------
latex_documents = [
    ('index',
     'bms-dev-guide.tex',
     u'Bare Metal Server - Developer Guide',
     u'OpenTelekomCloud', 'manual'),
]
