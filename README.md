# Resume Application
This repo contains code and deployment information for a resume.

## resume-json

Resume-json defaults to using JSON, but YAML is nicer to edit. This command converts the json to yaml.
```bash
yq eval -P resume.json -oy > output.yaml
```
Export the resume using a theme to HTML format.
```bash
resume export --resume resume.json --format html  --theme macchiato public/index.html
```
