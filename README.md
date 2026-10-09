# paboto.com: how to edit the site

Everything on paboto.com lives in this repository. When you save (commit) a change here,
the site updates by itself in about a minute.

## Which file is which page

| Page on the site | File to edit |
|---|---|
| The film you land on | `index.html` |
| Work (your sentence and the photo tiles) | `work.html` |
| Projects (the text and photos for each project) | `projects.html` |
| Photography | `photography.html` |
| About | `about.html` |
| Prices | `prices.html` |
| Contact | `contact.html` |
| All photos | the `images` folder |

You never need to touch `assets` (the look of the site) or `video`.

## Change some text

1. Click the file, e.g. `about.html`.
2. Click the pencil ✏️ at the top right of the file.
3. Change only the words **between** the tags. In `<p>Hi, I'm Steph.</p>` you change `Hi, I'm Steph.` and leave `<p>` and `</p>` alone.
4. Click the green **Commit changes…** button, then **Commit changes** again.
5. Wait a minute and refresh paboto.com.

Look for the lines that start with `<!-- ✏️` in the files. They explain each part in plain words.

## Add or swap a photo

1. Make the photo web-sized first: about 1400–2000 px on the long side, under 500 KB.
   [squoosh.app](https://squoosh.app) does it for free.
2. Give it a simple name: lowercase letters, numbers and hyphens, no spaces or æ ø å.
   For example `strangas-boxes.jpg`.
3. Open the `images` folder, click **Add file → Upload files**, drag the photo in, then **Commit changes**.
4. Open the page file and change the old file name after `images/` to the new one.
   Also update the `alt="…"` text: a short description of the photo, good for Google.

## Move a tile on the Work page

In `work.html`, each tile is one line that starts with `<a class="tile"`.
Cut a whole line and paste it higher or lower. The order of the lines is the order on the page.

## Add a new project

1. In `projects.html`, copy a whole block from `<article` to `</article>` and paste it where you want it.
2. Give it a new `id="…"` (for example `id="strangas"`) and change the words and photos.
3. In `work.html`, copy a tile line and point it to `projects.html#strangas`.

## Made a mistake?

Open the file, click **History**, open the version before your change and copy it back.
Or just tell Claude what happened. Nothing you do here can break anything that can't be undone.
