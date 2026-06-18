---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'CARFF: Conditional Auto-encoded Radiance Field for 3D Scene Forecasting'
subtitle: ''
summary: ''
authors:
- Jiezhi Yang
- Khushi Desai
- Charles Packer
- Harshil Bhatia
- Nicholas Rhinehart
- Rowan McAllister
- Joseph Gonzalez
tags: ["autonomous driving", "computer vision", "forecasting", "generative models", "machine learning", "robotics"]
categories: []
date: '2024-01-01'
lastmod: 2024-07-15T15:34:57-04:00
featured: false
draft: false

url_pdf: https://arxiv.org/pdf/2401.18075
url_project: https://www.carff.website/
url_code: https://github.com/StephenYangjz/CARFF

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
publishDate: '2024-07-15T19:34:56.648991Z'
publication_types:
- 'paper-conference'
abstract: >-
  We propose CARFF, a method for predicting future 3D scenes given past observations. Our
  method maps 2D ego-centric images to a distribution over plausible 3D latent scene
  configurations and predicts the evolution of hypothesized scenes through time. Our
  latents condition a global Neural Radiance Field (NeRF) to represent a 3D scene model,
  enabling explainable predictions and straightforward downstream planning. This approach
  models the world as a POMDP and considers complex scenarios of uncertainty in
  environmental states and dynamics. Specifically, we employ a two-stage training of
  Pose-Conditional-VAE and NeRF to learn 3D representations, and auto-regressively predict
  latent scene representations utilizing a mixture density network. We demonstrate the
  utility of our method in scenarios using the CARLA driving simulator, where CARFF
  enables efficient trajectory and contingency planning in complex multi-agent autonomous
  driving scenarios involving occlusions.
publication: '*European Conference on Computer Vision*'
publication_short: '**ECCV**'
url_doi: https://doi.org/10.48550/arXiv.2401.18075
paper_versions:
- retrieved_at: '2026-05-22T01:17:27+00:00'
  source: 'arxiv-page'
  url: 'https://arxiv.org/abs/2401.18075'
  pdf_url: 'https://arxiv.org/pdf/2401.18075'
---
