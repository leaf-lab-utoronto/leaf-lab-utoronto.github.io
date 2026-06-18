---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'N2N learning: Network to Network Compression via Policy Gradient Reinforcement
  Learning'
subtitle: ''
summary: ''
authors:
- Anubhav Ashok
- Nicholas Rhinehart
- Fares Beainy
- Kris M. Kitani
tags: ["compression", "machine learning", "reinforcement learning"]
categories: []
date: '2018-01-01'
lastmod: 2024-07-15T15:34:45-04:00
featured: false
draft: false

url_pdf: https://openreview.net/pdf?id=B1hcZZ-AW

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
publishDate: '2024-07-15T19:34:45.018581Z'
publication_types:
- 'paper-conference'
abstract: >-
  While bigger and deeper neural network architectures continue to advance the
  state-of-the-art for many computer vision tasks, real-world adoption of these networks
  is impeded by hardware and speed constraints. Conventional model compression methods
  attempt to address this problem by modifying the architecture manually or using
  pre-defined heuristics. Since the space of all reduced architectures is very large,
  modifying the architecture of a deep neural network in this way is a difficult task. In
  this paper, we tackle this issue by introducing a principled method for learning reduced
  network architectures in a data-driven way using reinforcement learning. Our approach
  takes a larger `teacher' network as input and outputs a compressed `student' network
  derived from the `teacher' network. In the first stage of our method, a recurrent policy
  network aggressively removes layers from the large `teacher' model. In the second stage,
  another recurrent policy network carefully reduces the size of each remaining layer. The
  resulting network is then evaluated to obtain a reward -- a score based on the accuracy
  and compression of the network. Our approach uses this reward signal with policy
  gradients to train the policies to find a locally optimal student network. Our
  experiments show that we can achieve compression rates of more than 10x for models such
  as ResNet-34 while maintaining similar performance to the input `teacher' network. We
  also present a valuable transfer learning result which shows that policies which are
  pre-trained on smaller `teacher' networks can be used to rapidly speed up training on
  larger `teacher' networks.
publication: '*International Conference on Learning Representations*'
publication_short: '**ICLR**'
url_doi: https://openreview.net/forum?id=B1hcZZ-AW
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2756085244'
  updated: '2026-02-09T09:26:11.010843'
  title: 'N2N Learning: Network to Network Compression via Policy Gradient Reinforcement Learning'
---
