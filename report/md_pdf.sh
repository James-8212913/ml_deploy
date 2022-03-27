#!/bin/bash
printf "%s\n" "Converting Markdown to PDF"
pandoc \
  --standalone \
  --template=eisvogel \
  --citeproc \
  --listings \
  keyinfo.yaml \
  ml_deploy_report.md \
  -o James_Murray_13879046_ml_report.pdf

printf "%s\n" "Finished"
