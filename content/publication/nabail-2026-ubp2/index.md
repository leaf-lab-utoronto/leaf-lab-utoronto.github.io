---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'UBP2: Uncertainty-Balanced Preference Planning for Efficient Preference-based Reinforcement Learning'
authors:
- Mohamed Nabail
- Leo Cheng
- Jingmin Wang
- Nicholas Rhinehart
tags: ["reinforcement learning", "machine learning", "model-based control", "robotics", "reward learning"]
date: '2026-06-17'
lastmod: 2026-06-17
publishDate: '2026-06-17'
url_pdf: https://arxiv.org/pdf/2606.19328
url_doi: https://doi.org/10.48550/arXiv.2606.19328
publication: '*arXiv:2606.19328*'
publication_short: '**arXiv**'
publication_types:
- 'preprint'

abstract: >-
  Preference-based RL provides an approach to learning reward models from pairwise
  comparisons of behaviors, bypassing the need for explicit reward design. However,
  existing methods typically rely on passive data collection and suffer from poor sample
  efficiency, especially during the early stages of learning. We introduce a model-based
  approach that actively directs exploration by jointly reasoning over uncertainties in
  the reward, dynamics, and value functions. Our method, Uncertainty-Balanced Preference
  Planning (UBP2), uses ensembles of reward, dynamics, and value function models to
  evaluate candidate trajectories according to a unified score that combines expected
  reward, terminal value, and epistemic uncertainty. Planning under this objective yields
  an explicit tradeoff between exploitation and information acquisition without requiring
  ad hoc exploration heuristics. Under standard regularity assumptions, we establish
  sublinear regret guarantees for both finite-horizon and infinite-horizon settings.
  Empirically, experiments on the Meta-World benchmark show UBP2 achieves substantially
  higher sample efficiency than model-free preference-based methods and non-optimistic
  model-based baselines.
categories: []
subtitle: ''
summary: ''
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Smart'
  preview_only: false

# Projects (optional).
projects: []
---
