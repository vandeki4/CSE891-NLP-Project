Invoke-WebRequest -Uri http://www.statmt.org/europarl/v7/es-en.tgz -OutFile ./es-en.tgz -UseBasicParsing
tar -xzf ./es-en.tgz