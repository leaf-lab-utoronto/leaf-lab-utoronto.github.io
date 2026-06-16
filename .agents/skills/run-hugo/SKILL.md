---
description: Launch the Hugo dev server for the LEAF Lab website
triggers:
  - run the website
  - serve the website
  - start hugo
  - hugo server
---

# Run Hugo dev server

Start the Hugo dev server on port 1313 in the background, then verify it's up.

```bash
hugo server --port 1313 --bind 127.0.0.1 &
```

Wait ~3 seconds for startup, then confirm with:

```bash
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:1313/
```

A `200` response means the server is ready. Tell the user the site is available at **http://localhost:1313** and that Hugo will live-reload on file saves.

If port 1313 is already in use (exit code non-zero or connection refused), check for an existing Hugo process:

```bash
lsof -i :1313 | grep hugo
```

If one is already running, just report the URL without starting a new instance.
