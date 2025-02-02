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

{% for activity in site.data.activities %}
- **{{ activity.title }}**  
  *{{ activity.date }}* *Category: {{ activity.category }}* 
  {{ activity.description }} 
{% endfor %}
