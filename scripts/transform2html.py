from json2html import *
import glob, os, shutil, re, json

# Create output directory (and deltree if it already exists)
path='../html'
shutil.rmtree(path, ignore_errors=True, onerror=None)
os.mkdir(path)

http_regex=r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'

for filename in glob.iglob('../config/solutions/**', recursive=True):
    if os.path.isdir(filename): #filter directories
        if not os.path.exists(os.path.join(path,os.path.relpath(filename, '../config/solutions'))):
            os.mkdir(os.path.join(path,os.path.relpath(filename, '../config/solutions')))

    if os.path.isfile(filename): # filter files
        if not os.path.exists(os.path.join(path,os.path.relpath(filename, '../config/solutions'))):
            with open(filename) as in_file:
                print(in_file)
                with open(os.path.join(path, os.path.relpath(filename, '../config/solutions'))+'.html', "w") as out_file:

                    json_data = json.load(in_file)

                    for environment in json_data['environments']:
                        for project in environment['projects']:
                            project['project'] = "https://console.cloud.google.com/home/dashboard?project="+project['project']

                    html_document = json2html.convert(json = json_data)
                    output=re.sub(http_regex, r"<a href=\g<0>>\g<0></a>", html_document)

                    out_file.write(output)
                out_file.closed
            in_file.closed


