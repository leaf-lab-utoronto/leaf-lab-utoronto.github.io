---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Directed-Info GAIL: Learning Hierarchical Policies from Unsegmented Demonstrations using Directed Information'
subtitle: ''
summary: ''
authors:
- Arjun Sharma
- Mohit Sharma
- Nicholas Rhinehart
- Kris M Kitani
tags: ["imitation learning", "robotics"]
categories: []
date: '2019-01-01'
lastmod: 2024-07-15T15:34:46-04:00
featured: false
draft: false
result_media:
  src: result-candidates/digail-snippet.mp4
  type: video
  alt: Directed-Info GAIL hierarchical policy result animation

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
publishDate: '2024-07-15T19:34:46.577992Z'
publication_types:
- 'paper-conference'
abstract: >-
  The use of imitation learning to learn a single policy for a complex task that has
  multiple modes or hierarchical structure can be challenging. In fact, previous work has
  shown that when the modes are known, learning separate policies for each mode or
  sub-task can greatly improve the performance of imitation learning. In this work, we
  discover the interaction between sub-tasks from their resulting state-action trajectory
  sequences using a directed graphical model. We propose a new algorithm based on the
  generative adversarial imitation learning framework which automatically learns sub-task
  policies from unsegmented demonstrations. Our approach maximizes the directed
  information flow in the graphical model between sub-task latent variables and their
  generated trajectories. We also show how our approach connects with the existing Options
  framework, which is commonly used to learn hierarchical policies.
publication: '*International Conference on Learning Representations (ICLR)*'
publication_short: '**ICLR**'
url_pdf: https://arxiv.org/pdf/1810.01266
url_doi: https://doi.org/10.48550/arXiv.1810.01266
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2895192407'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Directed-Info GAIL: Learning Hierarchical Policies from Unsegmented Demonstrations using Directed Information'
---
