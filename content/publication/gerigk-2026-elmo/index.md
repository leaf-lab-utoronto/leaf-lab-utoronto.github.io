---
title: "ELMO: Emergent Representations In Imitation Learning Via Dynamic Hierarchical Action Chunking"
authors:
- Jasper Gerigk
- yang-xu
- nicholas-rhinehart
- Igor Gilitschenski
author_notes:
- "*"
- "*"
- "†"
- "†"
tags: ["imitation learning", "robotics", "manipulation", "machine learning", "benchmarks"]
date: '2026-11-25'
publishDate: '2026-11-25'
arxiv_date: '2026-11-25T17:19:06Z'
arxiv_date_source: https://arxiv.org/abs/2611.34741
publication_types:
- preprint
publication: '*[arXiv:2611.34741](https://arxiv.org/abs/2611.34741)*'
publication_short: '**arXiv**'
url_pdf: https://arxiv.org/pdf/2611.34741
url_doi: https://doi.org/10.48550/arXiv.2611.34741
url_project: https://uoft-isl.github.io/elmo.github.io/
url_code: https://github.com/uoft-isl/ELMO
summary: ELMO learns where to divide robot demonstrations into actions such as pushing or stacking, and how to carry out each action using live observations.
result_media:
  src: result-candidates/push-yellow-right.mp4
  type: video
  poster: result-candidates/push-yellow-right.webp
  alt: A bimanual robot pushes the yellow block to the right.
---

## Summary

ELMO learns where to divide a robot demonstration into actions such as pushing or stacking. A vision-language-action planner selects each action, and a decoder uses live observations to guide the robot until the next action begins. On Blocks, a benchmark designed to test whether a robot follows instructions when object positions change, ELMO succeeded in 38.6% of in-distribution trials. The strongest baseline succeeded in 4.9%.

<sup>*</sup> Jasper Gerigk and Yang Xu contributed equally. <sup>†</sup> Nicholas Rhinehart and Igor Gilitschenski jointly supervised the work.
