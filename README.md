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

Horse listings are defined in the `HORSES`, `SOLD`, and `COMING` arrays in the same file. Add photo paths to the `photos` array on each horse for sale.

## Deploy to Vercel

This project is deployed on [Vercel](https://vercel.com) as **lrn_rquestrian**.

- **Production URL:** https://lrnrquestrian.vercel.app
- **Git integration:** pushes to `main` deploy to production; other branches get preview URLs.

No build step is required — Vercel serves `index.html` from the repository root.

To deploy manually from the CLI:

```bash
npx vercel --prod
```
