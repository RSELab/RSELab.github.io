![on-push](../../actions/workflows/on-push.yaml/badge.svg)
![on-pull-request](../../actions/workflows/on-pull-request.yaml/badge.svg)
![on-schedule](../../actions/workflows/on-schedule.yaml/badge.svg)

# UW Robotics and State Estimation Lab website

The website of the Robotics and State Estimation Lab (RSE Lab) at the University of Washington, led by Dieter Fox.

Live site: **[rse-lab.cs.washington.edu](https://rse-lab.cs.washington.edu)**

It is a [Jekyll](https://jekyllrb.com) site built on Greene Lab's [Lab Website Template](https://github.com/greenelab/lab-website-template) ([template docs](https://greene-lab.gitbook.io/lab-website-template-docs)).

## For lab members

You don't need to install anything to update the site. You can edit files on GitHub and open a pull request.

- **[Add or update your profile](docs/profile.md):** your photo, role, research blurb and links, plus what to do when you join or leave the lab.
- **[Publications](docs/publications.md):** how papers get onto the site automatically, how to add a thumbnail, project page or description, and how to add or hide a paper.

Each pull request gets a preview build, and a bot comments with its link. Once the pull request is merged, the live site updates within a few minutes.

## Where things live

| Path | What it is |
| --- | --- |
| `_members/` | One file per current member. Each file is one card on the [Team](https://rselab.github.io/team/) page. |
| `images/team/` | Member photos |
| `images/outings/` | Photos for the scrolling band at the top of the Team page. Every image in this folder is shown automatically. |
| `_data/alumni.yaml` | The Alumni list on the Team page |
| `_data/openalex.yaml` | Settings for pulling publications from OpenAlex automatically |
| `_data/sources.yaml` | Papers added by hand, and extras for auto-pulled papers (thumbnails, descriptions, links, tags) |
| `_data/allowed_authors.yaml` | Extra names that count as lab coauthors when filtering auto-pulled papers |
| `_data/citations.yaml` | **Generated. Don't edit it.** The full citation list the Publications page is built from. |
| `_data/projects.yaml` | Entries on the Projects page |
| `_posts/` | Blog posts |
| `_cite/` | The Python citation pipeline (from the template, plus an OpenAlex plugin) |
| `team/`, `publications/`, `projects/`, `blog/`, `contact/`, `index.md` | The pages themselves |
| `_includes/`, `_layouts/`, `_styles/`, `_scripts/` | Templates, CSS and JS |

## How the site is built and deployed

Everything runs in GitHub Actions. Nobody builds the site by hand.

1. **Every push to `main`** runs `on-push`. It first runs `_cite/cite.py`, which reads `_data/openalex.yaml` and `_data/sources.yaml`, looks up full citation details, and commits the result to `_data/citations.yaml`. It then builds the site with Jekyll and pushes the output to the `gh-pages` branch.
2. **GitHub Pages** serves the `gh-pages` branch at https://rse-lab.cs.washington.edu/. The domain comes from the `CNAME` file in the repo root, which Jekyll copies into every build. Without it, each deploy would wipe the custom domain.
3. **Every Monday** `on-schedule` refreshes the citations, so new papers appear without anyone pushing.
4. **Pull requests** run `on-pull-request`, which builds a preview at `https://rse-lab.cs.washington.edu/preview/pr-<number>/`.

Because the citation step commits to `main`, the bot often has commits you don't. Run `git pull` before you push.

## Previewing locally (optional)

You need Ruby and Bundler, plus Python 3 if you want to regenerate citations:

```sh
bundle install
bundle exec jekyll serve      # http://localhost:4000

# optional: regenerate _data/citations.yaml the same way CI does
pip install -r _cite/requirements.txt
python _cite/cite.py
```

There's no need to commit a regenerated `citations.yaml`. CI regenerates it on every push anyway.

## Admin notes

- **Domain:** `rse-lab.cs.washington.edu` is a DNS CNAME to `rselab.github.io`, managed by UW CSE support (support@cs.washington.edu). The domain is verified for the RSELab org through a `_github-pages-challenge-RSELab` TXT record. Don't delete that record, because it stops anyone else's GitHub Pages site from claiming the domain.

- The repository is `RSELab/RSELab.github.io`. GitHub Pages is set to serve the **`gh-pages` branch**, not `main`. If someone switches it back to `main`, the live site breaks, because GitHub's default Jekyll build can't run this template's plugins.
- To change which papers are pulled automatically, edit `_data/openalex.yaml`. The comments at the top of that file list every option.
- To give a new member write access, add them to the RSELab GitHub organization. Members who aren't in the organization can still contribute through a fork and a pull request.
