#!bin/bash
install_path="/home/chaseuelt/google-cloud-sdk"

if [ -d "$install_path" ]; then
  echo "installed"
else
  cd ~ && \
  curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-465.0.0-linux-x86_64.tar.gz && \
  tar -xf google-cloud-cli-465.0.0-linux-x86_64.tar.gz && \
  ./google-cloud-sdk/install.sh && \
  ./google-cloud-sdk/bin/gcloud init
fi



if [ -d "$1" ]; then
  ~/google-cloud-sdk/bin/gcloud compute scp $1 --compress --recurse instance-20240218-025258:/home/chaseuelt/	--zone=us-west4-b
elif [ -f "$1" ]; then
  ~/google-cloud-sdk/bin/gcloud compute scp $1 --compress instance-20240218-025258:/home/chaseuelt/	--zone=us-west4-b
fi

echo "SCP complete"
