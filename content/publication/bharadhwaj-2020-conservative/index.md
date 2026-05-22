---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Conservative safety critics for exploration
subtitle: ''
summary: ''
authors:
- Homanga Bharadhwaj
- Aviral Kumar
- Nicholas Rhinehart
- Sergey Levine
- Florian Shkurti
- Animesh Garg
tags: ["reinforcement learning", "autonomous exploration", "machine learning"]
categories: ["reinforcement learning", "machine learning", "autonomous exploration"]
date: '2020-01-01'
lastmod: 2024-07-15T15:34:51-04:00
featured: false
draft: false
result_media:
  src: result-candidates/csc.gif
  type: image
  alt: Conservative safety critics result animation

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
publishDate: '2024-07-15T19:34:51.043945Z'
publication_types:
- 'paper-conference'
abstract: >-
  Safe exploration presents a major challenge in reinforcement learning (RL): when active
  data collection requires deploying partially trained policies, we must ensure that these
  policies avoid catastrophically unsafe regions, while still enabling trial and error
  learning. In this paper, we target the problem of safe exploration in RL by learning a
  conservative safety estimate of environment states through a critic, and provably upper
  bound the likelihood of catastrophic failures at every training iteration. We
  theoretically characterize the tradeoff between safety and policy improvement, show that
  the safety constraints are likely to be satisfied with high probability during training,
  derive provable convergence guarantees for our approach, which is no worse
  asymptotically than standard RL, and demonstrate the efficacy of the proposed approach
  on a suite of challenging navigation, manipulation, and locomotion tasks. Empirically,
  we show that the proposed approach can achieve competitive task performance while
  incurring significantly lower catastrophic failure rates during training than prior
  methods. Videos are at this url
  https://sites.google.com/view/conservative-safety-critics/home
publication: '*International Conference on Represetation Learning*'
publication_short: '**ICLR**'
url_pdf: https://openreview.net/pdf?id=iaO86DUuKi
url_project: https://sites.google.com/view/conservative-safety-critics/home
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3096954237'
  updated: '2026-03-11T14:59:36.786465'
  title: 'Conservative Safety Critics for Exploration'
---
