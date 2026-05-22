---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models'
authors:
- Mozhgan Pourkeshavarz
- Tianran Liu
- Nicholas Rhinehart
tags: ["autonomous driving", "computer vision", "forecasting", "machine learning", "robotics", "generative models"]
date: '2026-03-30'
lastmod: 2026-03-30
publishDate: '2026-03-30'
url_pdf: https://arxiv.org/pdf/2603.28963
url_doi: https://doi.org/10.48550/arXiv.2603.28963
publication: '*arXiv:2603.28963*'
publication_short: '**arXiv**'
publication_types:
- 'preprint'

abstract: >-
  Multi-agent traffic simulation is central to developing and testing autonomous driving
  systems. Recent data-driven simulators have achieved promising results, but rely heavily
  on supervised learning from labeled trajectories or semantic annotations, making it
  costly to scale their performance. Meanwhile, large amounts of unlabeled sensor data can
  be collected at scale but remain largely unused by existing traffic simulation
  frameworks. This raises a key question: How can a method harness unlabeled data to
  improve traffic simulation performance? In this work, we propose AutoWorld, a traffic
  simulation framework that employs a world model learned from unlabeled occupancy
  representations of LiDAR data. Given world model samples, AutoWorld constructs a
  coarse-to-fine predictive scene context as input to a multi-agent motion generation
  model. To promote sample diversity, AutoWorld uses a cascaded Determinantal Point
  Process framework to guide the sampling processes of both the world model and the motion
  model. Furthermore, we designed a motion-aware latent supervision objective that
  enhances AutoWorld's representation of scene dynamics. Experiments on the WOSAC
  benchmark show that AutoWorld ranks first on the leaderboard according to the primary
  Realism Meta Metric (RMM). We further show that simulation performance consistently
  improves with the inclusion of unlabeled LiDAR data, and study the efficacy of each
  component with ablations. Our method paves the way for scaling traffic simulation
  realism without additional labeling. Our project page contains additional visualizations
  and released code.
categories: []
subtitle: ''
summary: ''
featured: false
draft: false
result_media:
  src: result-candidates/autoworld-snippet.mp4
  type: video
  alt: AutoWorld multi-agent traffic simulation result animation

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
  url: 'https://openalex.org/W7147413225'
  updated: '2026-04-02T13:53:19.096889'
  title: 'AutoWorld: Scaling Multi-Agent Traffic Simulation with Self-Supervised World Models'
---
