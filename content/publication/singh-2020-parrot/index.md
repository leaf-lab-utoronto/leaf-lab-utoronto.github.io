---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Parrot: Data-driven behavioral priors for reinforcement learning'
subtitle: ''
summary: ''
authors:
- Avi Singh
- Huihan Liu
- Gaoyue Zhou
- Albert Yu
- Nicholas Rhinehart
- Sergey Levine
tags: ["generative models", "imitation learning", "machine learning", "robotics", "manipulation"]
categories: []
date: '2020-01-01'
lastmod: 2024-07-15T15:34:52-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false
result_media:
  src: result-candidates/parrot.gif
  type: image
  alt: Parrot robot manipulation result animation

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-07-15T19:34:51.850904Z'
publication_types:
- 'paper-conference'
abstract: >-
  Reinforcement learning provides a general framework for flexible decision making and
  control, but requires extensive data collection for each new task that an agent needs to
  learn. In other machine learning fields, such as natural language processing or computer
  vision, pre-training on large, previously collected datasets to bootstrap learning for
  new tasks has emerged as a powerful paradigm to reduce data requirements when learning a
  new task. In this paper, we ask the following question: how can we enable similarly
  useful pre-training for RL agents? We propose a method for pre-training behavioral
  priors that can capture complex input-output relationships observed in successful trials
  from a wide range of previously seen tasks, and we show how this learned prior can be
  used for rapidly learning new tasks without impeding the RL agent's ability to try out
  novel behaviors. We demonstrate the effectiveness of our approach in challenging robotic
  manipulation domains involving image observations and sparse reward functions, where our
  method outperforms prior works by a substantial margin.
publication: '*International Conference on Learning Representations*'
publication_short: '**ICLR**'
url_pdf: https://openreview.net/pdf?id=Ysuv-WOFeKR
url_project: https://sites.google.com/view/parrot-rl
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3103763075'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Parrot: Data-Driven Behavioral Priors for Reinforcement Learning'
---
