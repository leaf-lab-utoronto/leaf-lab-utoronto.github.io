---
# Documentation: https://docs.hugoblox.com/managing-content/

title: 'Towards foundational LiDAR world models with efficient latent flow matching'
subtitle: ''
summary: ''
abstract: >-
  LiDAR-based world models offer more structured and geometry-aware representations than
  their image-based counterparts. However, existing LiDAR world models are narrowly
  trained; each model excels only in the domain for which it was built. This raises a
  critical question: can we develop LiDAR world models that exhibit strong transferability
  across multiple domains? To answer this, we conduct the first systematic domain transfer
  study across three demanding scenarios: (i) outdoor to indoor generalization, (ii)
  sparse- to dense-beam adaptation, and (iii) non-semantic to semantic transfer. Given
  different amounts of fine-tuning data, our experiments show that a single pretrained
  model can achieve up to 11\% absolute improvement (83\% relative) over training from
  scratch and outperforms training from scratch in 30/36 of our comparisons. This
  transferability significantly reduces the reliance on manually annotated data for
  semantic occupancy forecasting: our method exceeds previous baselines with only 5\% of
  the labeled training data of prior work. We also observed inefficiencies of current
  generative-model-based LiDAR world models, mainly through their under-compression of
  LiDAR data and inefficient training objectives. To address these issues, we propose a
  latent conditional flow matching (CFM)-based framework that achieves state-of-the-art
  reconstruction accuracy using only half the training data and a compression ratio 6
  times higher than that of prior methods. Our model also achieves SOTA performance on
  semantic occupancy forecasting while being 1.98x-23x more computationally efficient (a
  1.1x-3.9x FPS speedup) than previous methods.
authors:
- Tianran Liu
- Shengwen Zhao
- Nicholas Rhinehart

# Dates
date: '2025-06-30'
lastmod: 2025-06-30
publishDate: '2025-09-18'

categories: []
draft: false
featured: false
result_media:
  src: result-candidates/occfm-snippet.gif
  type: image
  alt: Foundational LiDAR world model occupancy forecasting result animation

# I.D.s and links.
publication: '*Advances in Neural Information Processing Systems*'
publication_short: '**NeurIPS**'
url_pdf: https://arxiv.org/pdf/2506.23434
url_project: https://orbis36.github.io/AdaFlowMatchingWM-Web/
url_doi: https://openreview.net/forum?id=OyX9cC9WaV 
publication_types:
- 'paper-conference'

# Tags.
tags: ["computer vision", "forecasting", "machine learning", "robotics"]

image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
paper_versions:
- retrieved_at: '2026-05-22T01:17:27+00:00'
  source: 'openreview'
  url: 'https://openreview.net/forum?id=OyX9cC9WaV'
  updated: '1776754749205'
  title: 'Towards foundational LiDAR world models with efficient latent flow matching'
---
