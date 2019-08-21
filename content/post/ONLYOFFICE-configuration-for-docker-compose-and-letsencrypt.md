---
title: ONLYOFFICE configuration for docker-compose (and letsencrypt).
date: 2016-12-14 03:55:37
link: https://gist.github.com/kvaps/6ac945e6c2e2e41bd536b7486a7dea4a
---

- Run communityserver container, and get `onlyoffice.conf` from it:
```bash
docker run -name communityserver -i -t -d onlyoffice/communityserver`
# wait 1-2 minutes.
sudo docker exec -i -t communityserver /bin/bash -c 'cat /etc/nginx/sites-enabled/onlyoffice' > onlyoffice.conf`
sudo docker rm -fv communityserver
```

<!-- more -->
