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
This creates a self-contained HTML file which is located at `public/index.html`.

Export the resume into PDF format!
```bash
resume export --resume resume.json --format pdf  --theme macchiato public/resume.pdf

resume export --resume resume.json --format pdf --theme macchiato public/resume_$(date +"%Y%m%d_%H%M%S").pdf
```

## Deployment
### Kubernetes
In order to deploy this resume to the url `samkorn.me`, which is currently hosted using kubernetes, this `index.html` file must be added to a ConfigMap in the cluster.

```
kubectl create configmap nginx-html --from-file=public/index.html --dry-run=client -o yaml | kubectl apply -f -
```

