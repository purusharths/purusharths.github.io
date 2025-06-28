## Personal Webpage
## (Workflow with Pelican + Obsidian)


## Setting up Pelican

1. Enable venv and install dependencies with `requirements.txt`

2. Install dependencies via `pip`. For interactive local development, also install `invoke`:
```
pip install -r requirements.txt
pip install invoke
```
3. Build the website:
```
python -m invoke livereload
```
This command will compile the site and open a browser window that dynamically updates as you edit
the content of your website.

4. Edit the content of your website. You can change `config.yml`, the contents of each page in the `pages` 
directory, blog posts in the `articles` directory, and add your list of publications in
`pages/publications.bib`.

5. To set up new post run `new_post.py`
6. To push changes run `push_changes.sh`. A github action takes over after the files are pushed (as shown below in `Using GitHub Actions`)

7. Using Makefile
```
make regenerate (to regenerate html outputs)
make serve (same as 3.)
make clean (clean html output)
```


## Setting up Obsidian 
1. Open `content` folder as vault.
2. Disable `Use [[Wikilinks]]`
3. In settings set up `default location for new attachments` as `In subfolder under current folder`.
Put subfolder name as `images`

Note: After adding any image, it would be required to append `images/` to the image path.


#### Debugging
Got a cryptic error message? Try running
```
python -m pelican --debug
```
which will build the website and prints log messages and a detailed stack trace for errors.

## Using Github Actions

```yml
# Simple workflow for deploying static content to GitHub Pages
name: Deploy static content to Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches: ["main"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Single deploy job since we're just deploying
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          # Upload entire repository
          path: 'output'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```





