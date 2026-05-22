---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Jointly Forecasting and Controlling Behavior by Learning from High-Dimensional
  Data
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
tags: ["autonomous driving", "forecasting", "generative models", "imitation learning", "model-based control", "reinforcement learning", "reward learning"]
categories: []
date: '2019-01-01'
lastmod: 2024-07-15T15:34:49-04:00
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
publishDate: '2024-07-15T19:34:48.845334Z'
publication_types:
- 'thesis'
abstract: >-
  Achieving a precise predictive understanding of the future is difficult, yet widely
  studied in the natural sciences. Significant research activity has been dedicated to
  building testable models of cause and effect. From a certain view, the ability to
  forecast the universe is the “holy grail”; the ultimate goal of science. If we had it,
  we could anticipate, and therefore (at least implicitly) understand all observable
  phenomena. The human capability to forecast offers complementary motivation. Critical to
  our intelligence is our ability to plan behaviors by considering how our actions are
  likely to result in future payoff, especially in the presence of other collaborative and
  competitive agents. In this work, we seek to computationally model the future in the
  presence of agent behavior given rich observations of the environment. The brunt of our
  focus is to reason about what agents could do, instead of other sources of
  stochasticity. This focus on future agent behavior allows us to tightly couple and
  jointly perform forecasting and control. The field of Computer Vision (CV) is focused on
  designing algorithms to automatically understand images, videos, and other perceptual
  data. However, the field’s effort to-date focuses on non-interactive, present-focused
  tasks [79, 81, 158, 184]. Most CV contributions are algorithms to answer questions like
  “what is that”, and “what happened”, rather than “what could happen”, or “how could I
  achieve X”. Computer Vision has under-explored reasoning about the interactive and
  decision-based nature of the world. In contrast, Reinforcement Learning (RL) prioritizes
  modeling interactions and decisions by focusing on how to design algorithms to evoke
  behavior that maximizes a scalar reward signal. The resulting learning agents, in order
  to perform well, must have an understanding of how their current behaviors will affect
  their prospects of future reward. However, in the dominant paradigm of model-free RL
  [218], agents reason implicitly about the future. In contrast, model-based RL learns
  one-step dynamics to estimate “what could happen in the near future”. Yet model-based RL
  primarily focuses on control, rather than explicitly forecasting a single agent (let
  alone multiple agents). In this thesis, we consider the problem of designing algorithms
  to enable computational systems to (1) forecast future behavior of intelligent agents
  given rich observations of their environments, as well as to (2) use this reasoning for
  control. We believe these two problems should be tightly integrated and jointly
  considered, and use them to structure this thesis. We define forecasting to be the
  problem of estimating the set of possible outcomes of a system, whereas control is the
  problem of producing actions that generate a single outcome of a system. We often use
  Imitation Learning and Reinforcement Learning to formulate and situate our work. We
  contribute forecasting and control approaches to excel in diverse, realistic,
  single-agent, and multi-agent domains. The first part of the thesis focuses on
  progressively designing more capable forecasting models. We proceed through approaches
  to (1) forecast single actions of daily behavior by developing matrix factorization
  models [169], (2) forecast goal-driven action trajectories of daily behavior by
  developing Online Inverse Reinforcement Learning models [168, 170], (3) forecast motion
  trajectories of vehicles by developing a deep reversible generative models [171, 174].
  The second part of the thesis focuses on progressively designing more capable models
  that tightly couple forecasting and control. We discuss (4) forecasting as auxiliary
  supervision for implicitly-planned control [228], (5) forecasting and explicitly
  planning with the same model [176], and (6) forecasting and planning future interactions
  of multiple agents [175].
publication: ''
url_project: https://kilthub.cmu.edu/articles/thesis/Jointly_Forecasting_and_Controlling_Behavior_by_Learning_from_High-Dimensional_Data/9934172
# url_pdf: './paper.pdf'
paper_versions:
- retrieved_at: '2026-05-22T01:21:55+00:00'
  source: 'figshare'
  url: 'https://api.figshare.com/v2/articles/9934172'
  updated: '2019-10-18T19:07:24Z'
  title: 'Jointly Forecasting and Controlling Behavior by Learning from High-Dimensional Data'
---
