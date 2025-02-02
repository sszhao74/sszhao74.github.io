---
layout: page
title: activities
permalink: /activities/
description: activities of KLIC
nav: true
nav_order: 1
display_categories: [work, fun]
horizontal: false
---

## Activities

{% for activity in site.data.activities %}
- **{{ activity.title }}**  
  *{{ activity.date }}*  
  {{ activity.description }}
  *Category: {{ activity.category }}*
{% endfor %}
