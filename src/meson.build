gratch_sources = [
  'main.c',
  'gratch-window.c',
  'gratch-application.c',
]

gratch_deps = [
  dependency('libadwaita-1', version: '>= 1.0'),
]

gnome = import('gnome')

gratch_sources += gnome.compile_resources('gratch-resources',
  'gratch.gresource.xml',
  c_name: 'gratch'
)

executable('gratch', gratch_sources,
  dependencies: gratch_deps,
  install: true,
)
