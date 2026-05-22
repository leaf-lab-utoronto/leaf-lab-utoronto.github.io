---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Rapid exploration for open-world navigation with latent goal models
subtitle: ''
summary: ''
authors:
- Dhruv Shah
- Benjamin Eysenbach
- Gregory Kahn
- Nicholas Rhinehart
- Sergey Levine
tags: ["autonomous exploration", "offroad navigation", "robotics", "model-based control"]
categories: []
date: '2021-01-01'
lastmod: 2024-07-15T15:34:53-04:00
featured: false
draft: false
result_media:
  src: result-candidates/rss21_shorttalk_teaser.gif
  type: image
  alt: RECON rapid exploration result animation

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
publishDate: '2024-07-15T19:34:52.877993Z'
publication_types:
- 'paper-conference'
abstract: >-
  We describe a robotic learning system for autonomous exploration and navigation in
  diverse, open-world environments. At the core of our method is a learned latent variable
  model of distances and actions, along with a non-parametric topological memory of
  images. We use an information bottleneck to regularize the learned policy, giving us (i)
  a compact visual representation of goals, (ii) improved generalization capabilities, and
  (iii) a mechanism for sampling feasible goals for exploration. Trained on a large
  offline dataset of prior experience, the model acquires a representation of visual goals
  that is robust to task-irrelevant distractors. We demonstrate our method on a mobile
  ground robot in open-world exploration scenarios. Given an image of a goal that is up to
  80 meters away, our method leverages its representation to explore and discover the goal
  in under 20 minutes, even amidst previously-unseen obstacles and weather conditions.
  Please check out the project website for videos of our experiments and information about
  the real-world dataset used at https://sites.google.com/view/recon-robot.
publication: '*Conference on Robot Learning*'
publication_short: '**CoRL**'

url_pdf: https://proceedings.mlr.press/v164/shah22a/shah22a.pdf
url_project: https://sites.google.com/view/recon-robot
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W4287215707'
  updated: '2026-03-25T23:56:10.502304'
  title: 'Rapid Exploration for Open-World Navigation with Latent Goal Models'
---
