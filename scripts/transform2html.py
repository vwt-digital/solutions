from json2html import *
import glob, os, shutil, re, json

html_index_file='index.html'
http_regex=r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

# Create output directory (and deltree if it already exists)
path='../html'
shutil.rmtree(path, ignore_errors=True, onerror=None)
os.mkdir(path)

# Create output html index file
with open(os.path.join(path, html_index_file), "w") as html_output_file:
    html_output_file.write("<html><table>\n")

for filename in glob.iglob('../solutions/**', recursive=True):
    if os.path.isdir(filename): #filter directories
        if not os.path.exists(os.path.join(path,os.path.relpath(filename, '../solutions'))):
            os.mkdir(os.path.join(path,os.path.relpath(filename, '../solutions')))

    if os.path.isfile(filename): # filter files
        if not os.path.exists(os.path.join(path,os.path.relpath(filename, '../solutions'))):
            with open(filename) as in_file:
                print(in_file)

                with open(os.path.join(path, html_index_file), "a") as html_output_file:
                    tmp_filename = os.path.relpath(filename, '../solutions')+'.html'
                    html_output_file.write('<tr><td><a href="'+ tmp_filename +'">'+ tmp_filename +'</a></td></tr>\n')

                with open(os.path.join(path, os.path.relpath(filename, '../solutions'))+'.html', "w") as out_file:

                    json_data = json.load(in_file)

                    for environment in json_data['environments']:
                        for project in environment['projects']:
                            project['project'] = "https://console.cloud.google.com/home/dashboard?project="+project['project']

                    html_document = json2html.convert(json = json_data)
                    output=re.sub(http_regex, r"<a href=\g<0>>\g<0></a>", html_document)

                    out_file.write(output)


# Finalize output html index file
with open(os.path.join(path, html_index_file), "a") as html_output_file:
    html_output_file.write("</table></html>\n")
