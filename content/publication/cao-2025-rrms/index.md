---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Residual Reward Models for Preference-based Reinforcement Learning'
subtitle: ''
summary: ''
authors:
- Chenyang Cao
- Miguel Rogel-García
- Mohamed Nabail
- Xueqian Wang
- Nicholas Rhinehart
tags: ["reward learning", "machine learning", "robotics", "reinforcement learning", "manipulation"]
categories: []
date: '2025-07-01'
lastmod: 2025-07-01
publishDate: '2025-07-01'
featured: false
draft: false

result_media:
  src: result-candidates/rrm-snippet.gif

url_pdf: https://arxiv.org/pdf/2507.00611
url_project: https://sunlighted.github.io/RRM-web/
publication: '*arXiv:2507.00611*'
publication_short: '**arXiv**'

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
publication_types:
- 'preprint'
abstract: >-
  Preference-based Reinforcement Learning (PbRL) provides a way to learn high-performance
  policies in environments where the reward signal is hard to specify, avoiding heuristic
  and time-consuming reward design. However, PbRL can suffer from slow convergence speed
  since it requires training in a reward model. Prior work has proposed learning a reward
  model from demonstrations and fine-tuning it using preferences. However, when the model
  is a neural network, using different loss functions for pre-training and fine-tuning can
  pose challenges to reliable optimization. In this paper, we propose a method to
  effectively leverage prior knowledge with a Residual Reward Model (RRM). An RRM assumes
  that the true reward of the environment can be split into a sum of two parts: a prior
  reward and a learned reward. The prior reward is a term available before training, for
  example, a user's ``best guess'' reward function, or a reward function learned from
  inverse reinforcement learning (IRL), and the learned reward is trained with
  preferences. We introduce state-based and image-based versions of RRM and evaluate them
  on several tasks in the Meta-World environment suite. Experimental results show that our
  method substantially improves the performance of a common PbRL method. Our method
  achieves performance improvements for a variety of different types of prior rewards,
  including proxy rewards, a reward obtained from IRL, and even a negated version of the
  proxy reward. We also conduct experiments with a Franka Panda to show that our method
  leads to superior performance on a real robot. It significantly accelerates policy
  learning for different tasks, achieving success in fewer steps than the baseline. The
  videos are presented at https://sunlighted.github.io/RRM-web/.
paper_versions:
- retrieved_at: '2026-05-22T01:17:27+00:00'
  source: 'arxiv-page'
  url: 'https://arxiv.org/abs/2507.00611'
  pdf_url: 'https://arxiv.org/pdf/2507.00611'
---
