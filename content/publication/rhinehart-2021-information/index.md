---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Information is power: Intrinsic control via information capture'
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Jenny Wang
- Glen Berseth
- John Co-Reyes
- Danijar Hafner
- Chelsea Finn
- Sergey Levine
tags: ["autonomous exploration", "intrinsic control", "generative models", "reinforcement learning"]
categories: []
date: '2021-01-01'
lastmod: 2024-07-15T15:34:54-04:00
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
publishDate: '2024-07-15T19:34:54.149648Z'
publication_types:
- 'paper-conference'
abstract: >-
  Humans and animals explore their environment and acquire useful skills even in the
  absence of clear goals, exhibiting intrinsic motivation. The study of intrinsic
  motivation in artificial agents is concerned with the following question: what is a good
  general-purpose objective for an agent? We study this question in dynamic
  partially-observed environments, and argue that a compact and general learning objective
  is to minimize the entropy of the agent's state visitation estimated using a latent
  state-space model. This objective induces an agent to both gather information about its
  environment, corresponding to reducing uncertainty, and to gain control over its
  environment, corresponding to reducing the unpredictability of future world states. We
  instantiate this approach as a deep reinforcement learning agent equipped with a deep
  variational Bayes filter. We find that our agent learns to discover, represent, and
  exercise control of dynamic objects in a variety of partially-observed environments
  sensed with visual observations without extrinsic reward.
publication: '*Advances in Neural Information Processing Systems*'
publication_short: '**NeurIPS**'
url_pdf: https://proceedings.neurips.cc/paper_files/paper/2021/file/59112692262234e3fad47fa8eabf03a4-Paper.pdf
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3211993735'
  updated: '2026-04-17T18:11:37.981687'
  title: 'Information is Power: Intrinsic Control via Information Capture'
---
