# paboto.com: how to edit the site

Everything on paboto.com lives here. When you save (commit) a change, the site updates by itself in about a minute.

Easiest of all: tell Claude what you want changed, and it's done for you.

## Which file is which page

| On the site | File |
|---|---|
| The film you land on | `index.html` |
| Work: your sentence and the photo tiles | `work.html` |
| One page per project | the `work` folder, e.g. `work/boulebar.html` |
| Photography | `photography.html` |
| About | `about.html` |
| Contact | `contact.html` |
| All photos | the `images` folder |

You never need to touch `assets` (the look of the site) or `video`.

## Change some text

1. Click the file, e.g. `about.html`.
2. Click the pencil ✏️ at the top right.
3. Change only the words **between** the tags. In `<p>Hi, I'm Steph.</p>` you change `Hi, I'm Steph.` and leave `<p>` and `</p>` alone.
4. Click the green **Commit changes…** button, then **Commit changes** again.
5. Wait a minute and refresh paboto.com.

The lines that start with `<!-- ✏️` explain each part in plain words.

## Add or swap a photo

1. Make the photo web-sized first: about 1400–2000 px on the long side, under 500 KB. [squoosh.app](https://squoosh.app) does it for free.
2. Give it a simple name: lowercase letters, numbers and hyphens, no spaces or æ ø å. For example `strangas-boxes.jpg`.
3. Open the `images` folder, click **Add file → Upload files**, drag the photo in, then **Commit changes**.
4. In the page file, change the old file name after `/images/` to the new one, and update `alt="…"`: a short description of the photo, good for Google.

## Move a tile on the Work page

In `work.html`, each tile is one line starting with `<a class="tile"`. Cut a whole line and paste it higher or lower.

## Add a new project

1. Open the `work` folder, open a project (e.g. `boulebar.html`), copy everything in it.
2. Click **Add file → Create new file**, name it e.g. `strangas.html`, paste, and change the words and photos.
3. In `work.html`, copy a tile line, paste it, and change the link to `/work/strangas`, the photo and the words.

## The hidden prices page

`prices.html` is hidden for now: anyone who goes to paboto.com/prices is sent to Contact. To show it again:

1. In `vercel.json`, delete the whole line with `"/prices"`.
2. Add `<a href="/prices" data-page="prices">Prices</a>` to the menu at the top of every page.

## Made a mistake?

Open the file, click **History**, and copy back the version from before your change. Or just tell Claude. Nothing here can break in a way that can't be undone.
