echo Improving all HTML files using tidy.

date > tidy.log

declare -a arr=("archiv.html"
                "dfmm-lv.html"
                "dwz-liste.html"
                "impressum.html"
                "index.html"
		"jugend.html"
                "kalender.html"
                "mannschaften.html"
                "turniere_schlopo.html"
                "turniere_stm.html"
                "turniere_vm.html"
                "turniere.html"
                "vereinsgeschichte.html"
                "vorstand.html"
                )
                
for i in "${arr[@]}"
do
    echo $i >> tidy.log
    tidy -o $i -config tidy.conf $i 2>> tidy.log
done

file_num=$(grep '.html' tidy.log | wc -l)
err_num=$(grep 'Error:' tidy.log | wc -l)
warn_num=$(grep 'Warning:' tidy.log | wc -l)

echo Done: $err_num error\(s\) and $warn_num warning\(s\) in $file_num file\(s\).
