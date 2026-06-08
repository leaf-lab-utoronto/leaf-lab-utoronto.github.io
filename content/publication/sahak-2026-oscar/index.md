---
title: 'OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation'
authors:
- Hshmat Sahak
- Aoran Jiao
- Nicholas Rhinehart
- Tim Barfoot
tags: ["robotics", "model-based control", "offroad navigation", "machine learning", "forecasting"]
date: '2026-06-01'
publishDate: '2026-06-08T13:40:15.484155Z'
publication_types:
- 'preprint'
publication: '*arXiv:2606.00990*'
publication_short: '**arXiv**'
url_pdf: https://arxiv.org/pdf/2606.00990
url_doi: https://doi.org/10.48550/arXiv.2606.00990
abstract: >-
  A mobile robot following a graph of known routes can make costly navigation errors when
  a temporary obstacle blocks a critical edge: waiting too long behind a parked cart
  wastes time, but immediately rerouting around a person who would move in a few seconds
  is also inefficient. Standard reactive obstacle avoidance addresses local motion around
  obstacles, while fixed wait-or-reroute rules ignore how long different obstacle types
  tend to persist. We propose OSCAR: an adaptive survival-modeling framework for
  graph-based navigation with temporary blockages. Assuming obstacle class labels are
  available at encounter time, the robot learns class-conditioned residual clearance-time
  distributions from online experience, including right-censored observations when it
  reroutes before observing clearance. These survival models are integrated into a
  time-dependent graph planner that maintains obstacle memory and computes a patience
  threshold at each blocked edge: how long to wait before taking an alternate route. The
  method continuously updates its clearance estimates across episodes and uses them to
  balance waiting against rerouting. We evaluate the approach in simulation and on a real
  mobile robot in a university atrium with obstacles including people, chairs, bins, and
  tubes. In simulation, the learned policy's time-to-goal converges to within 1% of an
  oracle with access to ground-truth clearance distributions after fewer than 20
  observations per obstacle class, outperforming all heuristic baselines. Real-world
  deployment confirms that the policy improves online, adapting its patience thresholds
  from experience across 50 navigation episodes.
draft: false
result_media:
  src: result-candidates/oscar-snippet.mp4
  type: video
  alt: OSCAR adaptive robot navigation result video
paper_versions:
- retrieved_at: '2026-06-08T13:50:09+00:00'
  source: 'openalex'
  url: 'https://openalex.org/W7163173669'
  updated: '2026-06-03T06:26:03.838407'
  title: 'OSCAR: Obstacle Survival Curves for Adaptive Robot Navigation'
---
