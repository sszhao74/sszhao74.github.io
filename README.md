# KLIC Website
This is the project for KLIC Website. It is powered by Jekyll with [al-folio](https://github.com/alshedivat/al-folio) theme. 

## Table Of Contents

- [KLIC Website](#KLIC-Website)
  - [Getting Started](#Getting-Started)
  - [Global Setting](#Global-Setting)
  - [About Page](#About-Page)
  - [Activities Page](#Activities-Page)
  - [Blog Page](#Blog-Page)
  - [People Page](#People-Page)
  - [Publications Page](#Publications-Page)

 
## Getting Started
- Step 1: Read the guideline from [al-folio](https://github.com/alshedivat/al-folio)
- Step 2: Clone this project to your local development environment and configure Docker and other contents according to the guidelines in al-folio.
- Step 3: Run the project in the console according to the following commands. 

          $ docker compose up

- Step 4: Open `localhost:8080` in the browser.

## Global Setting
- [_config.yml](_config.yml) :global page setting
- [_bibliography/](_bibliography/):Directory storing references in BibTex format
- [_data/](_data/): Directory storing all data files
- [_includes/](_includes/): Directory for layout components
- [_layouts/](layouts/): Directory for common layouts
- [_pages/](_pages/): Directory for all pages
- [_posts/](_posts/): Directory for all posts in Blog Page
- [_scripts/](_scripts/): Directory containts the script files for fetching data
- [_assets/](_assets/): Directory contains various resource files
  - [_assets/css/main.scss](_assets/css/main.scss): This is the file for global style configuration
  - [_assets/img/](_assets/img/): Directory contains all image recources
 
## About Page
This is the homepage of KLIC website.

- [_layouts/about.liquid](_layouts/about.liquid): style configuration
  - [_includes/latest_activities.liquid](_includes/latest_activities.liquid): configuration for latest activities
  - [_includes/latest_posts.liquid](_includes/latest_posts.liquid): configuration for latest posts
  - [_includes/selected_papers.liquid](_includes/selected_papers.liquid): configuration for selected papers （Note: need to add the field "selected = {true}" for the selected publication in the paper.bib file.）

- [_pages/about.md](_pages/about.md):content configuration


## Activities Page
This is the page for presenting all KLIC Activities.

- [_includes/activity.liquid](_includes/activity.liquid): style configuration
- [_pages/activities.md](_pages/activities.md): content configuration
- [_data/activities.yml](_data/activities.yml): data file

## Blog Page
This is the page for presenting all KLIC posts.

- [_pages/activities.md](_pages/blog.md): content&style configuration
- [_posts](_posts/): all posts can be stored in this directory.

## People Page
This is the page for showing all faculty&student members.

- [_pages/people.md](_pages/people.md): content&style configuration
- [_data/faculty.yml](_data/faculty.yml): data file of all faculties
- [_data/students.yml](_data/students.yml): data file of all students

## Publications Page
This is the page for presenting the publications of all groups in the past five years.

- [_pages/publications.md](_pages/publications.md): content&style configuration
- [_scripts/request_dblp.py](_scripts/request_dblp.py): It is used to obtain the citation data in BibTeX format of the publications of all teachers in the past five years from DBLP. You can add DBLP links by yourself. Running this script will update the paper.bib file.
- [_bibliography/paper.bib](_bibliography/paper.bib): references in BibTex format



