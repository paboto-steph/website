# paboto.com: how to edit the site

Everything on paboto.com lives here. When you save (commit) a change, the site updates by itself in about a minute.

Easiest of all: tell Claude what you want changed, and it's done for you.

## Which file is which page

| On the site | File |
|---|---|
| Front page: the film and all the work | `index.html` |
| One page per project | the `work` folder, e.g. `work/boulebar.html` |
| Info: about you and contact | `info.html` |
| All photos | the `images` folder |
| The film | the `video` folder |

You never need to touch `assets` (the look of the site).

## Change some text

1. Click the file, e.g. `info.html`.
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

## Move a project on the front page

In `index.html`, each project is one line starting with `<a class="item"`. Cut a whole line and paste it higher or lower. The order of the lines is the order on the page.

## Add a new project

1. Open the `work` folder, open a project (e.g. `boulebar.html`) and copy everything in it.
2. In the `work` folder, click **Add file → Create new file**, name it e.g. `strangas.html`, paste, and change the words and photos.
3. In `index.html`, copy a project line, paste it, and change the link to `/work/strangas`, the photo and the caption.

## The hidden prices page

`prices.html` is hidden for now: anyone who goes to paboto.com/prices is sent to Info. To show it again:

1. In `vercel.json`, delete the whole line with `"/prices"`.
2. Add a link to `/prices` where you want it, for example in `info.html`.

## Made a mistake?

Open the file, click **History**, and copy back the version from before your change. Or just tell Claude. Nothing here can break in a way that can't be undone.
