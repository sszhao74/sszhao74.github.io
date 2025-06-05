---
layout: page
title: Activities
permalink: /activities/
description: activities of KLIC
nav: false
nav_order: 1
display_categories: [work, fun]
horizontal: false
---

{% assign activities = site.data.activities %}
{% assign sorted_activities = activities | sort: 'date' | reverse %}

{% if sorted_activities.size > 0 %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for activity in sorted_activities %}
      {% include activity.liquid %}
    {% endfor %}
  </div>
{% else %}
  <p>No activities found.</p>
{% endif %}

