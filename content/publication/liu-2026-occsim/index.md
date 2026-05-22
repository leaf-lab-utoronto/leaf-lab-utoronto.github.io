---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models'
authors:
- Tianran Liu
- Shengwen Zhao
- Mozhgan Pourkeshavarz
- Weican Li
- Nicholas Rhinehart
tags: ["autonomous driving", "computer vision", "forecasting", "generative models", "machine learning", "robotics"]
date: '2026-03-30'
lastmod: 2026-03-30
publishDate: '2026-03-30'
url_pdf: https://arxiv.org/pdf/2603.28887
url_doi: https://doi.org/10.48550/arXiv.2603.28887
url_project: https://orbis36.github.io/OccSim/
publication: '*arXiv:2603.28887*'
publication_short: '**arXiv**'
publication_types:
- 'preprint'

abstract: >-
  Data-driven autonomous driving simulation has long been constrained by its heavy
  reliance on pre-recorded driving logs or spatial priors, such as HD maps. This
  fundamental dependency severely limits scalability, restricting open-ended generation
  capabilities to the finite scale of existing collected datasets. To break this
  bottleneck, we present OccSim, the first occupancy world model-driven 3D simulator.
  OccSim obviates the requirement for continuous logs or HD maps; conditioned only on a
  single initial frame and a sequence of future ego-actions, it can stably generate over
  3,000 continuous frames, enabling the continuous construction of large-scale 3D
  occupancy maps spanning over 4 kilometers for simulation. This represents an >80x
  improvement in stable generation length over previous state-of-the-art occupancy world
  models. OccSim is powered by two modules: W-DiT based static occupancy world model and
  the Layout Generator. W-DiT handles the ultra-long-horizon generation of static
  environments by explicitly introducing known rigid transformations in architecture
  design, while the Layout Generator populates the dynamic foreground with reactive agents
  based on the synthesized road topology. With these designs, OccSim can synthesize
  massive, diverse simulation streams. Extensive experiments demonstrate its downstream
  utility: data collected directly from OccSim can pre-train 4D semantic occupancy
  forecasting models to achieve up to 67% zero-shot performance on unseen data,
  outperforming previous asset-based simulator by 11%. When scaling the OccSim dataset to
  5x the size, the zero-shot performance increases to about 74%, while the improvement
  over asset-based simulators expands to 22.1%.
categories: []
subtitle: ''
summary: ''
featured: false
draft: false
result_media:
  src: result-candidates/occsim-snippet.mp4
  type: video
  alt: OccSim occupancy world model simulation result animation

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
  url: 'https://openalex.org/W7146954426'
  updated: '2026-04-02T13:53:19.096889'
  title: 'OccSim: Multi-kilometer Simulation with Long-horizon Occupancy World Models'
---
