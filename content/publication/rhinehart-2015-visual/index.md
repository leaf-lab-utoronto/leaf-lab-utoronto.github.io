---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Visual chunking: A list prediction framework for region-based object detection'
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Jiaji Zhou
- Martial Hebert
- J Andrew Bagnell
tags: ["computer vision", "imitation learning", "machine learning"]
categories: []
date: '2015-01-01'
lastmod: 2024-07-15T15:34:44-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Sequential predictions on test data.'
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-07-15T19:34:43.540738Z'
publication_types:
- 'paper-conference'
abstract: >-
  We consider detecting objects in an image by iteratively selecting from a set of
  arbitrarily shaped candidate regions. Our generic approach, which we term visual
  chunking, reasons about the locations of multiple object instances in an image while
  expressively describing object boundaries. We design an optimization criterion for
  measuring the performance of a list of such detections as a natural extension to a
  common per-instance metric. We present an efficient algorithm with provable performance
  for building a high-quality list of detections from any candidate set of region-based
  proposals. We also develop a simple class-specific algorithm to generate a candidate
  region instance in near-linear time in the number of low-level superpixels that
  outperforms other region generating methods. In order to make predictions on novel
  images at testing time without access to ground truth, we develop learning approaches to
  emulate these algorithms' behaviors. We demonstrate that our new approach outperforms
  sophisticated baselines on benchmark datasets.
publication: '*IEEE International Conference on Robotics and Automation*'
publication_short: '**ICRA**'
url_doi: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7139960
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2169950930'
  updated: '2025-11-06T03:46:38.306776'
  title: 'Visual chunking: A list prediction framework for region-based object detection'
---
