---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'PRECOG: PREdiction Conditioned On Goals in Visual Multi-Agent Settings'
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Rowan McAllister
- Kris Kitani
- Sergey Levine
tags: ["paper award", "forecasting", "generative models", "autonomous driving"]
categories: []
date: '2019-01-01'
lastmod: 2024-07-15T15:34:48-04:00
featured: false
draft: false
result_media:
  src: result-candidates/precog-teaser-snippet.mp4
  type: video
  alt: PRECOG multi-agent prediction result animation

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
publishDate: '2024-07-15T19:34:48.228106Z'
publication_types:
- 'paper-conference'
abstract: >-
  For autonomous vehicles (AVs) to behave appropriately on roads populated by human-driven
  vehicles, they must be able to reason about the uncertain intentions and decisions of
  other drivers from rich perceptual information. Towards these capabilities, we present a
  probabilistic forecasting model of future interactions between a variable number of
  agents. We perform both standard forecasting and the novel task of conditional
  forecasting, which reasons about how all agents will likely respond to the goal of a
  controlled agent (here, the AV). We train models on real and simulated data to forecast
  vehicle trajectories given past positions and LIDAR. Our evaluation shows that our model
  is substantially more accurate in multi-agent driving scenarios compared to existing
  state-of-the-art. Beyond its general ability to perform conditional forecasting queries,
  we show that our model's predictions of all agents improve when conditioned on knowledge
  of the AV's goal, further illustrating its capability to model agent interactions.
publication: '*Proceedings of the IEEE International Conference on Computer Vision*'
publication_short: '**ICCV**'
url_pdf: https://openaccess.thecvf.com/content_ICCV_2019/papers/Rhinehart_PRECOG_PREdiction_Conditioned_on_Goals_in_Visual_Multi-Agent_Settings_ICCV_2019_paper.pdf
url_doi: https://doi.org/10.1109/ICCV.2019.00291
url_project: https://sites.google.com/view/precog
url_code: https://github.com/nrhinehart/precog
highlight: <span style="color:#DC4633">Best Paper Award @ ICML 2019 Workshop on AI for Autonomous Driving</span>
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2943516367'
  updated: '2026-04-28T14:05:53.105641'
  title: 'PRECOG: PREdiction Conditioned on Goals in Visual Multi-Agent Settings'
---
