# LRN Equestrian — Horse Sales Catalogue

Premium static website for [LRN Equestrian](https://www.instagram.com/lrn_equestrian): a curated catalogue of young and experienced showjumping horses for sale.

## Features

- Horse catalogue with grid and list views
- Jump level filter and age sorting
- Horse profile modals with timeline, highlights, and enquiry form
- Sold and Coming Soon sections
- Save favourites and compare horses (localStorage)
- Ask Our Expert contact panel
- X-ray / vetting request flow
- Mobile responsive layout
- LRN monochrome branding — no emojis, contact-based pricing only

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Configuration

Edit the `CONTACT` object at the top of the script in `index.html`:

```js
const CONTACT = {
  email: "lrnequestrian@gmail.com",
  whatsapp: "",  // optional — e.g. "40712345678"
  instagram: "https://www.instagram.com/lrn_equestrian",
};
```

Horse listings are defined in the `HORSES`, `SOLD`, and `COMING` arrays in the same file. Replace placeholder entries with real data and add photo URLs to the `photos` array on each horse.

## Deploy to Netlify

1. Push this repository to GitHub.
2. In [Netlify](https://www.netlify.com/), create a new site from the repo.
3. Build command: leave empty. Publish directory: `/` (repository root).
4. Deploy — `index.html` is served as the site entry point.

No build step required.
