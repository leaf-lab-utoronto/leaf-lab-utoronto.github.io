---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: 'Welcome'
      # image:
      #   # Reference an image in your `assets/media/` folder
      #   filename: coders.jpg
      # Add your Call-To-Action (CTA) button and optional icon
      cta:
        label: Read our publications
        url: publication
        icon_pack: fas
        icon: book-open-reader
      # Optionally, add an alternative CTA link
      cta_alt:
        label: Contact Us
        url: contact
        icon_pack: fas
        icon: email
      # Optionally, add a note under the Call-To-Action button
      # cta_note:
      #   label: >-
      #     foo       
      # Add your Hero text here
      text: |
        <div style="display: flex; justify-content: flex-start; flex-direction: row; align-items: start; flex-wrap: wrap; width: 100%">
        <img class="avatar avatar-circle" src="/images/nr_headshot_v1.jpg" alt="Nicholas Rhinehart" href="author/nicholas-rhinehart/" style="width: 250px; height: 100%; margin: 0;">
        <div style="align-self: top; font-size: medium; text-align: top; padding-left: 20px; min-width: 250px; max-width: 500px">
          Welcome to the Learning, Embodied Autonomy, and Forecasting (LEAF) lab, part of the <a href="https://utoronto.ca" target="_blank">University of Toronto</a>, <a href="https://utias.utoronto.ca" target="_blank">UTIAS</a>, and the <a href="https://robotics.utoronto.ca" target="_blank">Robotics Institute</a>. We aim to develop broadly useful autonomous systems that operate in complex, dynamic environments by advancing the algorithmic foundations of robot learning.
          <br><br>         
          Our research spans topics within <a href="./tag/robotics">robotics</a>, <a href="./tag/machine-learning">machine learning</a>, and <a href="./tag/computer-vision">computer vision</a>, and includes <a href="./tag/forecasting">forecasting</a>, <a href="./tag/imitation-learning">imitation learning</a>, <a href="./tag/reinforcement-learning">reinforcement learning</a>, <a href="./tag/reward-learning">reward learning</a>, and <a href="./tag/planning">planning</a>. The LEAF lab is led by <a href="author/nicholas-rhinehart/">Prof. Nick Rhinehart</a>.
        </div>
        </div>
        <br>

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
      title: Recent Publications
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
        </div>
        <div class="row">
        <div class="section-heading col-12 col-lg-4 mb-3 mb-lg-0 d-flex flex-column align-items-center align-items-lg-start">
          <h1 class="mb-0" style="visibility: hidden">Our research interests</h1>
        </div>
        <div class="row">
        <div style="display:flex; justify-content: space-between; column-gap: 3vw; row-gap: 1vw; font-size: medium; text-align:left">
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
        </div>
      design:
        columns: '1'
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
