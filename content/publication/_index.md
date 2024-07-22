---
# Listing view
# view: compact
# type: landing
view: citation

sections:
  - block: collection
    content:
      title: Recent Publications
      text: ""
      count: 3
      filters:
        folders:
          - publication
      page_type: publication
    design:
      view: citation
      columns: '1'
  # - block: collection
  #   id: publications
  #   content:
  #     title: Publications
  #     count: 0
  #     filters:
  #       folders:
  #       - publication
  #     sort_by: 'Date'
  #   design:
  #     view: citation
  #     type: listing
    

# Optional banner image (relative to `assets/media/` folder).
# banner:
#   caption: ''
#   image: ''
---
