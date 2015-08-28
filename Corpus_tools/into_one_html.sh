#!/bin/bash
#thanks to sattu94 over at: http://www.linuxquestions.org/questions/linux-software-2/merge-of-html-files-into-a-single-html-or-pdf-284545/#post4390727 for the script
echo "Enter directory path pages:";
read html_path;
echo "Enter complete filename of the starting page:"
read start_page;
ls $html_path > "list.txt";
grep -iv "</body>" "$html_path/$start_page" | grep -iv "</html>" > "$html_path/all_merged.html";
for i in $(< list.txt)
do
	grep -iv "<body>" "$html_path/$i" | grep -iv "<html>" | grep -iv "</body>" | grep -iv "</html>" >> "$html_path/all_merged.html"
done
echo "</body></html>" >> "$html_path/all_merged.html"
echo "Merged file ---> $html_path/all_merged.html"
