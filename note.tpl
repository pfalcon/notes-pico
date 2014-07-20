{% args note %}
<li class="note col-xs-12 col-sm-6 col-lg-4">
  <div class="panel panel-primary">
    <div class="panel-heading">
      {{ note[1] }}
      <a
        class="btn btn-danger btn-xs archive-note pull-right"
        data-note="{{ note[0] }}"
        href="archive/{{ note[0] }}">&times;</a>
    </div>
    <div class="panel-body">
      {{ note[3] }}
    </div>
  </div>
</li>
