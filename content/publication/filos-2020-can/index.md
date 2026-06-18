---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Can autonomous vehicles identify, recover from, and adapt to distribution shifts?
subtitle: ''
summary: ''
authors:
- Angelos Filos
- Panagiotis Tigkas
- Rowan McAllister
- Nicholas Rhinehart
- Sergey Levine
- Yarin Gal
tags: ["autonomous driving", "computer vision", "imitation learning", "model-based control", "machine learning"]
categories: []
date: '2020-01-01'
lastmod: 2024-07-15T15:34:50-04:00
featured: false
draft: false
result_media:
  src: result-candidates/rip_animation_edit.gif
  type: image
  alt: Robust imitative planning result animation

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
publishDate: '2024-07-15T19:34:50.173981Z'
publication_types:
- 'paper-conference'
abstract: >-
  Out-of-training-distribution (OOD) scenarios are a common challenge of learning agents
  at deployment, typically leading to arbitrary deductions and poorly-informed decisions.
  In principle, detection of and adaptation to OOD scenes can mitigate their adverse
  effects. In this paper, we highlight the limitations of current approaches to novel
  driving scenes and propose an epistemic uncertainty-aware planning method, called
  \emph{robust imitative planning} (RIP). Our method can detect and recover from some
  distribution shifts, reducing the overconfident and catastrophic extrapolations in OOD
  scenes. If the model's uncertainty is too great to suggest a safe course of action, the
  model can instead query the expert driver for feedback, enabling sample-efficient online
  adaptation, a variant of our method we term \emph{adaptive robust imitative planning}
  (AdaRIP). Our methods outperform current state-of-the-art approaches in the nuScenes
  \emph{prediction} challenge, but since no benchmark evaluating OOD detection and
  adaption currently exists to assess \emph{control}, we introduce an autonomous car
  novel-scene benchmark, \texttt{CARNOVEL}, to evaluate the robustness of driving agents
  to a suite of tasks with distribution shifts.
publication: '*International Conference on Machine Learning*'
publication_short: '**ICML**'
url_pdf: http://proceedings.mlr.press/v119/filos20a/filos20a.pdf
url_doi: http://proceedings.mlr.press/v119/filos20a.html
url_project: https://sites.google.com/view/av-detect-recover-adapt
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3035498040'
  updated: '2026-04-21T08:09:41.155169'
  title: 'Can Autonomous Vehicles Identify, Recover From, and Adapt to Distribution Shifts?'
---
