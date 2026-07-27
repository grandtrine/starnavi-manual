<div class="cover-title">
  <h1>{{ config.site_name }}</h1>
  {% if config.site_description %}
  <p class="cover-subtitle">{{ config.site_description }}</p>
  {% endif %}
  {# extra 全体を言語別に差し替えると analytics 等も消えるため、版表記だけキーを分ける #}
  {% if config.theme.language == 'en' and config.extra.manual_date_en %}
  <p class="cover-date">{{ config.extra.manual_date_en }}</p>
  {% elif config.extra.manual_date %}
  <p class="cover-date">{{ config.extra.manual_date }}</p>
  {% endif %}
</div>
