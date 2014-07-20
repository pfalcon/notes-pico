Notes = window.Notes || {};

(function(exports, $) {
  function Editor() {
    this.form = $('form#note-form');
    this.editor = $('textarea#content');
    this.container = $('ul.notes');
    this.initialize();
  }

  Editor.prototype.initialize = function() {
    this.setupMasonry();
    this.setupNotes();
    this.setupForm();
    this.editor.focus();
  }

  Editor.prototype.setupMasonry = function() {
    var self = this;
    imagesLoaded(this.container, function() {
      self.container.masonry({'itemSelector': '.note'});
    });
  }

  Editor.prototype.setupNotes = function() {
    var self = this;
    $('a.archive-note').on('click', this.archiveNote);
  }

  Editor.prototype.archiveNote = function(e) {
    e.preventDefault();
    var elem = $(this);
    var panel = elem.parents('.panel');
    var self = this;
    $.post(elem.attr('href'), function(data) {
      if (data.success) {
        panel.remove();
        $('ul.notes').masonry();
      }
    });
  }

  Editor.prototype.setupForm = function() {
    var self = this;
    this.editor.on('keydown', function(e) {
      if (e.ctrlKey && e.keyCode == 13) {
        self.form.submit();
      }
    });
    this.form.submit(function(e) {
      e.preventDefault();
      self.addNote();
    });
    this.addMarkdownHelpers();
  }

  Editor.prototype.addNote = function() {
    var self = this;
    this.editor.css('color', '#464545');
    $.post(this.form.attr('target'), this.form.serialize(), function(data) {
      if (data.success) {
        self.editor.val('').focus();
        listElem = $(data.note);
        listElem.find('a.archive-note').on('click', self.archiveNote);
        self.container.prepend(listElem);
        self.container.masonry('prepended', listElem);
      } else {
        self.editor.css('color', '#dd1111');
      }
    });
  }

  Editor.prototype.addMarkdownHelpers = function() {
    var self = this;
    this.addHelper('indent-left', function(line) {
      return '    ' + line;
    });
    this.addHelper('indent-right', function(line) {
      return line.substring(4);
    });
    this.addHelper('list', function(line) {
      return '* ' + line;
    });
    this.addHelper('bold', function(line) {
      return '**' + line + '**';
    });
    this.addHelper('italic', function(line) {
      return '*' + line + '*';
    });
    this.addHelper('font', null, function() {
      self.focus().select();
    });
  }

  Editor.prototype.addHelper = function(iconClass, lineHandler, callBack) {
    var link = $('<a>', {'class': 'btn btn-xs'}),
        icon = $('<span>', {'class': 'glyphicon glyphicon-' + iconClass}),
        self = this;

    if (!callBack) {
      callBack = function() {
        self.modifySelection(lineHandler);
      }
    }

    link.on('click', function(e) {
      e.preventDefault();
      callBack();
    });
    link.append(icon);
    this.editor.before(link);
  }

  Editor.prototype.modifySelection = function(lineHandler) {
    var selection = this.getSelectedText();
    if (!selection) return;

    var lines = selection.split('\n'),
        result = [];
    for (var i = 0; i < lines.length; i++) {
      result.push(lineHandler(lines[i]));
    }

    this.editor.val(
      this.editor.val().split(selection).join(result.join('\n'))
    );
  }

  Editor.prototype.getSelectedText = function() {
    var textAreaDOM = this.editor[0];
    return this.editor.val().substring(
      textAreaDOM.selectionStart,
      textAreaDOM.selectionEnd);
  }

  exports.Editor = Editor;
})(Notes, jQuery);