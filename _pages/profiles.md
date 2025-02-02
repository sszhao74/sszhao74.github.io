---
layout: profiles
permalink: /people/
title: people
description: members of the lab or group
nav: true
nav_order: 3
---

## Faculty Members

{% for faculty in site.data.faculty %}
<div class="faculty-profile">
  <img src="{{ faculty.image }}" alt="{{ faculty.name }}" class="faculty-image">
  <h2>{{ faculty.name }}</h2>
  <p><strong>Position:</strong> {{ faculty.position }}</p>
  <p>{{ faculty.bio }}</p>
</div>
{% endfor %}

## Students

<div class="student-grid">
{% for student in site.data.students %}
<div class="student-profile">
  <img src="{{ student.image }}" alt="{{ student.name }}" class="student-image">
  <h3>{{ student.name }}</h3>
  <p><strong>Lab:</strong> {{ student.lab }}</p>
  <p><strong>Research Topic:</strong> {{ student.research_topic }}</p>
  <p>{{ student.bio }}</p>
</div>
{% endfor %}
</div>
