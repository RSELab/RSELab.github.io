# Adding or updating your profile

Each current member is a single Markdown file in [`_members/`](../_members) plus a photo in [`images/team/`](../images/team). That file is your card on the [Team page](https://rselab.github.io/team/).

## Quick version (all in the browser)

1. Open [`_members/`](../_members) on GitHub.
   - **New member:** click **Add file → Create new file** and name it `firstname-lastname.md`.
   - **Updating:** open your file and click the pencil icon.
2. Fill it in using the template below.
3. Upload your photo: go to [`images/team/`](../images/team), click **Add file → Upload files**, and name it to match, e.g. `firstname-lastname.jpg`.
4. Choose **Create a new branch and start a pull request**. When you aren't a member of the RSELab org, GitHub offers to fork the repo for you instead, which works just as well.
5. A bot comments on the pull request with a preview link. Check your card there, then ask a site admin to merge.

## The template

```markdown
---
name: Ada Lovelace
lastname: lovelace
image: images/team/ada-lovelace.jpg
role: PhD Student
research: Robot learning, manipulation, 3D perception
links:
  home-page: https://ada.example.com
  google-scholar: AbCdEfGhIjK
  github: adalovelace
  twitter: adalovelace
---

Optional longer bio in Markdown. It appears on your own page at
https://rselab.github.io/members/ada-lovelace/. Your card on the Team page links there.
```

### Fields

| Field | Required | Notes |
| --- | --- | --- |
| `name` | yes | Your name as it should appear on your card. |
| `lastname` | yes | Lowercase. Cards within a group are sorted by this field. |
| `image` | yes | Path to your photo. If it's missing or wrong, a placeholder image is shown. |
| `role` | yes | Use one of the values below. This decides which section of the Team page you appear in. |
| `research` | recommended | A short line of interests. Keep it to about three topics so it fits on the card. |
| `links` | optional | Your link icons. See the list below. |
| `aliases` | optional | Every name you publish under, including your site name, e.g. `[Helen Wang, Yi Ru Wang]`. The "See your papers" link on your page searches for all of them. |

### Role

The Team page sorts people into sections by `role`, so spelling and capitalization matter:

| `role:` | Shows up under |
| --- | --- |
| `Faculty` | Faculty, Postdocs, and PhD Students (listed first) |
| `Postdoc` | Faculty, Postdocs, and PhD Students (after faculty) |
| `PhD Student` | Faculty, Postdocs, and PhD Students (after postdocs). Any other value, e.g. `Research Scientist` or `MS Student`, also lands here. |
| `Undergrad` | Undergrad Students |

### Links

Each key becomes an icon on your card. Most keys take just your **handle or ID**, and the site builds the full URL:

| Key | Value to put | Example |
| --- | --- | --- |
| `home-page` | full URL | `https://ada.example.com` |
| `google-scholar` | the `user=` part of your Scholar URL | `AbCdEfGhIjK` |
| `github` | username | `adalovelace` |
| `twitter` | handle, without `@` | `adalovelace` |
| `bluesky` | handle | `ada.bsky.social` |
| `linkedin` | full URL | `https://www.linkedin.com/in/ada-lovelace` |
| `orcid` | ORCID iD | `0000-0002-1825-0097` |
| `email` | address | `ada@cs.washington.edu` |

Leave out any links you don't want. The full list of supported keys is in [`_data/types.yaml`](../_data/types.yaml).

## Your photo

- Use a square crop with your face centered. Cards crop the photo to a circle.
- Around 600×600 px is plenty. Keep the file under about 500 KB, because large photos slow the page down.
- `.jpg` is preferred. Name it to match your member file, e.g. `ada-lovelace.jpg`.
- The filename is case-sensitive: `Ada-Lovelace.JPG` and `ada-lovelace.jpg` are different files on the live site.

## Leaving the lab

When you graduate or move on, a single pull request should do both of these:

1. **Delete** your file from `_members/`. Your photo can stay in `images/team/`.
2. **Add yourself** to the top of [`_data/alumni.yaml`](../_data/alumni.yaml):

   ```yaml
   - name: Ada Lovelace
     degree: PhD
     year: "2026"
     now: Research Scientist at Analytical Engines Inc.
   ```

   `degree` must be one of `PhD`, `Postdoc`, `MS` or `Undergrad`, and it decides which table you appear in. PhD and Postdoc alumni share one table, and MS and Undergrad alumni share the other. `now` is optional. Quote the year so YAML keeps it as text.

Your papers stay on the Publications page after you leave, because alumni still count as lab coauthors. For details, see [publications.md](publications.md).

## Lab outing photos

To add a photo to the scrolling band at the top of the Team page, upload it to [`images/outings/`](../images/outings). Nothing else is needed, because every image in that folder is picked up automatically. Use landscape photos about 1200 px wide.
