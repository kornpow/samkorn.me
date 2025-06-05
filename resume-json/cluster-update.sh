#!/bin/bash

echo "Exporting resume to HTML..."
resume export \
    --resume resume.yaml \
    --format html \
    --theme macchiato \
    public/index.html

echo "Updating resume in cluster..."
kubectl create \
    configmap nginx-html \
    -n kornpow \
    --from-file=public/index.html \
    --dry-run=client -o yaml | kubectl apply -f -

echo "Done!"