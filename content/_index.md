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
        <div class="row">
          <div class="section-heading col-12 col-lg-4">
            <h1 class="mb-0">Welcome</h1>  
            <div id="profile">
              <img class="avatar avatar-circle" width="270" height="270" src="/author/nicholas-rhinehart/avatar_hu135f67f5c95d083c81bf1ae5ab9b832b_1472581_270x270_fill_q75_lanczos_center.jpg" alt="Nicholas Rhinehart">
              <p class="cta-btns responsive-top-padding" style="display: flex; justify-content: center; column-gap: 1vw">
                <a href="/publication" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-book-open-reader pr-1" aria-hidden="true"></i>Read our work</a>
                <a href="/contact" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-envelope pr-1" aria-hidden="true"></i>Contact us</a>
              </p>
            </div>
          </div>
          <div class="col-12 col-lg-8">
            <div class="article-style responsive-top-padding">
              <div>Welcome to the Learning, Embodied Autonomy, and Forecasting (LEAF) lab, part of the <a href="https://robotics.utoronto.ca" target="_blank">Robotics Institute</a> and <a href="https://utias.utoronto.ca" target="_blank">Institute for Aerospace Studies</a> at the <a href="https://utoronto.ca" target="_blank">University of Toronto</a>.
              <br><br>
              We aim to develop broadly useful autonomous systems that safely operate in complex environments by advancing the algorithmic foundations of robot learning. Our research develops efficient principled algorithms with methods from model-based and model-free reinforcement learning, imitation learning, information theory, and deep learning. 
              </div>
            </div>
          </div>
        </div>


  - block: collection
    content:
      title: News
      text: ""
      count: 5
      filters:
        folders:
          - event
    design:
      view: card
      columns: '2'
  - block: collection
    content:
      title: Recent publications
      text: ""
      count: 3
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
        <div class="row">
          <div class="section-heading col-12 col-lg-4 mb-3 mb-lg-0 d-flex flex-column align-items-center align-items-lg-start">
            <h1 class="mb-0">Our research interests</h1>  
          </div>
        <div class="col-12 col-lg-8">
          <div style="display:flex; justify-content: flex-start; column-gap: 1vw; row-gap: 1vw; font-size: medium; text-align:left; flex-wrap: wrap">
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
            <li><a href="./tag/planning">Planning</a></li>
            <li><a href="./tag/reward-learning">Reward learning</a></li>
            </ul>
            </div>
            <div>
            <h2>Applications:</h2>
            <ul>
            <li><a href="./tag/autonomous-driving">Autonomous driving</a></li>
            <li><a href="./tag/autonomous-exploration">Autonomous exploration</a></li>
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
  # - block: markdown
  #   content:
  #     title: ''
  #     text: |
  #       <div style="display: flex; justify-content: center; flex-direction: row; flex-wrap: nowrap; column-gap: 1vw">
  #         <a href="#"><img src="/images/logo.png" alt="LEAF Lab logo" style="height: 80px"></a>
  #         <div style="border-left: 1px solid #1E3765; height: 40px; margin-top: 20px; margin-bottom: 20px"></div>
  #         <a href="https://robotics.utoronto.ca"><img src="/images/ri-logo.png" style="height: 80px" alt="U of T Robotics Institute Logo"></a>
  #         <div style="border-left: 1px solid #1E3765; height: 40px; margin-top: 20px; margin-bottom: 20px"></div>
  #         <a href="https://utoronto.ca"><img src="/images/uot-logo.png" style="height: 80px" alt="U of T Logo"></a>
  #       </div>
  #       <hr style="width: 50%; background: 1px solid #1E3765"></hr>
  # - block: markdown
  #   content:
  #     title: ''
  #     text: ''
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}} {{% cta cta_link="./publications/" cta_text="Read our publications" %}}
  #   design:
  #     columns: '1'
---
