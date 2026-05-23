---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Offline reinforcement learning for visual navigation
subtitle: ''
summary: ''
authors:
- Dhruv Shah
- Arjun Bhorkar
- Hrish Leen
- Ilya Kostrikov
- Nicholas Rhinehart
- Sergey Levine
tags: ["computer vision", "machine learning", "offroad navigation", "reinforcement learning", "robotics"]
categories: []
date: '2022-01-01'
lastmod: 2024-07-15T15:34:55-04:00
featured: false
draft: false
result_media:
  src: result-candidates/revind-snippet.mp4
  type: video
  alt: ReViND offline RL visual navigation result animation

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
publishDate: '2024-07-15T19:34:55.155364Z'
publication_types:
- 'paper-conference'
abstract: >-
  Reinforcement learning can enable robots to navigate to distant goals while optimizing
  user-specified reward functions, including preferences for following lanes, staying on
  paved paths, or avoiding freshly mowed grass. However, online learning from
  trial-and-error for real-world robots is logistically challenging, and methods that
  instead can utilize existing datasets of robotic navigation data could be significantly
  more scalable and enable broader generalization. In this paper, we present ReViND, the
  first offline RL system for robotic navigation that can leverage previously collected
  data to optimize user-specified reward functions in the real-world. We evaluate our
  system for off-road navigation without any additional data collection or fine-tuning,
  and show that it can navigate to distant goals using only offline training from this
  dataset, and exhibit behaviors that qualitatively differ based on the user-specified
  reward function.
url_pdf: https://proceedings.mlr.press/v205/shah23a/shah23a.pdf
url_project: https://sites.google.com/view/revind
url_code: https://github.com/arjunbhorkar/ReViND
publication: '*Conference on Robot Learning*'
publication_short: '**CoRL**'
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W4311992093'
  updated: '2026-02-09T09:26:11.010843'
  title: 'Offline Reinforcement Learning for Visual Navigation'
---
