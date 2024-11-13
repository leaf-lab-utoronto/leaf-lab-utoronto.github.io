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
          <div class="section-heading col-12 col-lg-4 d-flex flex-column align-items-center align-items-lg-start">
            <h1 class="mb-0">Welcome</h1>  
            <div id="profile" style="align-self: center">
              <img class="avatar avatar-circle" width="270" height="270" src="/images/nr_headshot_v2.jpg" alt="Nicholas Rhinehart">
              <p class="cta-btns" style="display: flex; justify-content: center; column-gap: 1vw">
                <a href="/publication" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-book-open-reader pr-1" aria-hidden="true"></i>Read our work</a>
                <a href="/apply" class="btn btn-primary btn-md mb-md-1"><i class="fas fa-flask pr-1" aria-hidden="true"></i>Join us</a>
              </p>
            </div>
          </div>
          <div class="col-12 col-lg-8">
            <div class="article-style responsive-top-padding">
              <div>Welcome to the <strong>Learning, Embodied Autonomy, and Forecasting (LEAF)</strong> lab, part of the <a href="https://robotics.utoronto.ca" target="_blank">Robotics Institute</a> and <a href="https://utias.utoronto.ca" target="_blank">Institute for Aerospace Studies</a> at the <a href="https://utoronto.ca" target="_blank">University of Toronto</a>. The LEAF lab is led by <a href="author/nicholas-rhinehart/">Prof. Nick Rhinehart</a>.
              <br><br> 
              We aim to develop broadly useful autonomous systems that efficiently and safely operate in complex environments by advancing the algorithmic foundations of robot learning. By developing learning-based systems for forecasting and control, the LEAF lab equips autonomous systems with the ability to predict and respond to real-time changes in their environment. Our research develops principled algorithms by advancing and drawing upon methods from model-based and model-free reinforcement learning, imitation learning, information theory, and deep learning.
              <br><br>
              Several of the LEAF lab's current research thrusts are (i) developing transferable models by learning to forecast high-dimensional data, (ii) deep learning methods for jointly forecasting and planning motion in uncertain environments,  (iii) autonomous systems that learn from a variety of sources of human data -- demonstration data, preference feedback, and others -- in order to help them perform complex tasks safely and efficiently.
              <br><br>
              <strong>We are hiring (including for Fall 2025)</strong>. Interested in joining our lab? Learn more <a href="/apply">here</a>.
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
---
