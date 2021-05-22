##
# tordl-webui
#
# @file
# @version 0.1

APP = ws

TARGET = $(APP)/core

SASS_DIR = $(APP)/static/styles

all: $(TARGET)

CSS:
	$(foreach SRC, $(wildcard $(SASS_DIR)/*.sass), sassc $(SRC) $(basename $(SRC)).css)

$(TARGET): CSS
	FLASK_APP=$(TARGET) flask run

clean:
	rm $(wildcard $(SASS_DIR)/*.css)

# end
