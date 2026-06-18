---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'SMiRL: Surprise Minimizing RL in Dynamic Environments'
subtitle: ''
summary: ''
authors:
- Glen Berseth
- Daniel Geng
- Coline Devin
- Nicholas Rhinehart
- Chelsea Finn
- Dinesh Jayaraman
- Sergey Levine
tags: ["reinforcement learning", "intrinsic control", "machine learning", "autonomous exploration"]
categories: []
date: '2019-01-01'
lastmod: 2024-07-15T15:34:49-04:00
featured: false
draft: false
result_media:
  src: result-candidates/smirl-doom-snippet.mp4
  type: video
  alt: SMiRL dynamic environment result animation

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
publishDate: '2024-07-15T19:34:49.494664Z'
publication_types:
- 'paper-conference'
abstract: >-
  Every living organism struggles against disruptive environmental forces to carve out and
  maintain an orderly niche. We propose that such a struggle to achieve and preserve order
  might offer a principle for the emergence of useful behaviors in artificial agents. We
  formalize this idea into an unsupervised reinforcement learning method called surprise
  minimizing reinforcement learning (SMiRL). SMiRL alternates between learning a density
  model to evaluate the surprise of a stimulus, and improving the policy to seek more
  predictable stimuli. The policy seeks out stable and repeatable situations that
  counteract the environment's prevailing sources of entropy. This might include avoiding
  other hostile agents, or finding a stable, balanced pose for a bipedal robot in the face
  of disturbance forces. We demonstrate that our surprise minimizing agents can
  successfully play Tetris, Doom, control a humanoid to avoid falls, and navigate to
  escape enemies in a maze without any task-specific reward supervision. We further show
  that SMiRL can be used together with standard task rewards to accelerate reward-driven
  learning.
url_pdf: https://openreview.net/pdf?id=cPZOyoDloxl
publication: '*International Conference on Representation Learning*'
publication_short: '**ICLR**'
url_doi: https://openreview.net/forum?id=cPZOyoDloxl
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2995912970'
  updated: '2025-10-10T17:16:08.811792'
  title: 'SMiRL: Surprise Minimizing RL in Dynamic Environments'
---
