---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Learning Neural Parsers with Deterministic Differentiable Imitation Learning
subtitle: ''
summary: ''
authors:
- Tanmay Shankar
- Nicholas Rhinehart
- Katharina Muelling
- Kris M. Kitani
tags: ["imitation learning", "machine learning"]
categories: []
date: '2018-01-01'
lastmod: 2024-07-15T15:34:45-04:00
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
publishDate: '2024-07-15T19:34:45.325971Z'
publication_types:
- 'paper-conference'
abstract: >-
  We explore the problem of learning to decompose spatial tasks into segments, as
  exemplified by the problem of a painting robot covering a large object. Inspired by the
  ability of classical decision tree algorithms to construct structured partitions of
  their input spaces, we formulate the problem of decomposing objects into segments as a
  parsing approach. We make the insight that the derivation of a parse-tree that
  decomposes the object into segments closely resembles a decision tree constructed by
  ID3, which can be done when the ground-truth available. We learn to imitate an expert
  parsing oracle, such that our neural parser can generalize to parse natural images
  without ground truth. We introduce a novel deterministic policy gradient update, DRAG
  (i.e., DeteRministically AGgrevate) in the form of a deterministic actor-critic variant
  of AggreVaTeD, to train our neural parser. From another perspective, our approach is a
  variant of the Deterministic Policy Gradient suitable for the imitation learning
  setting. The deterministic policy representation offered by training our neural parser
  with DRAG allows it to outperform state of the art imitation and reinforcement learning
  approaches.
publication: '*Conference on Robot Learning*'
publication_short: '**CoRL**'
url_pdf: http://proceedings.mlr.press/v87/shankar18a/shankar18a.pdf
url_doi: http://proceedings.mlr.press/v87/shankar18a
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2808879645'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Learning Neural Parsers with Deterministic Differentiable Imitation Learning'
---
