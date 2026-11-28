.PHONY: build check serve serve-nexus

build:
	hugo --minify --cleanDestinationDir --printPathWarnings --panicOnWarning

check: build
	python3 scripts/check_site.py

serve:
	hugo server

serve-nexus:
	hugo server --bind "$${HOST:?}" --port "$${PORT:?}" \
		--baseURL "https://$${NEXUS_HOSTNAME:?}/" --appendPort=false \
		--renderToMemory --disableLiveReload
