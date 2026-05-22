---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Inverting the pose forecasting pipeline with SPF2: Sequential pointcloud forecasting
  for sequential pose forecasting'
subtitle: ''
summary: ''
authors:
- Xinshuo Weng
- Jianren Wang
- Sergey Levine
- Kris Kitani
- Nicholas Rhinehart
tags: ["autonomous driving", "computer vision", "generative models", "machine learning", "robotics"]
categories: []
date: '2021-01-01'
lastmod: 2024-07-15T15:34:51-04:00
featured: false
draft: false
result_media:
  src: result-candidates/spf2.gif
  type: image
  alt: Sequential pointcloud forecasting result animation

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
publishDate: '2024-07-15T19:34:51.353485Z'
publication_types:
- 'paper-conference'
abstract: >-
  Many autonomous systems forecast aspects of the future in order to aid decision-making.
  For example, self-driving vehicles and robotic manipulation systems often forecast
  future object poses by first detecting and tracking objects. However, this
  detect-then-forecast pipeline is expensive to scale, as pose forecasting algorithms
  typically require labeled sequences of object poses, which are costly to obtain in 3D
  space. Can we scale performance without requiring additional labels? We hypothesize yes,
  and propose inverting the detect-then-forecast pipeline. Instead of detecting, tracking
  and then forecasting the objects, we propose to first forecast 3D sensor data (e.g.,
  point clouds with $100$k points) and then detect/track objects on the predicted point
  cloud sequences to obtain future poses, i.e., a forecast-then-detect pipeline. This
  inversion makes it less expensive to scale pose forecasting, as the sensor data
  forecasting task requires no labels. Part of this work's focus is on the challenging
  first step --Sequential Pointcloud Forecasting (SPF), for which we also propose an
  effective approach, SPFNet. To compare our forecast-then-detect pipeline relative to the
  detect-then-forecast pipeline, we propose an evaluation procedure and two metrics.
  Through experiments on a robotic manipulation dataset and two driving datasets, we show
  that SPFNet is effective for the SPF task, our forecast-then-detect pipeline outperforms
  the detect-then-forecast approaches to which we compared, and that pose forecasting
  performance improves with the addition of unlabeled data.
publication: '*Conference on robot learning*'
publication_short: '**CoRL**'
url_pdf: https://proceedings.mlr.press/v155/weng21a/weng21a.pdf
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3102823913'
  updated: '2026-03-20T23:20:44.827607'
  title: 'Inverting the Pose Forecasting Pipeline with SPF2: Sequential Pointcloud Forecasting for Sequential Pose Forecasting'
---
