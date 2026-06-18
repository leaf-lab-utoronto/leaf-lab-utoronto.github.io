---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Hybrid imitative planning with geometric and predictive costs in off-road environments
subtitle: ''
summary: ''
authors:
- Nitish Dashora
- Daniel Shin
- Dhruv Shah
- Henry Leopold
- David Fan
- Ali Agha-Mohammadi
- Nicholas Rhinehart
- Sergey Levine
tags: ["imitation learning", "machine learning", "model-based control", "offroad navigation", "robotics"]
categories: []
date: '2022-01-01'
lastmod: 2024-07-15T15:34:54-04:00
featured: false
draft: false
result_media:
  src: result-candidates/hip-snippet.mp4
  type: video
  alt: Hybrid imitative planning off-road navigation result animation

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
publishDate: '2024-07-15T19:34:54.509572Z'
publication_types:
- 'paper-conference'
abstract: >-
  Geometric methods for solving open-world off-road navigation tasks, by learning
  occupancy and metric maps, provide good generalization but can be brittle in outdoor
  environments that violate their assumptions (e.g., tall grass). Learning-based methods
  can directly learn collision-free behavior from raw observations, but are difficult to
  integrate with standard geometry-based pipelines. This creates an unfortunate conflict –
  either use learning and lose out on well-understood geometric navigational components,
  or do not use it, in favor of extensively hand-tuned geometry-based cost maps. In this
  work, we reject this dichotomy by designing the learning and non-learning-based
  components in a way such that they can be effectively combined in a self-supervised
  manner. Both components contribute to a planning criterion: the learned component
  contributes predicted traversability as rewards, while the geometric component
  contributes obstacle cost information. We instantiate and comparatively evaluate our
  system in both in-distribution and out-of-distribution environments, showing that this
  approach inherits complementary gains from the learned and geometric components and
  significantly outperforms either of them.
publication: '*International Conference on Robotics and Automation*'
publication_short: '**ICRA**'
url_pdf: https://arxiv.org/pdf/2111.10948
url_doi: https://doi.org/10.1109/ICRA46639.2022.9811540
url_project: https://sites.google.com/view/hybrid-imitative-planning
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3217571039'
  updated: '2026-03-10T16:38:18.471706'
  title: 'Hybrid Imitative Planning with Geometric and Predictive Costs in Off-road Environments'
---
