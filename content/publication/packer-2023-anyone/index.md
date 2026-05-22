---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Is anyone there? learning a planner contingent on perceptual uncertainty
subtitle: ''
summary: ''
authors:
- Charles Packer
- Nicholas Rhinehart
- Rowan McAllister
- Matthew A Wright
- Xin Wang
- Jeff He
- Sergey Levine
- Joseph E Gonzalez
tags: ["autonomous driving", "computer vision", "forecasting", "generative models", "machine learning", "model-based control", "robotics"]
categories: []
date: '2023-01-01'
lastmod: 2024-07-15T15:34:55-04:00
featured: false
draft: false
result_media:
  src: result-candidates/avp-snippet.mp4
  type: video
  alt: Active visual planning perceptual uncertainty result animation

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
publishDate: '2024-07-15T19:34:55.501580Z'
publication_types:
- 'paper-conference'
abstract: >-
  Robots in complex multi-agent environments should reason about the intentions of
  observed and currently unobserved agents. In this paper, we present a new learning-based
  method for prediction and planning in complex multi-agent environments where the states
  of the other agents are partially-observed. Our approach, Active Visual Planning (AVP),
  uses high-dimensional observations to learn a flow-based generative model of multi-agent
  joint trajectories, including unobserved agents that may be revealed in the near future,
  depending on the robot's actions. Our predictive model is implemented using deep neural
  networks that map raw observations to future detection and pose trajectories and is
  learned entirely offline using a dataset of recorded observations (not ground-truth
  states). Once learned, our predictive model can be used for contingency planning over
  the potential existence, intentions, and positions of unobserved agents. We demonstrate
  the effectiveness of AVP on a set of autonomous driving environments inspired by
  real-world scenarios that require reasoning about the existence of other unobserved
  agents for safe and efficient driving. In these environments, AVP achieves optimal
  closed-loop performance, while methods that do not reason about potential unobserved
  agents exhibit either overconfident or underconfident behavior.
publication: '*Conference on Robot Learning*'
publication_short: '**CoRL**'
url_pdf: https://proceedings.mlr.press/v205/packer23a/packer23a.pdf
url_doi: https://openreview.net/forum?id=2CSj965d9O4
paper_versions:
- retrieved_at: '2026-05-22T01:17:27+00:00'
  source: 'openreview'
  url: 'https://openreview.net/forum?id=2CSj965d9O4'
  updated: '1683308420103'
  title: 'Is Anyone There? Learning a Planner Contingent on Perceptual Uncertainty'
---
