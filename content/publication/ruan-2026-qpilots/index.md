---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'QPILOTS: Efficient Test-Time Q-Steering for Flow Policies'
authors:
- Yifan Ruan
- Chenyang Cao
- Andreas Burger
- Ali Pesaranghader
- Kaveh Kamali
- Jaehong Kim
- Nandita Vijaykumar
- Alan Aspuru-Guzik
- Igor Gilitschenski
- Nicholas Rhinehart
tags: ["reinforcement learning", "machine learning", "robotics", "generative models"]
date: '2026-06-11'
lastmod: 2026-06-11
publishDate: '2026-06-11'
url_pdf: https://arxiv.org/pdf/2606.14801
url_doi: https://doi.org/10.48550/arXiv.2606.14801
publication: '*arXiv:2606.14801*'
publication_short: '**arXiv**'
publication_types:
- 'preprint'

abstract: >-
  Flow-matching and diffusion policies are expressive action generators, but optimizing
  them with temporal-difference reinforcement learning (RL) remains difficult. Effective
  policy extraction requires exploiting the critic's action gradient, yet directly
  backpropagating this signal through a multi-step denoising process can be numerically
  unstable. Existing methods work around this either by discarding gradient information,
  distilling the policy into a simpler one-step actor, or repeatedly fine-tuning the
  denoising policy as the critic improves. We propose QPILOTS, a method that leaves the
  original policy unmodified and steers the denoising process at inference time. At each
  denoising step, instead of evaluating the critic on the noisy intermediate action where
  critic predictions are unreliable, we first project that intermediate state to an
  estimate of the final clean action and compute the critic gradient there. We introduce
  two variants: QPILOTS-U uses a fast single-point approximation, while QPILOTS-M draws
  differentiable posterior samples via a learned auxiliary network. On a standard
  offline-to-online RL benchmark, QPILOTS achieves the best aggregate performance, reaching
  an average success rate of 90% across 50 tasks. We also apply QPILOTS to steer a large,
  frozen, pretrained Vision-Language Action (VLA) foundation model, outperforming or
  matching prior inference-time approaches across six manipulation tasks in simulation.
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
