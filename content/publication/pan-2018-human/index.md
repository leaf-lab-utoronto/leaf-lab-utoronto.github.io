---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Human-Interactive Subgoal Supervision for Efficient Inverse Reinforcement Learning
subtitle: ''
summary: ''
authors:
- Xinlei Pan
- Eshed Ohn-Bar
- Nicholas Rhinehart
- Yan Xu
- Yilin Shen
- Kris M. Kitani
tags: ["imitation learning", "machine learning", "reward learning"]
categories: []
date: '2018-01-01'
lastmod: 2024-07-15T15:34:45-04:00
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
publishDate: '2024-07-15T19:34:45.626120Z'
publication_types:
- 'paper-conference'
abstract: >-
  Humans are able to understand and perform complex tasks by strategically structuring
  tasks into incremental steps or sub-goals. For a robot attempting to learn to perform a
  sequential task with critical subgoal states, these subgoal states can provide a natural
  opportunity for interaction with a human expert. This paper analyzes the benefit of
  incorporating a notion of subgoals into Inverse Reinforcement Learning (IRL) with a
  Human-In-The-Loop (HITL) framework. The learning process is interactive, with a human
  expert first providing input in the form of full demonstrations along with some subgoal
  states. These subgoal states defines a set of sub-tasks for the learning agent to
  complete in order to achieve the final goal. The learning agent queries for partial
  demonstrations corresponding to each sub-task as needed when the learning agent
  struggles with individual sub-task. The proposed Human Interactive IRL (HI-IRL)
  framework is evaluated on several discrete path-planning tasks. We demonstrate that
  subgoal-based interactive structuring of the learning task results in significantly more
  efficient learning, requiring only a fraction of the demonstration data needed for
  learning the underlying reward function with a baseline IRL model.
publication: '*Proceedings of the 17th International Conference on Autonomous Agents
  and MultiAgent Systems*'
publication_short: '**AAMAS**'
url_pdf: https://arxiv.org/pdf/1806.08479
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2808012189'
  updated: '2026-05-21T09:19:25.381259'
  title: 'Human-Interactive Subgoal Supervision for Efficient Inverse Reinforcement Learning'
---
