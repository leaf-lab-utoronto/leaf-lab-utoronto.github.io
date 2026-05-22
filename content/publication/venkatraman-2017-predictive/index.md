---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Predictive-state decoders: Encoding the future into recurrent networks'
subtitle: ''
summary: ''
authors:
- Arun Venkatraman
- Nicholas Rhinehart
- Wen Sun
- Lerrel Pinto
- Martial Hebert
- Byron Boots
- Kris M. Kitani
- J. A. Bagnell
tags: ["imitation learning", "forecasting", "machine learning", "reinforcement learning"]
categories: []
date: '2017-01-01'
lastmod: 2024-07-15T15:34:45-04:00
featured: false
draft: false
author_notes:
- "Equal Contribution"
- "Equal Contribution"

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
publishDate: '2024-07-15T19:34:44.703937Z'
publication_types:
- 'paper-conference'
abstract: >-
  Recurrent neural networks (RNNs) are a vital modeling technique that rely on internal
  states learned indirectly by optimization of a supervised, unsupervised, or
  reinforcement training loss. RNNs are used to model dynamic processes that are
  characterized by underlying latent states whose form is often unknown, precluding its
  analytic representation inside an RNN. In the Predictive-State Representation (PSR)
  literature, latent state processes are modeled by an internal state representation that
  directly models the distribution of future observations, and most recent work in this
  area has relied on explicitly representing and targeting sufficient statistics of this
  probability distribution. We seek to combine the advantages of RNNs and PSRs by
  augmenting existing state-of-the-art recurrent neural networks with Predictive-State
  Decoders (PSDs), which add supervision to the network's internal state representation to
  target predicting future observations. Predictive-State Decoders are simple to implement
  and easily incorporated into existing training pipelines via additional loss
  regularization. We demonstrate the effectiveness of PSDs with experimental results in
  three different domains: probabilistic filtering, Imitation Learning, and Reinforcement
  Learning. In each, our method improves statistical performance of state-of-the-art
  recurrent baselines and does so with fewer iterations and less data.
publication: '*Advances in Neural Information Processing Systems*'
publication_short: '**NeurIPS**'
url_pdf: https://proceedings.neurips.cc/paper_files/paper/2017/file/61b4a64be663682e8cb037d9719ad8cd-Paper.pdf
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2750941309'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Predictive-State Decoders: Encoding the Future into Recurrent Networks'
---
