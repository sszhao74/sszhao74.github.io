---
layout: page
title: people
permalink: /people/
description: members of the lab or group
nav: true
nav_order: 3
display_categories: [work, fun]
horizontal: false
---


## Faculty Members

{% for faculty in site.data.faculty %}
- **{{ faculty.name }}**
  - **Position:** {{ faculty.position }}
  - **Bio:** {{ faculty.bio }}
  - **Image:** ![{{ faculty.name }}]({{ faculty.image }})
{% endfor %}

## Students

{% for student in site.data.students %}
- **{{ student.name }}**
  - **Lab:** {{ student.lab }}
  - **Research Topic:** {{ student.research_topic }}
  - **Bio:** {{ student.bio }}
  - **Image:** ![{{ student.name }}]({{ student.image }})
{% endfor %}
