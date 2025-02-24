---
layout: page
title: People
permalink: /people/
description: 
nav: true
nav_order: 3
display_categories: [work, fun]
horizontal: false
---

<div class="lablogo_container">
    <img src="/assets/img/logo/lab_ERFI.png" alt="ERFI Lab">
    <img src="/assets/img/logo/lab_Deer.png" alt="Deer Lab">
    <img src="/assets/img/logo/lab_BiWell.png" alt="BiWell Lab">
    <img src="/assets/img/logo/lab_Synteraction.png" alt="Synteraction Lab">
    <img src="/assets/img/logo/lab_MEI.png" alt="MEI Lab">
</div>

## Faculty Members
<hr>

{% for faculty in site.data.faculty %}
<div class="profile-style">
  <div class="info-container">
    <h4 style="font-weight: 600; margin-bottom: 24px">{{ faculty.name }}</h4>
    <div class="people_content"><strong>Position:</strong> {{ faculty.position }}</div>
    <div class="people_content"><strong>Lab:</strong> <a href="{{ faculty.lab_url }}">{{ faculty.lab }}</a></div>
    <div class="people_content"><strong>Bio:</strong> {{ faculty.bio | markdownify }}</div>
    <div class="people_content"><strong>Research Interests:</strong> 
        <span style="font-size: 14px; font-color: #666666; font-weight: 400">{{ faculty.researchInterests | markdownify }}</span>
    </div>
    <div class="more-info people_content">
      {{ faculty.more_info | markdownify }}
    </div>
    <div class="people_content"><strong>Web:</strong>
      <a class="btn btn-outline-secondary btn-sm" role="button" aria-pressed="true" href="{{ faculty.personal_url }}">Personal Homepage</a>
      <a class="btn btn-outline-info btn-sm" role="button" aria-pressed="true" href="{{ faculty.gs_url }}">Google Scholar</a>
    </div>
  </div>
  <div class="image-container" style="text-align: {{ faculty.align | default: 'right' }};">
    <img src="{{ faculty.image }}" alt="{{ faculty.name }}" {% if faculty.image_circular %}class="img-circle"{% endif %}>
  </div>
</div>
{% endfor %}

<div style="margin-bottom:48px"></div>

## Students 🧑‍🎓
<hr>
<div class="projects" style="margin-top:24px">
  {% assign students = site.data.students %}
  {% assign labs = students | map: 'lab' | uniq %}
  
  <!-- Display categorized students -->
  {% for lab in labs %}
  <a id="{{ lab }}" href=".#{{ lab }}">
    <h4 class="category" style="color:#999999;margin-top:16px;margin-bottom:8px;text-align:right;">#{{ lab }}</h4>
    <!-- <hr style="border-style: dashed;"> -->
  </a>
  {% assign categorized_students = students | where: "lab", lab %}
  
  <!-- Generate cards for each student -->
  <div class="row row-cols-1 row-cols-md-3">
    {% for student in categorized_students %}
      <div class="col mb-4">
        <div class="card hoverable">
          <div class="row g-0">
            {% if student.image %}
            <div class="col-md-4" style="display: flex;">
              <img style="object-fit: cover;" src="{{ student.image | relative_url }}" class="img-fluid rounded-start" alt="{{ student.name }}">
            </div>
            {% endif %}
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">{{ student.name }}</h5>
                <p class="card-text">{{ student.bio }}</p>
                <!-- <p class="card-text"><strong>Lab:</strong> {{ student.lab }}</p> -->
                <p class="card-text"><strong>Research Topic:</strong> {{ student.research_topic }}</p>
                
              </div>
            </div>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
  {% endfor %}
</div>