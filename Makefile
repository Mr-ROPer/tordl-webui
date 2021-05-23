##
# tordl-webui
#
# @file
# @version 0.1

APP = ws

CORE = $(APP)/core

SASS_CC = sassc
SASS_DIR = $(APP)/static/styles

all: $(CORE)

# currently, it makes the most sense for `make` to run it after compilation.
# this is subject to change once a stable release is ready.
$(CORE): css run

css:
	$(foreach src, $(wildcard $(SASS_DIR)/*.sass), $(SASS_CC) $(src) $(basename $(src)).css)

run:
	FLASK_APP=$(CORE) flask run

clean:
	rm $(wildcard $(SASS_DIR)/*.css)

# end
