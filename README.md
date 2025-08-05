# Resume Application
This repo contains code and deployment information for a resume.

## Custom Theme Installation

To install and use the custom "macchiato" theme:

1. Install the theme globally (optional, helps with some CLI features):
   ```bash
   cd jsonresume-theme-macchiato
   npm install -g
   ```

2. Use the theme with resume-cli using a relative path:
   ```bash
   cd resume-json
   resume export --resume resume.yaml --format html --theme ../jsonresume-theme-macchiato public/index.html
   ```

Alternatively, you can use the theme from within the resume-json directory:
```bash
cd resume-json
resume export --resume resume.yaml --format html --theme ../jsonresume-theme-macchiato output.html
```

## Working with Resume Data

Resume data can be edited in either JSON or YAML format. YAML is generally easier to edit and is preferred for making changes.

Convert the JSON resume to YAML for easier editing:
```bash
yq eval -P resume.json -oy > resume.yaml
```

Export the resume using a theme to HTML format:
```bash
cd resume-json
resume export --resume resume.yaml --format html --theme ../jsonresume-theme-macchiato public/index.html
```

This creates a self-contained HTML file which is located at `public/index.html`.

Export the resume into PDF format:
```bash
cd resume-json
resume export --resume resume.yaml --format pdf --theme ../jsonresume-theme-macchiato public/resume.pdf

# Export with timestamped filename
resume export --resume resume.yaml --format pdf --theme ../jsonresume-theme-macchiato public/resume_$(date +"%Y%m%d_%H%M%S").pdf
```

## Output for job submissions
```bash
cd resume-json
resume export \
    --resume resume.yaml \
    --format pdf \
    --theme ../jsonresume-theme-macchiato \
    public/resume-samkorn-$(date +"%m-%d-%Y").pdf
```
## Deployment
### Kubernetes
In order to deploy this resume to the url `samkorn.me`, which is currently hosted using kubernetes, this `index.html` file must be added to a ConfigMap in the cluster.

```bash
cd resume-json
resume export \
    --resume resume.yaml \
    --format html \
    --theme ../jsonresume-theme-macchiato \
    public/index.html

kubectl create \
    configmap nginx-html \
    -n kornpow \
    --from-file=public/index.html \
    --dry-run=client -o yaml | kubectl apply -f -
```

