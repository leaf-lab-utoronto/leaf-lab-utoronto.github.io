---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Ving: Learning open-world navigation with visual goals'
subtitle: ''
summary: ''
authors:
- Dhruv Shah
- Benjamin Eysenbach
- Gregory Kahn
- Nicholas Rhinehart
- Sergey Levine
tags: ["computer vision", "machine learning", "offroad navigation", "model-based control", "robotics"]
categories: []
date: '2021-01-01'
lastmod: 2024-07-15T15:34:52-04:00
featured: false
draft: false
result_media:
  src: result-candidates/ving_mail.gif
  type: image
  alt: ViNG open-world navigation result animation

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
publishDate: '2024-07-15T19:34:52.584523Z'
publication_types:
- 'paper-conference'
abstract: >-
  We propose a learning-based navigation system for reaching visually indicated goals and
  demonstrate this system on a real mobile robot platform. Learning provides an appealing
  alternative to conventional methods for robotic navigation: instead of reasoning about
  environments in terms of geometry and maps, learning can enable a robot to learn about
  navigational affordances, understand what types of obstacles are traversable (e.g., tall
  grass) or not (e.g., walls), and generalize over patterns in the environment. However,
  unlike conventional planning algorithms, it is harder to change the goal for a learned
  policy during deployment. We propose a method for learning to navigate towards a goal
  image of the desired destination. By combining a learned policy with a topological graph
  constructed out of previously observed data, our system can determine how to reach this
  visually indicated goal even in the presence of variable appearance and lighting. Three
  key insights, waypoint proposal, graph pruning and negative mining, enable our method to
  learn to navigate in real-world environments using only offline data, a setting where
  prior methods struggle. We instantiate our method on a real outdoor ground robot and
  show that our system, which we call ViNG, outperforms previously-proposed methods for
  goal-conditioned reinforcement learning, including other methods that incorporate
  reinforcement learning and search. We also study how ViNG generalizes to unseen
  environments and evaluate its ability to adapt to such an environment with growing
  experience. Finally, we demonstrate ViNG on a number of real-world applications, such as
  last-mile delivery and warehouse inspection. We encourage the reader to visit the
  project website for videos of our experiments and demonstrations <sup
  xmlns:mml="http://www.w3.org/1998/Math/MathML"
  xmlns:xlink="http://www.w3.org/1999/xlink">1</sup> .
publication: '*IEEE International Conference on Robotics and Automation*'
url_pdf: https://escholarship.org/content/qt93m2m6w0/qt93m2m6w0.pdf
url_doi: https://doi.org/10.1109/ICRA48506.2021.9561936
url_project: https://sites.google.com/view/ving-robot/home
publication_short: '**ICRA**'
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W3112720093'
  updated: '2026-04-28T14:05:53.105641'
  title: 'ViNG: Learning Open-World Navigation with Visual Goals'
---
