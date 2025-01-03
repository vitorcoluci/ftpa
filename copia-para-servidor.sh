#!/bin/bash
cp index.html robots.txt search.json sitemap.xml styles.css ~/Downloads/ftpa-planejamento/
cp -r atividades custos dados inscricao justificativa localizacao organizacao publico-alvo site_libs sobre ~/Downloads/ftpa-planejamento/
cd ~/Downloads/ftpa-planejamento
git commit -am "subindo website"
git push origin main