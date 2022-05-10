#!/usr/bin/bash

app_name='gratch'
po_dir="po"
pot_path="${po_dir}/gratch.pot"
linguas_path="${po_dir}/LINGUAS"

_fmt(){
    cf_files=$(find . -name "*.c" -o -name "*.h")
    for f in $cf_files
    do
        clang-format -i $f
    done
}

up_po(){
    [[ -f $pot_path ]] || touch $pot_path
    xgettext \
        -f po/POTFILES \
        -d gratch \
        -j -i --omit-header -n \
        --package-name=$app_name \
        -o $pot_path
    for l in $(cat $linguas_path | grep -v "^#" | grep -v "^\n")
    do
        l_po_path=${po_dir}/${l}.po
        [[ -f ${l_po_path} ]] || touch ${l_po_path}
        msgmerge \
            -i -v -U \
            ${l_po_path} ${pot_path}
    done
}

po_fmt(){
    for pf in $(ls ${po_dir} | grep ".po$" )
    do
        gmo_path=${po_dir}/${pf/.po/.gmo}
        echo "${po_dir}/${pf} --> ${gmo_path}"
        msgfmt \
            -o  ${gmo_path}\
            ${po_dir}/${p}
    done
}

$@
