# Publications

The [Publications page](https://rselab.github.io/publications/) is generated. Most papers appear on it **automatically**, and you edit a YAML file only to add a paper, decorate one, or hide one.

> **Never edit `_data/citations.yaml`.** It's regenerated on every push, so any change you make there gets overwritten.

## How papers get on the site

A bot runs [`_cite/cite.py`](../_cite/cite.py) **on every push to `main`** and **every Monday**. It gathers papers from two places:

1. **Automatically from [OpenAlex](https://openalex.org)**, using the settings in [`_data/openalex.yaml`](../_data/openalex.yaml). A paper is pulled in when all of these are true:
   - Dieter Fox is an author.
   - At least one **other** author is a lab name, meaning a current member (`_members/`), an alum (`_data/alumni.yaml`), or someone listed in `_data/allowed_authors.yaml`.
   - It was published in **2024 or later**.
   - It's a paper, preprint, article or chapter, not a dataset, editorial or abstract.
   - When both an arXiv preprint and a published version exist, only the published version is kept.
2. **By hand from [`_data/sources.yaml`](../_data/sources.yaml)**: anything listed there by ID.

The bot looks up full citation details for each paper and writes them to `_data/citations.yaml`, and the page is built from that file.

OpenAlex usually indexes a new arXiv paper within a few days to a couple of weeks. If your paper isn't showing up yet, see the troubleshooting section below.

## Adding extras to your paper (thumbnail, description, project page)

Add an entry to `_data/sources.yaml` with the **same ID** as the paper. If the bot also pulls the paper from OpenAlex, the two entries are merged, and your fields take priority.

```yaml
- id: doi:10.48550/arXiv.2502.05485
  image: images/papers/hamster.png
  description: One or two sentences on what the paper does and why it matters.
  buttons:
    - type: website
      text: Project Page
      link: https://hamster-robot.github.io/
    - type: github
      text: Code
      link: https://github.com/your-org/your-repo
  tags:
    - vision language action
    - manipulation
```

| Field | Notes |
| --- | --- |
| `id` | Required. See the next section for formats. |
| `image` | Thumbnail. Upload it to `images/papers/` (create the folder the first time). Use a landscape image about 800 px wide and under about 300 KB. |
| `description` | A short summary shown under the citation. |
| `buttons` | Links shown as buttons. `type` picks the icon, e.g. `website` or `github`. All types are listed in [`_data/types.yaml`](../_data/types.yaml). |
| `tags` | Keywords people can search and filter on. Reuse existing tags where possible. |

## Finding the paper's ID

Use the paper's DOI with a `doi:` prefix:

| Paper | ID |
| --- | --- |
| arXiv preprint (`arxiv.org/abs/2502.05485`) | `doi:10.48550/arXiv.2502.05485` |
| Published paper with DOI `10.1109/iros60139.2025.11245882` | `doi:10.1109/iros60139.2025.11245882` |

Once a paper has been published, use the **published DOI**. That's the version the bot keeps, so an entry keyed on the arXiv DOI wouldn't merge with it. The publisher's page or [doi.org](https://doi.org) shows the DOI, and so does the paper's entry in `_data/citations.yaml` after the bot has run.

## Adding a paper the bot doesn't find

Examples include work without Dieter, papers from before 2024, or a paper OpenAlex hasn't indexed yet. Add the ID to `_data/sources.yaml`, with or without extras:

```yaml
- id: doi:10.48550/arXiv.2501.18564
```

The bot fills in the title, authors, venue and date.

## Hiding a paper

To hide a paper the bot pulled in that doesn't belong, such as unrelated work or a duplicate, add:

```yaml
- id: doi:10.1234/whatever
  remove: true
```

## Troubleshooting: "my paper is missing"

1. **Is Dieter Fox an author?** If not, add the paper by hand as described above.
2. **Do you publish under a different name than your profile shows?** For example, Helen Wang publishes as "Yi Ru Wang". Add your publishing name to [`_data/allowed_authors.yaml`](../_data/allowed_authors.yaml). Matching already handles case, middle initials, nicknames in parentheses and "Last, First" order, so only a genuinely different name needs an entry. Accented letters are the exception. The matcher drops them, so a name like "José Núñez" may not match reliably. If that applies to you, add your papers by hand.
3. **Are all the other lab authors missing from the site?** Coauthors who aren't members, alumni or listed in `allowed_authors.yaml` don't count. Add the long-term collaborators to `allowed_authors.yaml`.
4. **Is it brand new?** OpenAlex may not have indexed it yet. Add it by hand. Once OpenAlex picks it up, the two entries merge with no duplicate.
5. **Still stuck?** Open the latest run of the `on-push` workflow in the repository's **Actions** tab, and look at the `update-citations` step. Each source it processes is logged there, along with any lookup errors.

## How long until it's live?

The site updates about 3–5 minutes after your pull request is merged. The preview build on a pull request also regenerates citations, so you can check how your paper looks before merging.
