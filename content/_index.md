---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: |
        # Welcome to the Learning, Embodied Autonomy, and Forecasting Lab.
      text: 
        # {{< gallery album="highlights" >}}      
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '20px', '0']
  # - block: slider
  #   content:
  #     slides:
  #       - title:
  #         background:
  #           position: center
  #           image:
  #             filename: albums/highlights/cfo_teaser.jpg
  #             fit: contain
  #       - title:
  #         background:
  #           position: center
  #           image:
  #             filename: albums/highlights/deep_imitative_models.png
  #             fit: contain
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: 500px
      # Make the slides full screen within the browser window?
      is_fullscreen: false
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2000

  # See: https://hugoblox.com/blocks/hero/
  # - block: hero
  #   content:
  #     title: |
  #       The Learning, Embodied Autonomy, and Forecasting (LEAF) Laboratory

  #     cta:
  #       label: Foo
  #       url: google.com
  #     text: |
  #       <br>
        
  #       TODO Leaf lab description.
  
  # - block: collection
  #   content:
  #     title: Latest News
  #     subtitle:
  #     text:
  #     count: 5
  #     filters:
  #       author: ''
  #       category: ''
  #       exclude_featured: false
  #       publication_type: ''
  #       tag: ''
  #     offset: 0
  #     order: desc
  #     page_type: post
  #   design:
  #     view: card
  #     columns: '1'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}} {{% cta cta_link="./publications/" cta_text="Read our publications" %}}
  #   design:
  #     columns: '1'
---
