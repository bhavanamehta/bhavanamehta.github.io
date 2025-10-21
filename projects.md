---
layout: default
title: Projects
permalink: /projects/
---
<link rel="stylesheet" href="{{ '/assets/css/projects.css' | relative_url }}">

<section class="projects-intro">
  <h1>Projects</h1>
  <p>Selected work. Click a card to open the project page or download the files.</p>
</section>

<section class="projects-grid">
  {% for project in site.data.projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</section>