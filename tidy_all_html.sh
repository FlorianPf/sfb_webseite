echo Improving all HTML files using tidy.

date > tidy.log

for i in *.html; do
    echo $i >> tidy.log
    tidy -o $i -config tidy.conf $i 2>> tidy.log
done

file_num=$(grep '.html' tidy.log | wc -l)
err_num=$(grep 'Error:' tidy.log | wc -l)
warn_num=$(grep 'Warning:' tidy.log | wc -l)

echo Done: $err_num error\(s\) and $warn_num warning\(s\) in $file_num file\(s\).
