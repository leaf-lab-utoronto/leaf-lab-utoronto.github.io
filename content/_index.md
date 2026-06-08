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
          <div class="section-heading homepage-welcome-profile col-12 col-md-3 d-flex flex-column align-items-center align-items-md-start">
            <h1 class="mb-0" style="align-self: center">Welcome</h1>  
            <div id="profile" style="align-self: center">
              <img class="avatar avatar-square homepage-profile-photo img-fluid"
              src="/images/nr_headshot_v2.jpg" alt="Nicholas Rhinehart"
              style="max-width: 270px; width: 100 percent; aspect-ratio: 1; object-fit: cover;"
              >
              <p class="cta-btns" style="display: flex; justify-content: center; column-gap: 1vw">
                <a href="/publication" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-book-open-reader pr-1" aria-hidden="true"></i>Read our work</a>
                <a href="/apply" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-flask pr-1" aria-hidden="true"></i>Join us</a>
              </p>
            </div>
          </div>
          <div class="col-12 col-md-9 homepage-welcome-copy-column">
            <div class="article-style homepage-welcome-copy">
              <p>Welcome to the homepage of the <strong>Learning, Embodied Autonomy, and Forecasting (LEAF)</strong> lab, affiliated with the <a href="https://robotics.utoronto.ca" target="_blank">Robotics Institute</a>, <a href="https://utias.utoronto.ca" target="_blank">Institute for Aerospace Studies</a>, and <a href="https://cs.utoronto.ca" target="_blank">Department of Computer Science</a> at the <a href="https://utoronto.ca" target="_blank">University of Toronto</a>. The LEAF lab is led by <a href="author/nicholas-rhinehart/">Prof. Nick Rhinehart</a>.</p>
              <p>One of our central aims is general-purpose model-based control: autonomous systems that can be directed to perform a wide range of tasks by combining accurate models of the world with learned objectives. Two capabilities are essential to this vision: <em>forecasting</em>, learning to predict future observations and outcomes from rich sensor data, and <em>reward learning</em>, inferring what humans actually want from demonstrations, preferences, and other feedback. Together, these would allow an agent to simulate what will happen under different actions and select behavior aligned with human intent, without requiring hand-designed rewards or task-specific engineering. Our research draws on imitation learning, reinforcement learning, generative modeling, and information theory, with applications spanning autonomous driving, robot navigation, manipulation, and beyond.</p>
              <p>Current research thrusts include: learning transferable world models over high-dimensional sensor data such as LiDAR and occupancy; using world models to enable realistic large-scale simulation and efficient planning; and learning reward and objective functions from human feedback so that autonomous systems can perform complex tasks in alignment with human intent.</p>
              <p>Interested in joining? Learn more <a href="/apply">here</a>.</p>
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
