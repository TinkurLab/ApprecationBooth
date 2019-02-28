# Unit: Upload photo to Flowdock flow

## Overview

1. Generate the Flowdock ready image file on the Pi and and save to Pi
1. Run `curl -v -X POST -F "event=file" -F "content=@FILENAME.jpg" https://TOKEN@api.flowdock.com/flows/ORGANIZATION_NAME/FLOW_NAME/messages` to upload image to Flowdock flow

# Prerequisites

1. Generate a token at https://flowdock.com/account/tokens
