##
# tordl-webui
#
# @file
# @version 0.1

TARGET = ws/core

all: $(TARGET)

$(TARGET):
	FLASK_APP=$(TARGET) flask run

# end
