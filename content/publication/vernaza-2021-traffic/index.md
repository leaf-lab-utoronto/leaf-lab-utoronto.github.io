---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Traffic prediction with reparameterized pushforward policy for autonomous vehicles
subtitle: ''
summary: ''
authors:
- Paul Vernaza
- Nicholas Rhinehart
tags: []
categories: []
date: '2021-11-01'
lastmod: 2024-07-15T15:34:48-04:00
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
publishDate: '2024-07-15T19:34:48.554020Z'
publication_types:
- "patent"
abstract: >-
  Systems and methods for vehicle behavior prediction include an imaging device that
  captures images of a vehicle in traffic. A processing device including policy stored in
  a memory of the processing device in communication with the imaging device
  stochastically models future behavior of the vehicle based on the captured images. A
  policy simulator in communication with the processing device simulates the policy as a
  reparameterized pushforward policy of a base distribution. An evaluator receives the
  simulated policy from the policy simulator and performs cross-entropy optimization on
  the future behavior of the vehicle by analyzing the simulated policy and updating the
  policy according to cross-entropy error. An alert system retrieves the future behavior
  of the vehicle and recognizes hazardous trajectories of the future trajectories and
  generates an audible alert using a speaker.
publication: 'U.S. Patent No. 11,189,171'
url_pdf: https://patentimages.storage.googleapis.com/10/b2/4d/cb2314f855d433/US11189171.pdf
paper_versions:
- retrieved_at: '2026-05-22T01:21:55+00:00'
  source: 'source-page'
  url: 'https://patents.google.com/patent/US11189171'
---
