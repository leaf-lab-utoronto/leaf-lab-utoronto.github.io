---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Contingencies from observations: Tractable contingency planning with learned
  behavior models'
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Jeff He
- Charles Packer
- Matthew A Wright
- Rowan McAllister
- Joseph E Gonzalez
- Sergey Levine
tags: ["autonomous driving", "computer vision", "forecasting", "imitation learning", "machine learning", "model-based control", "robotics"]
categories: []
date: '2021-01-01'
lastmod: 2024-07-15T15:34:53-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false
result_media:
  src: result-candidates/cfo-right-snippet.mp4
  type: video
  alt: Contingency planning right-turn result animation

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-07-15T19:34:53.205711Z'
publication_types:
- 'paper-conference'
abstract: >-
  Humans have a remarkable ability to accurately reason about future events, including the
  behaviors and states of mind of other agents. Consider driving a car through a busy
  intersection: it is necessary to reason about the physics of the vehicle, the intentions
  of other drivers, and their beliefs about your own intentions. For example, if you
  signal a turn, another driver might yield to you; or if you enter the passing lane,
  another driver might decelerate to give you room to merge in front. Competent drivers
  must plan how they can safely react to a variety of potential future behaviors of other
  agents before they make their next move. This requires contingency planning: explicitly
  planning a set of conditional actions that depend on the stochastic outcome of future
  events. In this work, we develop a general-purpose contingency planner that is learned
  end-to-end using high-dimensional scene observations and low-dimensional behavioral
  observations. We use a conditional autoregressive flow model for contingency planning.
  We show how this model can tractably learn contingencies from behavioral observations.
  We developed a closed-loop control benchmark of realistic multi-agent scenarios in a
  driving simulator (CARLA), on which we compare our method to various noncontingent
  methods that reason about multi-agent future behavior, and find that our contingency
  planning method achieves qualitatively and quantitatively superior performance.
publication: '*IEEE International Conference on Robotics and Automation*'
publication_short: '**ICRA**'
url_pdf: https://ieeexplore.ieee.org/abstract/document/9561683
url_project: https://sites.google.com/view/contingency-planning
url_code: https://github.com/JeffTheHacker/ContingenciesFromObservations
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3154728557'
  updated: '2026-04-10T15:06:20.359241'
  title: 'Contingencies from Observations: Tractable Contingency Planning with Learned Behavior Models'
---
