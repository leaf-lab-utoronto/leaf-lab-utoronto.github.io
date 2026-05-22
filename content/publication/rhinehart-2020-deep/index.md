---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Deep Imitative Models for Flexible Inference, Planning, and Control
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Rowan McAllister
- Sergey Levine
tags: ["autonomous driving", "computer vision", "forecasting", "generative models", "imitation learning", "model-based control", "reward learning"]
categories: []
date: '2020-01-01'
lastmod: 2024-07-15T15:34:51-04:00
featured: false
draft: false
result_media:
  src: result-candidates/deep-im-snippet.mp4
  type: video
  alt: Deep imitative model planning result animation

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
publishDate: '2024-07-15T19:34:50.516033Z'
publication_types:
- 'paper-conference'
abstract: >-
  Imitation Learning (IL) is an appealing approach to learn desirable autonomous behavior.
  However, directing IL to achieve arbitrary goals is difficult. In contrast,
  planning-based algorithms use dynamics models and reward functions to achieve goals.
  Yet, reward functions that evoke desirable behavior are often difficult to specify. In
  this paper, we propose Imitative Models to combine the benefits of IL and goal-directed
  planning. Imitative Models are probabilistic predictive models of desirable behavior
  able to plan interpretable expert-like trajectories to achieve specified goals. We
  derive families of flexible goal objectives, including constrained goal regions,
  unconstrained goal sets, and energy-based goals. We show that our method can use these
  objectives to successfully direct behavior. Our method substantially outperforms six IL
  approaches and a planning-based approach in a dynamic simulated autonomous driving task,
  and is efficiently learned from expert demonstrations without online data collection. We
  also show our approach is robust to poorly specified goals, such as goals on the wrong
  side of the road.
publication: '*International Conference on Learning Representations*'
publication_short: '**ICLR**'
url_pdf: https://openreview.net/pdf?id=Skl4mRNYDr
url_project: https://sites.google.com/view/imitative-models
url_doi: https://openreview.net/forum?id=Skl4mRNYDr
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2896583015'
  updated: '2025-11-06T06:51:31.235846'
  title: 'Deep Imitative Models for Flexible Inference, Planning, and Control'
---
