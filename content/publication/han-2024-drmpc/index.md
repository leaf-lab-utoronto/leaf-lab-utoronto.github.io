---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'DR-MPC: Deep Residual Model Predictive Control for Real-world Social Navigation'
subtitle: ''
summary: ''
authors:
- James R. Han
- Hugues Thomas
- Jian Zhang
- Nicholas Rhinehart
- Timothy D. Barfoot
tags: ["computer vision", "forecasting", "machine learning", "model-based control", "robotics", "reinforcement learning", "social navigation"]
categories: []
date: '2025-02-01'
lastmod: 2024-11-04
featured: false
draft: false
result_media:
  src: result-candidates/dr-mpc-snippet.mp4
  type: video
  alt: DR-MPC social robot navigation result animation

url_pdf: https://arxiv.org/pdf/2410.10646
url_code: https://github.com/James-R-Han/DR-MPC

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
publishDate: '2025-02'
publication_types:
- 'article-journal'
abstract: >-
  How can a robot safely navigate around people with complex motion patterns? Deep
  Reinforcement Learning (DRL) in simulation holds some promise, but much prior work
  relies on simulators that fail to capture the nuances of real human motion. Thus, we
  propose Deep Residual Model Predictive Control (DR-MPC) to enable robots to quickly and
  safely perform DRL from real-world crowd navigation data. By blending MPC with
  model-free DRL, DR-MPC overcomes the DRL challenges of large data requirements and
  unsafe initial behavior. DR-MPC is initialized with MPC-based path tracking, and
  gradually learns to interact more effectively with humans. To further accelerate
  learning, a safety component estimates out-of-distribution states to guide the robot
  away from likely collisions. In simulation, we show that DR-MPC substantially
  outperforms prior work, including traditional DRL and residual DRL models. Hardware
  experiments show our approach successfully enables a robot to navigate a variety of
  crowded situations with few errors using less than 4 hours of training data.
publication: '*IEEE Robotics and Automation Letters*'
publication_short: '**RA-L**'
url_doi: https://doi.org/10.1109/LRA.2025.3546106
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W4407948601'
  updated: '2026-05-21T09:19:25.381259'
  title: 'DR-MPC: Deep Residual Model Predictive Control for Real-World Social Navigation'
---
