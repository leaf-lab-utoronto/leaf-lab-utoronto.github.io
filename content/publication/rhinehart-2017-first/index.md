---
# Documentation: https://docs.hugoblox.com/managing-content/

title: First-Person Activity Forecasting with Online Inverse Reinforcement Learning
subtitle: ''
summary: ''
authors:
- Nicholas Rhinehart
- Kris M. Kitani
tags: ["paper award", "imitation learning", "reward learning", "first-person video", "forecasting"]
categories: []
date: '2017-01-01'
lastmod: 2024-07-15T15:34:44-04:00
featured: false
draft: false
result_media:
  src: result-candidates/darko-teaser-snippet.mp4
  type: video
  alt: First-person activity forecasting result animation

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Predicted goals and actions in the home environment.'
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-07-15T19:34:44.370652Z'
publication_types:
- 'paper-conference'
abstract: >-
  We address the problem of incrementally modeling and forecasting long-term goals of a
  first-person camera wearer: what the user will do, where they will go, and what goal
  they seek. In contrast to prior work in trajectory forecasting, our algorithm, DARKO,
  goes further to reason about semantic states (will I pick up an object?), and future
  goal states that are far in terms of both space and time. DARKO learns and forecasts
  from first-person visual observations of the user’s daily behaviors via an Online
  Inverse Reinforcement Learning (IRL) approach. Classical IRL discovers only the rewards
  in a batch setting, whereas DARKO discovers the states, transitions, rewards, and goals
  of a user from streaming data. Among other results, we show DARKO forecasts goals better
  than competing methods in both noisy and ideal settings, and our approach is
  theoretically and empirically no-regret.
publication: '*The IEEE International Conference on Computer Vision*'
publication_short: '**ICCV**'
url_pdf: https://openaccess.thecvf.com/content_ICCV_2017/papers/Rhinehart_First-Person_Activity_Forecasting_ICCV_2017_paper.pdf
highlight: <span style="color:#DC4633">Best Paper Honorable Mention</span>
paper_versions:
- retrieved_at: '2026-05-22T01:04:48+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W2777985721'
  updated: '2026-03-20T23:20:44.827607'
  title: 'First-Person Activity Forecasting with Online Inverse Reinforcement Learning'
---
