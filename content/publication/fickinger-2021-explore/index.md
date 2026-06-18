---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Explore and control with adversarial surprise
subtitle: ''
summary: ''
authors:
- Arnaud Fickinger
- Natasha Jaques
- Samyak Parajuli
- Michael Chang
- Nicholas Rhinehart
- Glen Berseth
- Stuart Russell
- Sergey Levine
tags: ["reinforcement learning", "autonomous exploration", "intrinsic control", "machine learning"]
categories: ["intrinsic control", "machine learning", "reinforcement learning"]
date: '2021-01-01'
lastmod: 2024-07-15T15:34:53-04:00
featured: false
draft: false
result_media:
  src: result-candidates/as.gif
  type: image
  alt: Adversarial surprise exploration result animation

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
publishDate: '2024-07-15T19:34:53.532117Z'
publication_types:
- 'preprint'
abstract: >-
  Unsupervised reinforcement learning (RL) studies how to leverage environment statistics
  to learn useful behaviors without the cost of reward engineering. However, a central
  challenge in unsupervised RL is to extract behaviors that meaningfully affect the world
  and cover the range of possible outcomes, without getting distracted by inherently
  unpredictable, uncontrollable, and stochastic elements in the environment. To this end,
  we propose an unsupervised RL method designed for high-dimensional, stochastic
  environments based on an adversarial game between two policies (which we call Explore
  and Control) controlling a single body and competing over the amount of observation
  entropy the agent experiences. The Explore agent seeks out states that maximally
  surprise the Control agent, which in turn aims to minimize surprise, and thereby
  manipulate the environment to return to familiar and predictable states. The competition
  between these two policies drives them to seek out increasingly surprising parts of the
  environment while learning to gain mastery over them. We show formally that the
  resulting algorithm maximizes coverage of the underlying state in block MDPs with
  stochastic observations, providing theoretical backing to our hypothesis that this
  procedure avoids uncontrollable and stochastic distractions. Our experiments further
  demonstrate that Adversarial Surprise leads to the emergence of complex and meaningful
  skills, and outperforms state-of-the-art unsupervised reinforcement learning methods in
  terms of both exploration and zero-shot transfer to downstream tasks.
publication: '*arXiv preprint arXiv:2107.07394*'
url_pdf: https://arxiv.org/pdf/2107.07394 
url_doi: https://doi.org/10.48550/arXiv.2107.07394
url_project: https://sites.google.com/view/adversarialsurprise/home
url_code: https://github.com/ArnaudFickinger/adversarial-surprise
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3177658869'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Explore and Control with Adversarial Surprise'
---
