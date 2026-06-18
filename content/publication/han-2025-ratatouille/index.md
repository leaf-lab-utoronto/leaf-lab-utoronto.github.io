---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Ratatouille: Imitation Learning Ingredients for Real-world Social Robot Navigation'
authors:
- James R. Han
- Mithun Vanniasinghe
- Hshmat Sahak
- Nicholas Rhinehart
- Timothy D. Barfoot
tags: ["machine learning", "robotics", "imitation learning", "social navigation"]
date: '2025-09-21'
lastmod: 2025-09-21
publishDate: '2025-09-21'
url_pdf: https://arxiv.org/pdf/2509.17204
publication: '*arXiv:2509.17204*'
publication_short: '**arXiv**'
url_doi: https://doi.org/10.48550/arXiv.2509.17204
publication_types:
- 'preprint'

abstract: >-
  Scaling Reinforcement Learning to in-the-wild social robot navigation is both
  data-intensive and unsafe, since policies must learn through direct interaction and
  inevitably encounter collisions. Offline Imitation learning (IL) avoids these risks by
  collecting expert demonstrations safely, training entirely offline, and deploying
  policies zero-shot. However, we find that naively applying Behaviour Cloning (BC) to
  social navigation is insufficient; achieving strong performance requires careful
  architectural and training choices. We present Ratatouille, a pipeline and model
  architecture that, without changing the data, reduces collisions per meter by 6 times
  and improves success rate by 3 times compared to naive BC. We validate our approach in
  both simulation and the real world, where we collected over 11 hours of data on a dense
  university campus. We further demonstrate qualitative results in a public food court.
  Our findings highlight that thoughtful IL design, rather than additional data, can
  substantially improve safety and reliability in real-world social navigation. Video:
  https://youtu.be/tOdLTXsaYLQ. Code will be released after acceptance.
categories: []
subtitle: ''
summary: ''
featured: false
draft: false
result_media:
  src: result-candidates/ratatouille-opening-snippet.mp4
  type: video
  alt: Ratatouille social robot navigation result animation

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W4416257357'
  updated: '2026-04-17T18:11:37.981687'
  title: 'Ratatouille: Imitation Learning Ingredients for Real-world Social Robot Navigation'
---
