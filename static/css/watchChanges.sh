#!/bin/bash
while true; do   change=$(inotifywait -e close_write,moved_to,create .);   change=${change#./ * };   if [ "$change" = "game.less" ]; then lessc game.less > game.css; fi; done
