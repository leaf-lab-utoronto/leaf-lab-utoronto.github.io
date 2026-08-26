---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: ''
      text: |
        <div class="row homepage-welcome">
          <div class="section-heading homepage-welcome-profile col-12 col-lg-3 d-flex flex-column align-items-center align-items-lg-start">
            <h1 class="mb-0" style="align-self: center">Welcome</h1>  
            <div id="profile" style="align-self: center">
              <img class="avatar avatar-square homepage-profile-photo img-fluid"
              src="/images/nr_avatar.jpg" alt="Nicholas Rhinehart"
              style="max-width: 270px; width: 100%; aspect-ratio: 1; object-fit: cover;"
              >
              <p class="cta-btns" style="display: flex; justify-content: center; column-gap: 1vw">
                <a href="/publication" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-book-open-reader pr-1" aria-hidden="true"></i>Read our work</a>
                <a href="/apply" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-flask pr-1" aria-hidden="true"></i>Join us</a>
              </p>
              <!--
              <ul class="network-icon" aria-hidden="true" style="justify-content: center; margin-top: 0.5rem; margin-bottom: 0;">
                <li><a href="mailto:nick.rhinehart@utoronto.ca" aria-label="envelope"><i class="fas fa-envelope"></i></a></li>
                <li><a href="/files/cv_nick_rhinehart.pdf" aria-label="cv"><i class="ai ai-cv"></i></a></li>
                <li><a href="https://scholar.google.com/citations?user=xUGZX_MAAAAJ" target="_blank" rel="noopener" aria-label="google-scholar"><i class="ai ai-google-scholar"></i></a></li>
                <li><a href="https://orcid.org/0000-0003-4242-1236" target="_blank" rel="noopener" aria-label="orcid"><i class="ai ai-orcid"></i></a></li>
                <li><a href="https://twitter.com/nick_rhinehart" target="_blank" rel="noopener" aria-label="twitter"><i class="fab fa-twitter"></i></a></li>
                <li><a href="https://www.linkedin.com/in/nicholas-rhinehart-0b164341/" target="_blank" rel="noopener" aria-label="linkedin"><i class="fab fa-linkedin"></i></a></li>
              </ul>
              -->
            </div>
          </div>
          <div class="col-12 col-lg-9 homepage-welcome-copy-column">
            <div class="article-style homepage-welcome-copy">
              <p>Welcome to the homepage of the <strong>Learning, Embodied Autonomy, and Forecasting (LEAF)</strong> lab, affiliated with the <a href="https://robotics.utoronto.ca" target="_blank">Robotics Institute</a>, <a href="https://utias.utoronto.ca" target="_blank">Institute for Aerospace Studies</a>, and <a href="https://web.cs.toronto.edu" target="_blank">Department of Computer Science</a> at the <a href="https://utoronto.ca" target="_blank">University of Toronto</a>. The LEAF lab is led by <a href="author/nicholas-rhinehart/">Prof. Nick Rhinehart</a>.</p>
              <p>One of our central aims is <strong>general-purpose model-based control</strong>: autonomous systems that can be directed to perform a wide range of tasks by combining accurate models of the world with learned objectives. Two capabilities are essential to this vision: <strong>forecasting</strong> [<a href="/publication/liu-2026-occsim/">1</a>,<a href="/publication/pourkeshavarz-2026-autoworld/">2</a>,<a href="/publication/liu-2025-flwms/">3</a>,<a href="/publication/yang-2024-carff/">4</a>,<a href="/publication/han-2024-drmpc/">5</a>,<a href="/publication/weng-2022-s-2-net/">6</a>,<a href="/publication/packer-2023-anyone/">7</a>,<a href="/publication/rhinehart-2021-contingencies/">8</a>,<a href="/publication/weng-2021-inverting/">9</a>], learning to predict future observations and outcomes from rich sensor data, and <strong>reward learning</strong> [<a href="/publication/cao-2025-rrms/">10</a>,<a href="/publication/nabail-2026-ubp2/">11</a>,<a href="/publication/rhinehart-2020-deep/">12</a>,<a href="/publication/rhinehart-2018-r-2-p-2/">13</a>,<a href="/publication/rhinehart-2017-first/">14</a>,<a href="/publication/rhinehart-2016-learning/">15</a>], inferring what humans actually want from demonstrations, preferences, and other feedback. Together, these would allow an agent to simulate what will happen under different actions and select behavior aligned with human intent, without requiring hand-designed rewards or task-specific engineering. Our research draws on <strong>imitation learning</strong>, <strong>reinforcement learning</strong>, <strong>generative modeling</strong>, and <strong>information theory</strong>, with applications spanning autonomous driving, robot navigation, manipulation, and beyond.</p>
              <p>Current research thrusts include: learning <strong>transferable world models</strong> over high-dimensional sensor data such as LiDAR and occupancy [<a href="/publication/liu-2026-occsim/">1</a>,<a href="/publication/liu-2025-flwms/">3</a>]; using world models to enable <strong>realistic large-scale simulation and efficient planning</strong> [<a href="/publication/liu-2026-occsim/">1</a>,<a href="/publication/pourkeshavarz-2026-autoworld/">2</a>]; and learning <strong>reward and objective functions from human feedback</strong> [<a href="/publication/cao-2025-rrms/">10</a>,<a href="/publication/nabail-2026-ubp2/">11</a>] so that autonomous systems can perform complex tasks in alignment with human intent.</p>
            </div>
          </div>
        </div>


  - block: collection
    id: news
    content:
      title: News
      text: '<span class="homepage-news-marker"></span>'
      count: 7
      filters:
        folders:
          - event
    # See options here: https://docs.hugoblox.com/getting-started/page-builder/#listing-view
    design:
      view: event_list
      columns: '2'
  - block: markdown
    content:
      title: ''
      text: |
        <div class="row homepage-group-photo">
          <div class="section-heading col-12 mb-3 text-center">
            <h1 class="mb-0">Our team</h1>
          </div>
          <div class="col-12 text-center">
            <img src="/images/lab-group-photo.jpg" alt="LEAF Lab group photo" style="max-width:640px; width:100%; border-radius:8px; display:block; margin:0 auto;">
          </div>
        </div>

  - block: collection
    id: recent-publications
    content:
      title: Recent publications
      text: '<span class="homepage-recent-publications-marker"></span>'
      count: 5
      filters:
        folders:
          - publication
    design:
      view: citation
      columns: '2'
  - block: markdown
    content:
      title: ''
      text: |
        <div class="row homepage-research-interests">
          <div class="section-heading col-12 mb-3 d-flex flex-column align-items-center">
            <h1 class="mb-0">Our research interests</h1>  
          </div>
        <div class="col-12">
          <div style="display:flex; justify-content: center; column-gap: 2.5rem; row-gap: 1vw; font-size: medium; text-align:left; flex-wrap: wrap">
          <div class="research-interests">
            <h2>Fields:</h2>
            <ul>
            <li><a href="./tag/robotics">Robotics</a></li>
            <li><a href="./tag/machine-learning">Machine Learning</a></li>
            <li><a href="./tag/computer-vision">Computer Vision</a></li>
            </ul>
            </div>
          <div>
            <h2>Topics:</h2>
            <ul>
            <li><a href="./tag/forecasting">Forecasting</a></li>
            <li><a href="./tag/imitation-learning">Imitation learning</a></li>
            <li><a href="./tag/reinforcement-learning">Reinforcement learning</a></li>
            <li><a href="./tag/generative-models">Generative models</a></li>
            <li><a href="./tag/intrinsic-control">Intrinsic control</a></li>
            <li><a href="./tag/model-based-control">Model-based control</a></li>
            <li><a href="./tag/reward-learning">Reward learning</a></li>
            </ul>
            </div>
            <div>
            <h2>Applications:</h2>
            <ul>
            <li><a href="./tag/autonomous-driving">Autonomous driving</a></li>
            <li><a href="./tag/autonomous-exploration">Autonomous exploration</a></li>
            <li><a href="./tag/manipulation">Manipulation</a></li>
            <li><a href="./tag/offroad-navigation">Offroad Navigation</a></li>
            <li><a href="./tag/social-navigation">Social Navigation</a></li>
            </ul>
            </div>
          <div>
            <h2>Other interests:</h2>
            <ul>
            <li><a href="./tag/benchmarks">Benchmarks</a></li>
            <li><a href="./tag/compression">Compression</a></li>
            <li><a href="./tag/first-person-video">First-person video</a></li>
            </ul>
          </div>	
        </div>

  - block: markdown
    content:
      title: ''
      text: |
        <div class="homepage-funders">
          <h1>Supported by</h1>
          <div class="homepage-funder-logos" aria-label="LEAF lab funders and supporters">
            <a href="https://www.nserc-crsng.gc.ca/" target="_blank" rel="noopener" aria-label="Natural Sciences and Engineering Research Council of Canada">
              <img src="/images/funders/nserc.png" alt="NSERC CRSNG">
            </a>
            <a href="https://www.innovation.ca/" target="_blank" rel="noopener" aria-label="Canada Foundation for Innovation" class="homepage-funder-logo-wide">
              <img src="/images/funders/cfi.png" alt="Canada Foundation for Innovation">
            </a>
            <a href="https://www.ontario.ca/page/ontario-research-fund" target="_blank" rel="noopener" aria-label="Ontario Research Fund">
              <img src="/images/funders/ontario.png" alt="Government of Ontario">
            </a>
            <a href="https://www.lg.com/ca_en/" target="_blank" rel="noopener" aria-label="LG" class="homepage-funder-logo-wide">
              <img src="/images/funders/lg.png" alt="LG">
            </a>
            <a href="https://research.google/programs-and-events/tpu-research-cloud/" target="_blank" rel="noopener" aria-label="Google TPU Research Cloud">
              <img src="/images/funders/google.svg" alt="Google">
            </a>
            <a href="https://alliancecan.ca/" target="_blank" rel="noopener" aria-label="Digital Research Alliance of Canada" class="homepage-funder-logo-xwide">
              <img src="/images/funders/dra.png" alt="Digital Research Alliance of Canada">
            </a>
            <a href="https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/" target="_blank" rel="noopener" aria-label="NVIDIA Academic Grant Program">
              <img src="/images/funders/nvidia.png" alt="NVIDIA">
            </a>
            <a href="https://www.utoronto.ca/" target="_blank" rel="noopener" aria-label="University of Toronto" class="homepage-funder-logo-wide">
              <img src="/images/uot-logo.png" alt="University of Toronto">
            </a>
          </div>
        </div>
---
