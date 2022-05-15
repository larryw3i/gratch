#!/usr/bin/bash

app_name='gratch'
po_dir='po'
pot_path="${po_dir}/${app_name}.pot"
linguas_path="${po_dir}/LINGUAS"

_xgettext(){
    xgettext -v -a --output=${pot_path} -f ${po_dir}/POTFILES
    for line in $(cat $linguas_path); do
    	[[ -f ${po_dir}/${line}.po ]] || cp ${pot_path} ${po_dir}/${line}.po
    done
    for _po in $(find ${po_dir}/ -name "*.po"); do
    	echo $_po
        msgmerge -U -v ${_po} ${pot_path}
    done
}

_format(){
    clang-format --files=.clang-format-files -i
}

xget(){     _xgettext;          }
_fmt(){     _format;            }

$1
