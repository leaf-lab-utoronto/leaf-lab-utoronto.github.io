---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'S2Net: Stochastic Sequential Pointcloud Forecasting'
subtitle: ''
summary: ''
authors:
- Xinshuo Weng
- Junyu Nan
- Kuan-Hui Lee
- Rowan McAllister
- Adrien Gaidon
- Nicholas Rhinehart
- Kris Kitani
tags: ["autonomous driving", "forecasting", "generative models", "machine learning"]
categories: []
date: '2022-01-01'
lastmod: 2024-07-15T15:34:55-04:00
featured: false
draft: false

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
publishDate: '2024-07-15T19:34:54.809571Z'
publication_types:
- 'paper-conference'
abstract: >-
  Predicting futures of surrounding agents is critical for autonomous systems such as
  self-driving cars. Instead of requiring accurate detection and tracking prior to
  trajectory prediction, an object agnostic Sequential Pointcloud Forecasting (SPF) task
  was proposed [28], which enables a forecast-then-detect pipeline effective for
  downstream detection and trajectory prediction. One limitation of prior work is that it
  forecasts only a deterministic sequence of future point clouds, despite the inherent
  uncertainty of dynamic scenes. In this work, we tackle the stochastic SPF problem by
  proposing a generative model with two main components: (1) a conditional variational
  recurrent neural network that models a temporally-dependent latent space; (2) a
  pyramid-LSTM that increases the fidelity of predictions with temporally-aligned skip
  connections. Through experiments on real-world autonomous driving datasets, our
  stochastic SPF model produces higher-fidelity predictions, reducing Chamfer distances by
  up to 56.6% compared to its deterministic counterpart. In addition, our model can
  estimate the uncertainty of predicted points, which can be helpful to downstream tasks.
publication: '*European Conference on Computer Vision*'
publication_short: '**ECCV**'
url_pdf: https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136870541.pdf
url_doi: https://link.springer.com/chapter/10.1007/978-3-031-19812-0_32
paper_versions:
- retrieved_at: '2026-05-22T01:21:55+00:00'
  source: 'source-page'
  url: 'https://link.springer.com/chapter/10.1007/978-3-031-19812-0_32'
---
